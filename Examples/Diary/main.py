from fsm import *
from diary import *
import time
import os


class Application:

    @staticmethod
    def create_diary():
        """
        In this function we create the table of transitions between programs states and get info about the user.
        """
        states_dict = {}

        states_dict[Application.__main_menu] = [('add note', None, Application.__add_note), ('add task', None, Application.__add_task), ('show tasks', None, Application.__show_all_tasks), ('show t_tasks', None, Application.__show_todays_tasks), ('show notes', None, Application.show_all_notes), ('exit', None, Application.exit)]
        states_dict[Application.__add_note] = [('view', None, Application.__show_note_by_id), ('apply', None, Application.__main_menu), ('cancel', None, Application.__remove_note)]
        states_dict[Application.__add_task] = [('view', None, Application.__show_task_by_id), ('apply', None, Application.__main_menu), ('cancel', None, Application.__remove_note)]
        states_dict[Application.show_all_notes] = [('main menu', None, Application.__main_menu), ('show note', None, Application.__show_note_by_id)]
        states_dict[Application.__show_all_tasks] = [('main menu', None, Application.__main_menu), ('show task', None, Application.__show_task_by_id), ('show t_tasks', None, Application.__show_todays_tasks)]
        states_dict[Application.__show_note_by_id] = [('edit', None, Application.__edit_current_note), ('delete', None, Application.__remove_note), ('return', None, Application.show_all_notes), ('main menu', None, Application.__main_menu)]
        states_dict[Application.__show_task_by_id] = [('edit', None, Application.__edit_current_task), ('delete', None, Application.__remove_note), ('return', None, Application.__show_all_tasks), ('main menu', None, Application.__main_menu)]
        states_dict[Application.__edit_current_note] = [('main menu', None, Application.__main_menu), ('return', None, Application.show_all_notes), ('message', None, Application.__show_note_by_id)]
        states_dict[Application.__edit_current_task] = [('main menu', None, Application.__main_menu), ('return', None, Application.__show_all_tasks), ('task', None, Application.__show_task_by_id), ('t tasks', None, Application.__show_todays_tasks)]
        states_dict[Application.__remove_note] = [('main menu', None, Application.__main_menu), ('notes', None, Application.show_all_notes), ('tasks', None, Application.__show_all_tasks)]
        states_dict[Application.__show_todays_tasks] = [('main menu', None, Application.__main_menu), ('show task', None, Application.__show_task_by_id)]

        Application.__brain = FSM(Application.__main_menu, states_dict, Application.__main_menu)

        owners_name = input('Enter your name')
        owners_surname = input('Enter your surname')
        owners_birthday = input('Enter your birthday dd/mm/yyyy')
        owner = Person(owners_name, owners_surname, owners_birthday)
        d_name = input('Enter diary`s name')
        Application.diary = Diary(d_name, owner)

    @staticmethod
    def exit():
        """
        This function is used simply to exit from the software. We need it to be able to have menu enty 'exit' as far as
        we need a staticmethod to call it from somewhere.
        """
        raise SystemExit(0)

    @staticmethod
    def __add_note():
        """
        This function is used to add a new note to the diary. Actually, we don`t need any checks here, so we don`t
        care about them.
        """
        os.system('clear')
        os.system('cls')
        title = input('Enter notes name: ')
        text = input('Enter note`s text: ')
        created_on = time.strftime('%x')
        Application.diary.add_note(title, created_on, text)
        Application.current_entry = Application.diary.id

    @staticmethod
    def __add_task():
        """
        This function is used to add a new task(note with a deadline) to the diary. Very same to
        add_note() function.
        """
        os.system('clear')
        os.system('cls')
        title = input('Enter tasks name: ')
        deadline = input('Enter tasks deadline(mm/dd/yy): ')
        text = input('Enter tasks text: ')
        created_on = time.strftime('%x')
        Application.diary.add_note(title, created_on, text, True, deadline)
        Application.current_entry = Application.diary.id

    def show_all_notes():
        """
        This function is used to print all the notes that user had entered to the system. If the
        lenght of the notes body is more then 100 characters, show only first 100 + ...
        """
        os.system('clear')
        os.system('cls')
        notes = [note for note in Application.diary.get_notes(None) if note.is_event is False]
        print('Notes in {} are:\n'.format(Application.diary.name))
        for note in notes:
            print(note.id)
            print(note.name)
            print(note.created_date)
            if len(note.text) > 100:
                print(note.text[0:100] + '....')
            else:
                print(note.text)
            print()

    @staticmethod
    def __show_all_tasks():
        """
        This function is used to print all the tasks that user had entered to the system. If the
        lenght of the notes body is more then 100 characters, show only first 100 + ...
        """
        os.system('clear')
        os.system('cls')
        tasks = [task for task in Application.diary.get_notes() if task.is_event is True]
        print('Tasks in {} are:\n'.format(Application.diary.name))
        for task in tasks:
            print(task.id)
            print(task.name)
            print(task.created_date)
            print(task.event_date)
            if len(task.text) > 100:
                print(task.text[0:100] + '....')
            else:
                print(task.text)
            print()

    @staticmethod
    def __show_note_by_id():
        """
        This function is used to show information about one note from the diary. Ids are unique so, we can
        use them to index our data.
        """
        id = input('Enter notes id: ')
        Application.current_entry = id
        print(Application.diary.get_notes())
        print(Application.diary.get_notes()[0].id)
        print(Application.diary.get_notes()[0].is_event)
        note = [note for note in Application.diary.get_notes() if str(note.id) == str(id) and note.is_event is False][0]
        os.system('clear')
        os.system('cls')
        print('Notes id is {}'.format(note.id))
        print('Notes name is: {}'.format(note.name))
        print('Notes was created on: {}'.format(note.created_date))
        print('Notes deadline is on: {}'.format(note.event_date))
        print('Note is:\n' + note.text)
        print()

    @staticmethod
    def __show_task_by_id():
        """
        This function is used to show information about one task from the diary. Ids are unique so, we can
        use them to index our data.
        """
        id = input('Enter tasks id: ')
        os.system('clear')
        os.system('cls')
        Application.current_entry = int(id)
        note = [note for note in Application.diary.get_notes() if note.id == int(id)][0]
        os.system('clear')
        os.system('cls')
        print('Notes id is {}'.format(note.id))
        print('Notes name is: {}'.format(note.name))
        print('Notes was created on: {}'.format(note.created_date))
        print('Notes deadline is on: {}'.format(note.event_date))
        print('Note is:\n' + note.text)
        print()

    @staticmethod
    def __show_entries_by_date():
        """
        This function is used to print all entries(notes and tasks) from the diary for a certain date.
        """
        date = str(input('Enter the date in format "mm/dd/yy"'))
        os.system('clear')
        os.system('cls')
        notes = Application.diary.get_notes_date(date)
        for note in notes:
            print('Notes id is {}'.format(note.id))
            print('Notes name is: {}'.format(note.name))
            print('Notes was created on: {}'.format(note.created_date))
            print('Notes deadline is on: {}'.format(note.event_date))
            print('Note is:\n' + note.text)
            print()

    @staticmethod
    def __show_todays_tasks():
        """
        This function is used to print the information about all the tasks from the diary which have deadline
        on the current date.
        """
        notes = [note for note in Application.diary.get_notes() if str(note.event_date) == str(time.strftime('%x'))]
        os.system('clear')
        os.system('cls')
        for note in notes:
            print('Notes id is {}'.format(note.id))
            print('Notes name is: {}'.format(note.name))
            print('Notes was created on: {}'.format(note.created_date))
            print('Notes deadline is on: {}'.format(note.event_date))
            print('Note is:\n' + note.text)
            print()

    @staticmethod
    def __edit_current_note():
        """
        This function is used to edit the note with id, which is saved is Application.current_entry. User can
        edit notes title and/or name.
        """
        os.system('clear')
        os.system('cls')

        title = input('Do you want to edit the title? (Y/n)? ')
        if title.lower() == 'y':
            new_title = input('Enter new title: ')
        else:
            new_title = None

        body = input('Do you want to edit the text of the note? (Y/n)? ')
        if body.lower() == 'y':
            new_body = input('Enter new text: ')
        else:
            new_body = None

        Application.diary.update_note(Application.current_entry, title=new_title, text=new_body)

    @staticmethod
    def __edit_current_task():
        """
        This function is used to edit the task with id, which is saved is Application.current_entry. User can
        edit tasks title, name and deadline..
        """
        os.system('clear')
        os.system('cls')
        title = input('Do you want to edit the title of the task? (Y/n)? ')
        if title.lower() == 'y':
            new_title = input('Enter new title: ')
        else:
            new_title = None

        body = input('Do you want to edit the text of the task? (Y/n)? ')
        if body.lower() == 'y':
            new_body = input('Enter new text: ')
        else:
            new_body = None

        deadline = input('Do you want to edit the deadline of the task? (Y/n)? ')
        if deadline.lower() == 'y':
            new_deadline = input('Enter new deadline(mm/dd/yy): ')
        else:
            new_deadline = [task for task in Application.diary.get_notes() if task.id == Application.current_entry][0].event_date
        Application.diary.update_note(Application.current_entry, title=new_title, text=new_body, deadline=new_deadline)

    @staticmethod
    def __remove_note():
        """
        This function removes an entry with id from Application.current_entry. We don`t care if the entry is a note or a task, because
        they are stored in the same list.
        """
        Application.diary.remove_by_id(Application.current_entry)

    @staticmethod
    def __main_menu():
        """
        We need this function because of the same reason as exit() : to be able to use this fucntion in the
        our finite state machine, which is in charge of software state.
        """
        pass

    @staticmethod
    def __print_menu():
        """
        This function is responsible for the main part of interaction with user. Actually, one of the reasons to add it, was that it
        very clear shows, that FSM is the main 'brain' of this program. We check the FSM`s state, and depending on it, print the user menu.
        """
        if Application.__brain.state == Application.__main_menu:
            print('Welcome to your diary, {}!\nYou`re in the main menu now. Here are available actions'.format(Application.diary.owners_name))
            print('Print "add note" to create a new note')
            print('Print "add task" to create a new task')
            print('Print "show tasks" to show all your tasks')
            print('Print "show t_tasks" to show all tasks which have deadline today')
            print('Print "show notes" to show all your notes')
            print('Print "exit" to exit the application')
        elif Application.__brain.state == Application.__add_note:
            print('To add the note print "apply"')
            print('To view the note print "view"')
            print('To cancel print "cancel"')
        elif Application.__brain.state == Application.__add_task:
            print('To add the task print "apply"')
            print('To view the task print "view"')
            print('To cancel print "cancel"')
        elif Application.__brain.state == Application.show_all_notes:
            print('To return to main menu print "main menu"')
            print('To view full info about one note print "show note"')
        elif Application.__brain.state == Application.__show_all_tasks:
            print('To view full info about one task print "show task"')
            print('To return to main menu print "main menu"')
        elif Application.__brain.state == Application.__show_todays_tasks:
            print('To view full info about one task print "show task"')
            print('To return to main menu print "main menu"')
        elif Application.__brain.state == Application.__show_note_by_id:
            print('To edit this note print "edit"')
            print('To delete this note print "delete"')
            print('To see all notes print "return"')
            print('To return to main menu print "menu"')
        elif Application.__brain.state == Application.__show_task_by_id:
            print('To edit this task print "edit"')
            print('To close this task print "close"')
            print('To see all task print "return"')
            print('To return to main menu print "menu"')
        elif Application.__brain.state == Application.__edit_current_note:
            print('To return to the list of all notes print "return"')
            print('To see current note print "message"')
            print('To return to the main menu print "main menu"')
        elif Application.__brain.state == Application.__edit_current_task:
            print('To see the list of all tasks print "return"')
            print('To see the list of todays tasks print "t tasks"')
            print('To see current task print "task"')
            print('To return to the main menu print "main menu"')
        elif Application.__brain.state == Application.__remove_note:
            print('To go to main menu print "main menu"')
            print('To see all notes print "notes"')
            print('To see all tasks print "tasks"')
        else:
            print(Application.__brain.state.__func__())
            print('asdasdasf')

    @staticmethod
    def run():
        """
        This is the loop function of the program. Just it.
        """
        while 1:
            try:
                Application.__print_menu()
                message = input()
                Application.__brain.handle_message(message)
                Application.__brain.state()
            except Exception:
                continue


Application.create_diary()
Application.run()
