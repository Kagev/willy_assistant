from imports import os, Path, traceback, deepcopy

from methods.records_book_methods import Name, Phone, Email, Birthday
from methods.records_book_methods import Record
from methods.records_book_methods import RecordsBook
from methods.file_operations_methods import FileOperations
from methods.errors import ExitFromCLI
from methods.errors_processing import error_handler

from methods.clean_folder import main as clean_folder

from text_fields.general_text import GeneralText
from text_fields.main_menu_text import MainMenuText
from text_fields.records_book_menu_text import RecordsBookMenuText, AddRecordMenuText, ChangeRecordMenuText, \
    ShowRecordsMenuText, ImportMenuText, ExportMenuText
from text_fields.notes_menu_text import NotesMenuText, AddNotesMenuText, ChangeNotesMenuText


# ----------MENUS & SUBMENUS----------

class General:
    AUTOSAVE_PATH = Path(os.getcwd()) / 'records_book_autosave.bin'

    file_operations = FileOperations

    def create_or_restore_records_book(self) -> RecordsBook:
        if self.AUTOSAVE_PATH.is_file():
            result = self.file_operations.import_from_pickle(self.AUTOSAVE_PATH)
        else:
            result = RecordsBook()
        return result

    @error_handler
    def options_handler(self, user_command: str, options: dict) -> None:
        command = user_command.strip().lower()
        if command in options:
            options[command]()

    def record_book_autosave(self):
        self.file_operations.export_to_pickle(self.AUTOSAVE_PATH, records_book)

    @error_handler
    def option_exit_from_cli(self) -> None:
        raise ExitFromCLI


class MainMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '1': self.option_records_book_menu,
            '2': self.option_notes_menu,
            '3': self.option_clean_folder_tool,
            '0': self.option_show_current_call_stack,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().options_handler
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(MainMenuText.options_message)
        while True:
            user_input = input(MainMenuText.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            print(GeneralText.wrong_input_message)

    # RECORDS BOOK
    @error_handler
    def option_records_book_menu(self) -> None:
        RecordsBookMenu()

    # NOTES MENU
    @error_handler
    def option_notes_menu(self) -> None:
        NotesMenu()

    # CLEAN FOLDER TOOL
    def option_clean_folder_tool(self) -> None:
        clean_folder()
        input(GeneralText.continue_input_message)
        MainMenu()

    # SHOW CURRENT CALL STACK
    @error_handler
    def option_show_current_call_stack(self) -> None:
        for line in traceback.format_stack():
            print(f'{line.strip()}\n')
        print(f'Number of calls: {len(traceback.format_stack())}\n')
        input(GeneralText.continue_input_message)
        MainMenu()


# RECORDS BOOK MENU
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
            '0': self.option_return_to_main_menu,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().options_handler
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(RecordsBookMenuText.options_message)
        while True:
            user_input = input(RecordsBookMenuText.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            print(GeneralText.wrong_input_message)

    # ADD RECORD
    @error_handler
    def option_add_record(self) -> None:
        AddRecordMenu()

    # CHANGE RECORD
    @error_handler
    def option_change_record(self) -> None:
        ChangeRecordMenu()

    # SHOW RECORDS
    @error_handler
    def option_show_records(self) -> None:
        ShowRecordsMenu()

    # IMPORT
    @error_handler
    def option_import(self) -> None:
        ImportMenu()

    # EXPORT
    @error_handler
    def option_export(self) -> None:
        ExportMenu()

    # CLEAR RECORDS BOOK
    @error_handler
    def option_clear_records_book(self) -> None:
        user_input = input(RecordsBookMenuText.clear_input)
        if user_input == 'y':
            records_book.clear()
            print(RecordsBookMenuText.clear_successful_message)
            input(GeneralText.continue_input_message)
            RecordsBookMenu()

    # RETURN MAIN MENU
    @error_handler
    def option_return_to_main_menu(self) -> None:
        MainMenu()


class AddRecordMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '0': self.option_return_to_records_book_menu,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().options_handler
        super().record_book_autosave
        self.record = Record()
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(AddRecordMenuText.options_message)
        while True:
            print(self.record.record_info())
            if not self.record.name:
                self.add_name_to_record()
            elif not self.record.phones:
                self.add_phone_to_record()
            elif not self.record.email:
                self.add_email_to_record()
            elif not self.record.birthday:
                self.add_birthday_to_record()
            else:
                records_book.add_record(self.record)
                self.record_book_autosave()
                print(AddRecordMenuText.add_successful_message)
                input(GeneralText.continue_input_message)
                MainMenu()

    # ADD FIELDS TO NEW RECORD
    @error_handler
    def add_name_to_record(self) -> None:
        user_input = input(AddRecordMenuText.name_input_message)
        self.options_handler(user_input, self.MENU_OPTIONS)
        name = Name(user_input)
        if name.value in records_book.data:
            print(AddRecordMenuText.record_exists_message)
        else:
            self.record.add_name(name)

    @error_handler
    def add_phone_to_record(self) -> None:
        user_input = input(AddRecordMenuText.phone_input_message)
        self.options_handler(user_input, self.MENU_OPTIONS)
        self.record.add_phone(Phone(user_input))

    @error_handler
    def add_email_to_record(self) -> None:
        user_input = input(AddRecordMenuText.email_input_message)
        self.options_handler(user_input, self.MENU_OPTIONS)
        self.record.add_email(Email(user_input))

    @error_handler
    def add_birthday_to_record(self) -> None:
        user_input = input(AddRecordMenuText.birthday_input_message)
        self.options_handler(user_input, self.MENU_OPTIONS)
        self.record.add_birthday(Birthday(user_input))

    # RETURN TO MAIN MENU
    @error_handler
    def option_return_to_records_book_menu(self) -> None:
        RecordsBookMenu()


class ChangeRecordMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.PREMENU_OPTIONS = {
            '0': self.option_return_to_main_menu,
            'exit': self.option_exit_from_cli,
        }
        self.MENU_OPTIONS = {
            '1': self.option_change_name,
            '2': self.option_change_phone,
            '3': self.option_change_email,
            '4': self.option_change_birthday,
            '5': self.option_get_another_record,
            '6': self.option_delete_record,
            '0': self.option_return_to_records_book_menu,
            'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
            '0': self.option_return_to_change_record_menu,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().record_book_autosave
        super().options_handler
        self.record = None
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not records_book.data:
            print(ChangeRecordMenuText.empty_records_book_message)
            input(GeneralText.continue_input_message)
            RecordsBookMenu()
        else:
            print(ChangeRecordMenuText.premenu_options_message)
            while True:
                self.get_record_to_change()

    # GET RECORD
    @error_handler
    def get_record_to_change(self) -> None:
        user_input = input(ChangeRecordMenuText.record_input_message)
        self.options_handler(user_input, self.PREMENU_OPTIONS)
        self.record = records_book.get_record(Name(user_input))
        self.change_record_menu()

    # CHANGE RECORD MENU
    @error_handler
    def change_record_menu(self) -> None:
        print(ChangeRecordMenuText.options_message)
        print(self.record.show_record())
        while True:
            user_input = input(ChangeRecordMenuText.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            print(GeneralText.wrong_input_message)

    # CHANGE NAME
    @error_handler
    def option_change_name(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            self.change_name_in_record()

    @error_handler
    def change_name_in_record(self) -> None:
        user_input = input(ChangeRecordMenuText.name_input_message)
        self.options_handler(user_input, self.SUBMENU_OPTIONS)
        old_record = deepcopy(self.record)
        self.record.add_name(Name(user_input))
        records_book.add_record(self.record)
        records_book.delete_record(old_record)
        self.record_book_autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        self.change_record_menu()

    # CHANGE PHONE
    @error_handler
    def option_change_phone(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            self.change_phone_in_record()

    @error_handler
    def change_phone_in_record(self) -> None:
        user_input = input(ChangeRecordMenuText.phone_input_message)
        self.options_handler(user_input, self.SUBMENU_OPTIONS)
        self.record.add_phone(Phone(user_input))
        records_book.add_record(self.record)
        self.record_book_autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        self.change_record_menu()

    # CHANGE EMAIL
    @error_handler
    def option_change_email(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            self.change_email_in_record()

    @error_handler
    def change_email_in_record(self) -> None:
        user_input = input(ChangeRecordMenuText.email_input_message)
        self.options_handler(user_input, self.SUBMENU_OPTIONS)
        self.record.add_email(Email(user_input))
        records_book.add_record(self.record)
        self.record_book_autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        self.change_record_menu()

    # CHANGE BIRTHDAY
    @error_handler
    def option_change_birthday(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            self.change_birthday_in_record()

    @error_handler
    def change_birthday_in_record(self) -> None:
        user_input = input(ChangeRecordMenuText.birthday_input_message)
        self.options_handler(user_input, self.SUBMENU_OPTIONS)
        self.record.add_birthday(Birthday(user_input))
        records_book.add_record(self.record)
        self.record_book_autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        self.change_record_menu()

    # GET ANOTHER RECORD
    @error_handler
    def option_get_another_record(self) -> None:
        while True:
            self.get_record_to_change()

    # DELETE RECORD
    @error_handler
    def option_delete_record(self) -> None:
        user_input = input(ChangeRecordMenuText.delete_input)
        if user_input == 'y':
            records_book.delete_record(self.record)
            self.record_book_autosave()
            print(ChangeRecordMenuText.delete_successful_message)
            input(GeneralText.continue_input_message)
            self.change_record_menu()

    # RETURN TO MAIN MENU
    @error_handler
    def option_return_to_main_menu(self) -> None:
        MainMenu()

    # RETURN TO RECORDS BOOK MENU
    @error_handler
    def option_return_to_records_book_menu(self) -> None:
        RecordsBookMenu()

    # RETURN TO CHANGE RECORD MENU
    @error_handler
    def option_return_to_change_record_menu(self) -> None:
        self.change_record_menu()


class ShowRecordsMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '1': self.option_find_record,
            '2': self.option_show_record,
            '3': self.option_show_all,
            '4': self.option_debug,
            '0': self.option_return_to_records_book_menu,
            'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
            '0': self.option_return_to_show_record_menu,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().options_handler
        self.record = None
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not records_book.data:
            print(ShowRecordsMenuText.empty_records_book_message)
            input(GeneralText.continue_input_message)
            MainMenu()
        else:
            while True:
                print(ShowRecordsMenuText.options_message)
                user_input = input(ShowRecordsMenuText.input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                print(GeneralText.wrong_input_message)

    # FIND RECORD
    @error_handler
    def option_find_record(self) -> None:
        print(ShowRecordsMenuText.submenu_options_message)
        while True:
            self.find_and_show_record()

    @error_handler
    def find_and_show_record(self) -> None:
        result = ''
        user_input = input(ShowRecordsMenuText.search_input_message)
        self.options_handler(user_input, self.SUBMENU_OPTIONS)
        result = records_book.find_record(user_input)
        if result:
            print(result)
            input(GeneralText.continue_input_message)
            ShowRecordsMenu()
        print(ShowRecordsMenuText.no_matches_message)

    # SHOW RECORD
    @error_handler
    def option_show_record(self) -> None:
        print(ShowRecordsMenuText.submenu_options_message)
        while True:
            self.get_and_show_record()

    @error_handler
    def get_and_show_record(self) -> None:
        user_input = input(ShowRecordsMenuText.record_input_message)
        self.options_handler(user_input, self.SUBMENU_OPTIONS)
        self.record = records_book.get_record(Name(user_input))
        print(self.record.show_record())
        input(GeneralText.continue_input_message)
        ShowRecordsMenu()

    # SHOW ALL
    @error_handler
    def option_show_all(self) -> None:
        print(records_book.show_records())
        input(GeneralText.continue_input_message)
        ShowRecordsMenu()

    # DEBUG
    @error_handler
    def option_debug(self) -> None:
        print(records_book.data)
        input(GeneralText.continue_input_message)
        ShowRecordsMenu()

    # RETURN TO SHOW RECORD MENU
    @error_handler
    def option_return_to_show_record_menu(self) -> None:
        ShowRecordsMenu()

    # RETURN TO RECORDS BOOK MENU
    @error_handler
    def option_return_to_records_book_menu(self) -> None:
        RecordsBookMenu()


class ImportMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '0': self.option_return_to_records_book_menu,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().options_handler
        super().file_operations
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(ImportMenuText.options_message)
        while True:
            user_input = input(ImportMenuText.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            self.import_records_book_from_pickle(user_input)
            print(ImportMenuText.file_not_exists_message)

    @error_handler
    def import_records_book_from_pickle(self, path_from_user: str) -> None:
        path_for_import = Path(path_from_user)
        if path_for_import.is_file():
            imported_records_book = self.file_operations.import_from_pickle(path_for_import)
            if isinstance(imported_records_book, RecordsBook):
                records_book.update(imported_records_book)
                print(ImportMenuText.import_records_book_successful_message)
                input(GeneralText.continue_input_message)
                RecordsBookMenu()

    # RETURN TO RECORDS BOOK MENU
    @error_handler
    def option_return_to_records_book_menu(self) -> None:
        RecordsBookMenu()


class ExportMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.EXPORT_MENU_OPTIONS = {
            '1': self.option_export_txt,
            '2': self.option_export_pickle,
            '3': self.option_export_json,
            '4': self.option_export_csv,
            '0': self.option_return_to_records_book_menu,
            'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
            '0': self.option_return_to_export_menu,
            'exit': self.option_exit_from_cli,
        }
        super().option_exit_from_cli
        super().options_handler
        super().file_operations
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(ExportMenuText.options_message)
        while True:
            user_input = input(ExportMenuText.input_message)
            self.options_handler(user_input, self.EXPORT_MENU_OPTIONS)
            print(GeneralText.wrong_input_message)

    # EXPORT TO TXT
    @error_handler
    def option_export_txt(self) -> None:
        print(ExportMenuText.submenu_options_message)
        while True:
            user_input = input(ExportMenuText.txt_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            self.records_book_to_txt(user_input)

    @error_handler
    def records_book_to_txt(self, path_from_user: str) -> None:
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.txt'
        else:
            path_for_export = Path(path_from_user + '.txt')
        records_book_as_dict = records_book.convert_to_dict()
        self.file_operations.export_to_txt(path_for_export, records_book_as_dict)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        RecordsBookMenu()

    # EXPORT TO PICKLE
    @error_handler
    def option_export_pickle(self) -> None:
        print(ExportMenuText.submenu_options_message)
        while True:
            user_input = input(ExportMenuText.pickle_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            self.records_book_to_pickle(user_input)

    @error_handler
    def records_book_to_pickle(self, path_from_user: str) -> None:
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.bin'
        else:
            path_for_export = Path(path_from_user + '.pickle')
        self.file_operations.export_to_pickle(path_for_export, records_book)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        RecordsBookMenu()

    # EXPORT TO JSON
    @error_handler
    def option_export_json(self) -> None:
        print(ExportMenuText.submenu_options_message)
        while True:
            user_input = input(ExportMenuText.json_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            self.records_book_to_json(user_input)

    @error_handler
    def records_book_to_json(self, path_from_user: str) -> None:  # TODO
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.json'
        else:
            path_for_export = Path(path_from_user + '.json')
        records_book_as_dict = records_book.convert_to_dict()
        self.file_operations.export_to_json(path_for_export, records_book_as_dict)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        RecordsBookMenu()

    # EXPORT TO CSV
    @error_handler
    def option_export_csv(self) -> None:
        print(ExportMenuText.submenu_options_message)
        while True:
            user_input = input(ExportMenuText.csv_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            self.records_book_to_csv(user_input)

    @error_handler
    def records_book_to_csv(self, path_from_user: str) -> None:  # TODO
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.csv'
        else:
            path_for_export = Path(path_from_user + '.csv')
        list_of_records = records_book.convert_record_to_list()
        self.file_operations.export_to_csv(path_for_export, list_of_records)
        print(ExportMenuText.records_book_successful_message)
        input(GeneralText.continue_input_message)
        RecordsBookMenu()

    # RETURN TO EXPORT OPTIONS
    @error_handler
    def option_return_to_export_menu(self) -> None:
        ExportMenu()

    # RETURN TO RECORDS BOOK MENU
    @error_handler
    def option_return_to_records_book_menu(self) -> None:
        RecordsBookMenu()


# NOTES MENU

class NotesMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '1': self.option_add_new_notes,
            '2': self.option_change_notes,
            '0': self.option_return_to_main_menu,
            'exit': self.option_exit_from_cli,
        }
        super().options_handler
        super().record_book_autosave
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(NotesMenuText.options_message)

    # RETURN TO NOTES MENU
    @error_handler
    def option_return_to_main_menu(self) -> None:
        MainMenu()


class AddNoteMenu():
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '0': self.option_retun_to_main_menu,
            'exit': self.option_exit_from_cli,
        }
        super().options_handler
        super().record_book_autosave
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(AddNotesMenuText.options_message)
        while True:
            pass

    # RETURN TO NOTES MENU
    @error_handler
    def option_retun_to_notes_menu(self) -> None:
        NotesMenu()


class ChangeNoteMenu(General):
    # OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
            '0': self.option_retun_to_notes_menu,
            'exit': self.option_exit_from_cli,
        }
        super().options_handler
        super().record_book_autosave
        self.__call__()

    # MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(ChangeNotesMenuText.options_message)
        while True:
            pass

    # RETURN TO NOTES MENU
    @error_handler
    def option_retun_to_notes_menu(self) -> None:
        NotesMenu()


records_book = General.create_or_restore_records_book(self=General)
notes = General.create_or_restore_records_book(self=General)

# def test_box() -> None:
#     name_1 = Name('test')
#     name_2 = Name('Scottie Bailey')
#     name_3 = Name('James Caporal')
#     name_4 = Name('Daniela Diaz')
#     name_5 = Name('Evan Eurs')

#     phone_1 = Phone('   111111111111    mobile')
#     phone_2 = Phone('esrser 222222222222 ')
#     phone_3 = Phone('    333333333333 work')
#     phone_4 = Phone('444444444444serrse')
#     phone_5 = Phone('esrser555555555555 home')

#     birthday_1 = Birthday('17-05-2000')
#     birthday_2 = Birthday('18-05-2000')
#     birthday_3 = Birthday('19-05-2000')
#     birthday_4 = Birthday('20-05-2000')
#     birthday_5 = Birthday(None)

#     email_1 = Email('example@email.net')
#     email_2 = Email('example@email.net')
#     email_3 = Email('example@email.net')
#     email_4 = Email('example@email.net')
#     email_5 = Email(None)

#     record_1 = Record(name_1, phone_1, email_1, birthday_1)

#     record_1.add_phone(phone_3)
#     record_1.add_phone(phone_4)
#     record_1.add_phone(phone_5)

#     record_2 = Record(name_2, phone_2, email_2, birthday_2)
#     record_3 = Record(name_3, phone_3, email_3, birthday_3)
#     record_4 = Record(name_4, phone_4, email_4, birthday_4)
#     record_5 = Record(name_5, phone_5, email_5, birthday_5)


#     records_book.add_record(record_1)
#     records_book.add_record(record_2)
#     records_book.add_record(record_3)
#     records_book.add_record(record_4)
#     records_book.add_record(record_5)

# test_box()
