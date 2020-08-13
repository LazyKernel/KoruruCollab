# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

from . import web


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window
    #cardCount = mw.col.cardCount()
    # show a message box
    #showInfo("Card count: %d" % cardCount)

    #kanji = web.WebEndpoint('https://koruru.org', 3001).get('/api/kanji/list')
    #showInfo(str(kanji))
    pass

def syncFunction():
    pass

def addFunction():
    pass


def initGUI():
    mw.Koruru = QMenu('Koruru', mw)
    
    add = QAction('Add shared deck', mw)
    add.triggered.connect(addFunction)
    mw.Koruru.addAction(add)

    sync = QAction('Sync shared decks', mw)
    sync.triggered.connect(syncFunction)
    mw.Koruru.addAction(sync)

    action = QAction('Test', mw)
    action.triggered.connect(testFunction)
    mw.Koruru.addAction(action)

    mw.form.menubar.insertMenu(mw.form.menuHelp.menuAction(), mw.Koruru)

initGUI()
