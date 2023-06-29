
from project_willy.methods.data import RECORDS_BOOK, autosave
from project_willy.methods.imports import deepcopy

from project_willy.methods.records_book_methods import Record, Name, Phone, Email, Birthday
from project_willy.methods.menu_general_methods import General
from project_willy.methods.errors_processing import error_handler

from project_willy.text_fields.records_book_menu_change_text import ChangeRecordMenuText
from project_willy.text_fields.general_text import GeneralText


class ChangeRecordMenu(General):
# OPTIONS
    def __init__(self, record: Record = None) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_change_name,
        '2': self.option_change_phone,
        '3': self.option_change_email,
        '4': self.option_change_birthday,
        '5': self.option_get_another_record,
        '6': self.option_delete_record,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.record = record
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not RECORDS_BOOK.data:
            print(ChangeRecordMenuText.empty_records_book_message)
            input(GeneralText.continue_input_message)
            return # to previous menu
        else:
            while True:
                if not self.record:
                    print(ChangeRecordMenuText.premenu_options_message)
                    user_input = input(ChangeRecordMenuText.record_input_message)
                    self.options_handler(user_input, self.SUBMENU_OPTIONS)                    
                    self.get_record_to_change(user_input)
                else:
                    print(ChangeRecordMenuText.options_message)
                    print(self.record.show_record())
                    user_input = input(ChangeRecordMenuText.input_message)
                    if not self.options_handler(user_input, self.MENU_OPTIONS):
                        print(GeneralText.wrong_input_message)

# GET RECORD
    @error_handler
    def get_record_to_change(self, user_input) -> None:
        self.record = RECORDS_BOOK.get_record(Name(user_input))
        return True

#CHANGE NAME
    @error_handler
    def option_change_name(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            user_input = input(ChangeRecordMenuText.name_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_name_in_record(user_input):
                return # to main call
    
    @error_handler
    def change_name_in_record(self, user_input) -> None:
        old_record = deepcopy(self.record)
        self.record.add_name(Name(user_input))
        RECORDS_BOOK.add_record(self.record)
        RECORDS_BOOK.delete_record(old_record)
        autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        return True

# CHANGE PHONE
    @error_handler
    def option_change_phone(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            user_input = input(ChangeRecordMenuText.phone_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_phone_in_record(user_input):
                return # to main call

    @error_handler
    def change_phone_in_record(self, user_input) -> None:    
        self.record.add_phone(Phone(user_input))
        RECORDS_BOOK.add_record(self.record)
        autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        return True

# CHANGE EMAIL
    @error_handler
    def option_change_email(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            user_input = input(ChangeRecordMenuText.email_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_email_in_record(user_input):
                return # to main call

    @error_handler
    def change_email_in_record(self, user_input) -> None:
        self.record.add_email(Email(user_input))
        RECORDS_BOOK.add_record(self.record)
        autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        return True
    
# CHANGE BIRTHDAY
    @error_handler 
    def option_change_birthday(self) -> None:
        print(ChangeRecordMenuText.submenu_options_message)
        while True:
            user_input = input(ChangeRecordMenuText.birthday_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_birthday_in_record(user_input):
                return # to main call
    
    @error_handler
    def change_birthday_in_record(self, user_input) -> None:
        self.record.add_birthday(Birthday(user_input))
        RECORDS_BOOK.add_record(self.record)
        autosave()
        print(ChangeRecordMenuText.change_successful_message)
        input(GeneralText.continue_input_message)
        return True
    
# GET ANOTHER RECORD
    @error_handler
    def option_get_another_record(self) -> None:
        while True:
            user_input = input(ChangeRecordMenuText.record_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.get_record_to_change(user_input):
                return # to main call

# DELETE RECORD
    @error_handler
    def option_delete_record(self) -> None:
        user_input = input(ChangeRecordMenuText.delete_input)
        if user_input == 'y':
            RECORDS_BOOK.delete_record(self.record)
            self.record = None
            autosave()
            print(ChangeRecordMenuText.delete_successful_message)
            input(GeneralText.continue_input_message)
