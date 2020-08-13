from aqt import mw
from anki.stdmodels import models

name = 'Koruru'
fields = ['word-jp', 'word-en', 'sentence-jp', 'sentence-en', 'media', 'koruru-id', 'operation-id']

front = '''

'''

back = '''

'''

css = '''

'''

def createModel():
    models = mw.col.models
    if not models.byName(name):
        newModel = models.new(name)
        for field in fields:
            f = models.newField(field)
            models.addField(newModel, f)
        template = models.newTemplate('Koruru Sentence')
        template['qftm'] = front
        template['afmt'] = back
        template['css'] = css
        models.addTemplate(newModel, template)
        models.add(newModel)

def getKoruruNoteType():
    return mw.col.models.byName(name)
