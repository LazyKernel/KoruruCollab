from aqt import mw
from anki.notes import Note

from . import models

def addNote(deckId, model, fields):
    """ Adds a note to the collection, does not save collection """
    note = Note(mw.col, model)
    note.model()['did'] = deckId

    fields_copy = {key: fields[key] for key in fields if key in models.fields}

    for name, value in fields_copy.items():
        note[name] = value

    mw.col.addNote(note)

def bulkApplyOperations(deckId, operations):
    model = models.getKoruruNoteType()

    for fields in operations:
        if fields['type'] == 'add':
            addNote(deckId, model, fields)
        # update and delete operations currently not handled

    mw.col.save()

    # return number of successful operations
    return len(operations)
