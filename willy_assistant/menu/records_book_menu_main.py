
from project_willy.methods.data import RECORDS_BOOK, autosave
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.menu.records_book_menu_add import AddRecordMenu
from project_willy.menu.records_book_menu_change import ChangeRecordMenu
from project_willy.menu.records_book_menu_show import ShowRecordsMenu
from project_willy.menu.records_book_menu_import import ImportMenu
from project_willy.menu.records_book_menu_export import ExportMenu

from project_willy.text_fields.records_book_menu_main_text import RecordsBookMenuText
from project_willy.text_fields.general_text import GeneralText


class RecordsBookMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_add_record,
        '2': self.option_change_record,
        '3': self.option_show_records,
        '4': self.option_import,
        '5': self.option_export,
        '6': self.option_clear_records_book,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(RecordsBookMenuText.options_message)
            print(RECORDS_BOOK.records_calculatig())
            user_input = input(RecordsBookMenuText.input_message)
            if not self.options_handler(user_input, self.MENU_OPTIONS):
                print(GeneralText.wrong_input_message)

# ADD RECORD
    def option_add_record(self) -> None:
        AddRecordMenu()

# CHANGE RECORD
    def option_change_record(self) -> None:
        ChangeRecordMenu()

# SHOW RECORDS
    def option_show_records(self) -> None:
        ShowRecordsMenu()

# IMPORT
    def option_import(self) -> None:
        ImportMenu()

# EXPORT
    def option_export(self) -> None:
        ExportMenu()

# CLEAR RECORDS BOOK
    @error_handler
    def option_clear_records_book(self) -> None:
        if RECORDS_BOOK.data:
            user_input = input(RecordsBookMenuText.clear_input)
            if user_input == 'y':
                RECORDS_BOOK.clear()
                autosave()
                print(RecordsBookMenuText.clear_successful_message)
                input(GeneralText.continue_input_message)
        else:
            print(RecordsBookMenuText.empty_notes_book_message)
            input(GeneralText.continue_input_message)
