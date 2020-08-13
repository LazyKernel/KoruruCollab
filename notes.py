from aqt import mw
from anki.notes import Note

def addNote(deck, model, fields):
    """ Adds a note to the collection, does not save collection """
    note = Note(mw.col, model)
    note.model()['did'] = deck['id']

    for name, value in fields.items():
        note[name] = value

    mw.col.addNote(note)

def bulkApplyOperations(operations):
    pass
