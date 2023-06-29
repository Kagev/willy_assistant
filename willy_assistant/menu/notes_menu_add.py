
from project_willy.methods.data import NOTES_BOOK, autosave
from project_willy.methods.notes_methods import Notes
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.notes_menu_add_text import AddNotesMenuText
from project_willy.text_fields.general_text import GeneralText


class AddNotesMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.notes = Notes()
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(AddNotesMenuText.options_message)
        while True:
            print(self.notes.notes_info())
            if not self.notes['tags']:
                user_input = input(AddNotesMenuText.tags_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_tags_to_notes(user_input)
            elif not self.notes['notes']:
                user_input = input(AddNotesMenuText.tags_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_text_to_notes(user_input)
            else:
                self.notes.create_notes()
                NOTES_BOOK.add_notes(self.notes)
                autosave()
                print(AddNotesMenuText.add_successful_message)
                input(GeneralText.continue_input_message)
                return # to previous menu

# ADD FILEDS TO NOTES    
    @error_handler
    def add_tags_to_notes(self, user_input) -> None:
        self.notes.add_tags(user_input)
    
    @error_handler
    def add_text_to_notes(self, user_input) -> None:
        self.notes.add_text(user_input)
