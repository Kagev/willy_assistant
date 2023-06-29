
from project_willy.methods.data import NOTES_BOOK
from project_willy.methods.errors_processing import error_handler
from project_willy.methods.menu_general_methods import General

from project_willy.text_fields.notes_menu_show_text import ShowNotesMenuText
from project_willy.text_fields.general_text import GeneralText


class ShowNotesMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_find_record,            
        '2': self.option_sort_a_z,
        '3': self.option_sort_date,
        '4': self.option_debug,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not NOTES_BOOK.data:
            print(ShowNotesMenuText.empty_notes_book_message)
            input(GeneralText.continue_input_message)
        else:
            while True:
                print(ShowNotesMenuText.options_message)
                user_input = input(ShowNotesMenuText.input_message)
                if not self.options_handler(user_input, self.MENU_OPTIONS):
                    print(GeneralText.wrong_input_message)

# FIND RECORD
    @error_handler
    def option_find_record(self) -> None:
        while True:
            print(ShowNotesMenuText.submenu_options_message)
            user_input = input(ShowNotesMenuText.search_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            result = self.find_and_show_record(user_input)
            if result:
                print(result)
                input(GeneralText.continue_input_message)
                return # to main call

    @error_handler
    def find_and_show_record(self, user_input) -> str:
        dict_of_notes = NOTES_BOOK.find_notes(user_input)
        if dict_of_notes:
            return self.show_notes(dict_of_notes)
        print(ShowNotesMenuText.no_matches_message)

    @error_handler
    def show_notes(self, dict_of_notes: dict) -> str:
        result = ''
        for indx, notes in dict_of_notes.items():
            result += '\n{:^40}\n{:^40}\n'.format(f'Notes: {indx}', '-'*40)+f'{notes}'
        return result

# SHOW SORTED ALL BY A-Z
    @error_handler
    def option_sort_a_z(self) -> None:
        dict_of_notes = NOTES_BOOK.sort_by_tag()
        if dict_of_notes:
            print(self.show_notes(dict_of_notes))
        input(GeneralText.continue_input_message)   

# SHOW SORTED ALL BY DATE
    @error_handler
    def option_sort_date(self) -> None:
        dict_of_notes = NOTES_BOOK.sort_by_date()
        if dict_of_notes:
            print(self.show_notes(dict_of_notes))
        input(GeneralText.continue_input_message)   

# DEBUG
    @error_handler
    def option_debug(self) -> None:
        print(NOTES_BOOK)
        input(GeneralText.continue_input_message)
