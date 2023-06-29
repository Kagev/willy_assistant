
from project_willy.methods.data import RECORDS_BOOK, NOTES_BOOK, autosave

from project_willy.methods.imports import Path

from project_willy.methods.records_book_methods import RecordsBook
from project_willy.methods.notes_methods import NotesBook
from project_willy.methods.file_operations_methods import FileOperations
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.general_text import GeneralText
from project_willy.text_fields.records_book_menu_import_text import ImportMenuText


class ImportMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(ImportMenuText.options_message)
        while True:
            user_input = input(ImportMenuText.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            if self.import_records_book_from_pickle(user_input):
                return # to previous menu

    @error_handler
    def import_records_book_from_pickle(self, path_from_user: str) -> None:
        path_for_import = Path(path_from_user)
        if path_for_import.is_file():
            imported_records_book, imported_notes_book = FileOperations.import_from_pickle(path_for_import)
            if isinstance(imported_records_book, RecordsBook) and isinstance(imported_records_book, NotesBook):
                RECORDS_BOOK.update(imported_records_book)
                NOTES_BOOK.append(imported_notes_book)
                autosave()
                print(ImportMenuText.import_records_book_successful_message)
                input(GeneralText.continue_input_message)
                return True
            else:
                print(ImportMenuText.invalid_file_message)
        else:
            print(ImportMenuText.file_not_exists_message)
