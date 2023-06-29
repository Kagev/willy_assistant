
from project_willy.methods.data import NOTES_BOOK, autosave
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.notes_menu_main_text import NotesMenuText
from project_willy.text_fields.general_text import GeneralText

from project_willy.menu.notes_menu_add import AddNotesMenu
from project_willy.menu.notes_menu_change import ChangeNotesMenu
from project_willy.menu.notes_menu_show import ShowNotesMenu


class NotesMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_add_new_notes,
        '2': self.option_change_notes,
        '3': self.option_show_notes,
        '4': self.option_clear_notes_book,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(NotesMenuText.options_message)
            print(NOTES_BOOK.notes_calculatig())
            user_input = input(NotesMenuText.input_message)
            if not self.options_handler(user_input, self.MENU_OPTIONS):
                print(GeneralText.wrong_input_message)

    def option_add_new_notes(self) -> None:
        AddNotesMenu()
    
    def option_change_notes(self) -> None:
        ChangeNotesMenu()
        
    def option_show_notes(self) -> None:
        ShowNotesMenu()

# CLEAR NOTES BOOK
    @error_handler
    def option_clear_notes_book(self) -> None:
        if NOTES_BOOK.data:
            user_input = input(NotesMenuText.clear_input)
            if user_input == 'y':
                NOTES_BOOK.clear()
                autosave()
                print(NotesMenuText.clear_successful_message)
                input(GeneralText.continue_input_message)
        else:
            print(NotesMenuText.empty_notes_book_message)
            input(GeneralText.continue_input_message)
