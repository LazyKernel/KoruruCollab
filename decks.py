from aqt import mw
import re

p = re.compile(r'koruru-(\w*)')

def getAllKoruruDecks():
    ids = []
    for deck in mw.col.decks.all():
        match = p.match(deck.desc)
        if match:
            ids.append({'deckId': deck.id, 'koruruId': match.group()})
        
    return ids

def getKoruruDeck(koruruId):
    # very inefficient
    for deck in mw.col.decks.all():
        if deck.desc == 'koruru-{id}'.format(id=koruruId):
            return mw.col.decks.get(deck.id)

def createNewDeck(koruruId, name):
    deckId = mw.col.decks.id(name, create=False)
    if deckId:
        raise Exception('Deck with name {name} already exists.'.format(name=name))

    deckId = mw.col.decks.id(name)
    deck = col.decks.get(deckId)
    deck['desc'] = 'koruru-{id}'.format(id=koruruId)
    mw.col.decks.save(deck)
    return deckId

def getLastestOperationFromDeck(deckId):
    latestOp = -1
    for child in mw.col.decks.cids(deckId):
        note = mw.col.getCard(child).note()
        if note['operation-id'] > latestOp:
            latestOp = note['operation-id']
    return latestOp
