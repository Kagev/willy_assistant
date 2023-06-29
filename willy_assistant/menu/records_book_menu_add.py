
from project_willy.methods.data import RECORDS_BOOK, autosave
from project_willy.methods.records_book_methods import Record, Name, Phone, Email, Birthday
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.records_book_menu_add_text import AddRecordMenuText
from project_willy.text_fields.general_text import GeneralText


class AddRecordMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.record = Record()
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(AddRecordMenuText.options_message)
            print(self.record.record_info())
            if not self.record.name:
                user_input = input(AddRecordMenuText.name_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_name_to_record(user_input)
            elif not self.record.phones:
                user_input = input(AddRecordMenuText.phone_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_phone_to_record(user_input)
            elif not self.record.email:
                user_input = input(AddRecordMenuText.email_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_email_to_record(user_input)
            elif not self.record.birthday:
                user_input = input(AddRecordMenuText.birthday_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_birthday_to_record(user_input)
            else:
                RECORDS_BOOK.add_record(self.record)
                autosave()
                print(AddRecordMenuText.add_successful_message)
                input(GeneralText.continue_input_message)
                return # to previous menu

# ADD FIELDS TO NEW RECORD
    @error_handler
    def add_name_to_record(self, user_input) -> None:
        name = Name(user_input)
        if name.value in RECORDS_BOOK.data:
            print(AddRecordMenuText.record_exists_message)
        else:
            self.record.add_name(name)

    @error_handler
    def add_phone_to_record(self, user_input) -> None:
        self.record.add_phone(Phone(user_input))

    @error_handler
    def add_email_to_record(self, user_input) -> None:
        self.record.add_email(Email(user_input))

    @error_handler
    def add_birthday_to_record(self, user_input) -> None:
        self.record.add_birthday(Birthday(user_input))
