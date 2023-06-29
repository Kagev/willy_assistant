
from project_willy.methods.data import RECORDS_BOOK

from project_willy.methods.imports import Path, os

from project_willy.methods.menu_general_methods import General
from project_willy.methods.file_operations_methods import FileOperations
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.general_text import GeneralText
from project_willy.text_fields.records_book_menu_export_text import ExportMenuText


class ExportMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_export_txt,
        '2': self.option_export_pickle,
        '3': self.option_export_json,
        '4': self.option_export_csv,
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
        if not RECORDS_BOOK.data:
            print(ExportMenuText.empty_records_book_message)
            input(GeneralText.continue_input_message)
            return # to previous menu
        else:
            while True:
                print(ExportMenuText.options_message)
                user_input = input(ExportMenuText.input_message)
                if not self.options_handler(user_input, self.MENU_OPTIONS):
                    print(GeneralText.wrong_input_message)

# EXPORT TO TXT
    @error_handler
    def option_export_txt(self) -> None:
        while True:
            print(ExportMenuText.submenu_options_message)
            user_input = input(ExportMenuText.txt_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_txt(user_input):
                return # to main call

    @error_handler
    def records_book_to_txt(self, path_from_user: str) -> None:
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.txt'
        else:
            path_for_export = Path(path_from_user+'.txt')
        records_book_as_dict = RECORDS_BOOK.convert_to_dict()
        FileOperations.export_to_txt(path_for_export, records_book_as_dict)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        return True

# EXPORT TO PICKLE
    @error_handler
    def option_export_pickle(self) -> None:
        print(ExportMenuText.submenu_options_message)
        while True:
            user_input = input(ExportMenuText.pickle_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_pickle(user_input):
                return # to main call

    @error_handler
    def records_book_to_pickle(self, path_from_user: str) -> None:
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.bin'
        else:
            path_for_export = Path(path_from_user+'.bin')
        FileOperations.export_to_pickle(path_for_export, RECORDS_BOOK)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        return True

# EXPORT TO JSON
    @error_handler
    def option_export_json(self) -> None:
        print(ExportMenuText.submenu_options_message)
        while True:
            user_input = input(ExportMenuText.json_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_json(user_input):
                return # to main call

    @error_handler   
    def records_book_to_json(self, path_from_user: str) -> None: #TODO
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.json'
        else:
            path_for_export = Path(path_from_user+'.json')
        records_book_as_dict = RECORDS_BOOK.convert_to_dict()
        FileOperations.export_to_json(path_for_export, records_book_as_dict)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        return True

# EXPORT TO CSV
    @error_handler
    def option_export_csv(self) -> None:
        print(ExportMenuText.submenu_options_message)        
        while True:
            user_input = input(ExportMenuText.csv_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_csv(user_input):
                return # to main call

    @error_handler
    def records_book_to_csv(self, path_from_user: str) -> None: #TODO
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.csv'
        else:
            path_for_export = Path(path_from_user+'.csv')
        list_of_records = RECORDS_BOOK.convert_record_to_list()
        FileOperations.export_to_csv(path_for_export, list_of_records)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        return True
