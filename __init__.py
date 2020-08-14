from aqt import mw
from aqt.utils import showInfo, getOnlyText
from aqt.qt import *

from . import web
from . import decks
from . import models
from . import notes


koruruEndpoint = web.WebEndpoint('https://koruru.org', 3001)

def syncFunction():
    def syncFun():
        koruruDecks = decks.getAllKoruruDecks()
        for deck in koruruDecks:
            highestOp = decks.getLastestOperationFromDeck(deck['deckId'])
            response = koruruEndpoint.get('/api/collab/' + str(deck['koruruId']) + '&' + str(highestOp))
            notes.bulkApplyOperations(deck['deckId'], response['operations'])

    def onDone(fut):
        showInfo('Succesfully synced decks from koruru.org')

    mw.taskman.with_progress(syncFun, on_done=onDone, label='Syncing from koruru.org...', immediate=True)


def addFunction():
    token = getOnlyText('Shared deck token: ')
    ops = 0

    def addFunc():
        if not models.noteTypeExists():
            models.createModel()
        
        response = koruruEndpoint.get('/api/collab/' + token)
        deckId = decks.createNewDeck(response['token'], response['name'])
        ops = notes.bulkApplyOperations(deckId, response['operations'])

    def onDone(fut):
        showInfo('Successfully executed {op} {opStr}.'.format(
            op=ops,
            opStr='operations.' if ops != 1 else 'operation.'
        ))
    
    mw.taskman.with_progress(addFunc, on_done=onDone, label='Syncing from koruru.org...', immediate=True)


def initGUI():
    mw.Koruru = QMenu('Koruru', mw)
    
    add = QAction('Add shared deck', mw)
    add.triggered.connect(addFunction)
    mw.Koruru.addAction(add)

    sync = QAction('Sync shared decks', mw)
    sync.triggered.connect(syncFunction)
    mw.Koruru.addAction(sync)

    mw.form.menubar.insertMenu(mw.form.menuHelp.menuAction(), mw.Koruru)

initGUI()
