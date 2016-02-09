class Diary:
    """
    This class represents a diary. It has such attributes as diary name(String), owner(type Person) and notes.
    """

    def __init__(self, name, owner):
        self.__name = name
        self.__owner = owner
        self.__notes = []
        self.__id = 0

    @property
    def owners_name(self):
        return self.__owner.name

    @property
    def owners_surname(self):
        return self.__owner.surname

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def get_notes(self, date=None):
        if date:
            print(date)
            return [note for note in self.__notes if note.created_date == date]
        else:
            return self.__notes

    def get_all_names(self):
        """
        Returns a list of names of all the notes.
        """
        return [note.name for note in self.__notes]

    def add_note(self, name, created_on, text, is_event=False, event_date=''):
        """
        Adds a new node with the target parameters to the notes list.
        """
        assert type(name) == str, 'Wrong type of name variable'
        assert type(created_on) == str, 'Wrong type of created_on variable'
        assert type(text) == str, 'Wrong type of text variable'
        assert type(is_event) == bool, 'Wrong type of is_event variable'
        assert type(event_date) == str, 'Wrong type of name variable'
        new_note = Note(name, created_on, text, is_event, event_date, self.__id)
        self.__notes.append(new_note)
        self.__id += 1

    def get_note_text(self, name, date):
        """
        Returns text of note with name given as a parameter and with target date.
        """
        notes = [note.text for note in self.__notes if note.name == name and note.created_date == date]
        if notes:
            return notes[0]
        return None

    def get_notes_date(self, date):
        """
        Returns a list of names for notes which were created on date.
        """
        return [note.name for note in self.__notes if note.created_date == date]

    def update_note(self, id, title=None, text=None, deadline=None):
        # note = [index for index in range(self.__notes if note.id == int(id)][0]
        id = int(id)
        if title:
            print('accepted title')
            self.__notes[id].name = title
        if text:
            self.__notes[id].text = text
        if deadline:
            self.__notes[id].event_date = deadline

    def remove_note(self, name, date):
        """
        Removes a note with name and date, given as a parameter.
        """
        note_to_remove = self.get_note_text(name, date)
        self.__notes.remove(note_to_remove)

    def remove_by_id(self, id):
        """
        Pretty, obvious that, this function deletes a note with attribute id = id.
        """
        if len([note for note in self.__notes if note.id == int(id)]) > 0:
            note = [note for note in self.__notes if note.id == int(id)][0]
            self.__notes.remove(note)


class Note:

    def __init__(self, name, created_date, note_text, is_event=False, event_date=None, id=0):
        self.__id = id
        self.__name = name
        self.__created_date = created_date
        self.__note_text = note_text
        self.__is_event = is_event
        self.__event_date = event_date

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def created_date(self):
        return self.__created_date

    @property
    def text(self):
        return self.__note_text

    @text.setter
    def text(self, text):
        self.__note_text = text

    @property
    def is_event(self):
        return self.__is_event

    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, date):
        self.__event_date = date


class Person:

    def __init__(self, name, surname, birthday):
        self.__name = name
        self.__birthday = birthday
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def birthday(self):
        return self.__birthday

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name

    @surname.setter
    def surname(self, surname):
        if type(surname) == str:
            self.__surname = surname
