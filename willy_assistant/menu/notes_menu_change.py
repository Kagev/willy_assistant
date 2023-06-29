
from project_willy.methods.data import NOTES_BOOK, autosave
from project_willy.methods.notes_methods import Notes
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.notes_menu_change_text import ChangeNotesMenuText
from project_willy.text_fields.general_text import GeneralText


class ChangeNotesMenu(General):
# OPTIONS
    def __init__(self, notes: Notes = None) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_change_tags,
        '2': self.option_change_notes_text,
        '3': self.option_delete_notes,
        '4': self.option_get_another_notes,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.notes = notes
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not NOTES_BOOK.data:
            print(ChangeNotesMenuText.empty_notes_book_message)
            input(GeneralText.continue_input_message)
            return # to previous menu
        else:
            while True:
                if not self.notes:
                    print(ChangeNotesMenuText.premenu_options_message)
                    user_input = input(ChangeNotesMenuText.tags_input_message)
                    self.options_handler(user_input, self.SUBMENU_OPTIONS)
                    self.get_notes_to_change(user_input)
                else:
                    print(ChangeNotesMenuText.options_message)
                    print(self.notes.notes_info())
                    user_input = input(ChangeNotesMenuText.input_message)
                    if not self.options_handler(user_input, self.MENU_OPTIONS):
                        print(GeneralText.wrong_input_message)                      


# GET NOTES TO CHANGE
    @error_handler
    def get_notes_to_change(self, user_input) -> bool:
        result = ''
        dict_of_notes = NOTES_BOOK.find_notes(user_input)
        if dict_of_notes:
            for indx, notes in dict_of_notes.items():
                result += f"\nNotes: {indx}\n\n{notes}\n"
        if result:
            while True:
                print(ChangeNotesMenuText.premenu_options_message)
                print(result)
                user_input = input(ChangeNotesMenuText.notes_indx_input_message)
                self.options_handler(user_input, self.SUBMENU_OPTIONS)
                if self.notes_choosing(dict_of_notes, user_input):
                    return True
        else:
            print(ChangeNotesMenuText.no_matches_message)
            input(GeneralText.continue_input_message)
    
    @error_handler
    def notes_choosing(self, dict_of_notes: dict, user_input: str) -> bool:
        self.notes = dict_of_notes[int(user_input.strip())]
        return True

#CHANGE TAGS
    @error_handler
    def option_change_tags(self) -> None:
        while True:
            print(ChangeNotesMenuText.submenu_options_message)
            user_input = input(ChangeNotesMenuText.tags_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_tags_in_notes(user_input):
                return #to main call

    @error_handler
    def change_tags_in_notes(self, user_input) -> None:
        self.notes.add_tags(user_input)
        self.notes.create_notes()
        autosave()
        print(ChangeNotesMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        return True

# CHANGE TEXT
    @error_handler
    def option_change_notes_text(self) -> None:
        while True:
            print(ChangeNotesMenuText.submenu_options_message)
            user_input = input(ChangeNotesMenuText.text_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_text_in_notes(user_input):
                return #to main call

    @error_handler
    def change_text_in_notes(self, user_input) -> None:
        self.notes.add_text(user_input)
        self.notes.create_notes()
        autosave()
        print(ChangeNotesMenuText.delete_successful_message)
        input(GeneralText.continue_input_message)
        return True

# GET ANOTHER NOTES
    @error_handler
    def option_get_another_notes(self) -> None:
        while True:
            print(ChangeNotesMenuText.submenu_options_message)
            user_input = input(ChangeNotesMenuText.tags_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.get_notes_to_change(user_input):
                return # to main call

# DELETE NOTES
    @error_handler
    def option_delete_notes(self) -> None:
        user_input = input(ChangeNotesMenuText.delete_input)
        if user_input == 'y':
            NOTES_BOOK.delete_notes(self.notes)
            self.notes = None
            autosave()
            print(ChangeNotesMenuText.delete_successful_message)
            input(GeneralText.continue_input_message)
