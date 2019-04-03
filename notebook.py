import datetime
class Note:
    last_id = 0
    def __init__(self,memo,tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        Note.last_id += 1
        self.id = Note.last_id
    def maatch(self,filter):
        return filter in self.memo or filter in self.tags
class Notebook:
    def __init__(self):
        self.notes = []
    def new_note(self, memo,tags =''):
        self.notes.append(Note(memo,tags))
    def modify_memo(self,note_id,memo):
        note = self._find_note(note_id)
        if note:
                note.memo = memo
                return True
        return False
    def modify_tags(self,note_id,tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
    
    def searche(self,filter):
        return [note for note in self.notes if note.maatch(filter)]
    def _find_note(self,note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
