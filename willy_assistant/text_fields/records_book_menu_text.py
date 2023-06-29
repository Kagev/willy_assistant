
class RecordsBookMenuText:

    options_message =\
    '\n{:^40}\n{:^40}\n'.format('---RECORDS BOOK MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. ADD NEW RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE EXISTS RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SHOW RECORDS', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. IMPORT RECORDS BOOK', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('5. EXPORT RECORDS BOOK', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('6. CLEAR RECORDS BOOK', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    input_message = 'You are in "RECORDS BOOK MENU". Choose one of the options.\n>>> '
    clear_successful_message = '\nThe record book has been cleared successfully!\n'
    clear_input = 'Are you sure? Enter "y" to continue.\n>>> '


class AddRecordMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---ADDING RECORD MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    name_input_message = 'Input user first name and last, please. [First name required]\n>>> '
    phone_input_message = 'Input user phone and phone type, please. [Phone required]\n>>> '
    email_input_message = 'Input user email, please. [Not required]\n>>> '
    birthday_input_message = 'Input user birthday, please.[Not required]\n>>> '
    add_successful_message = '\nRecord has been successfully added to record book!\n'
    record_exists_message =  '\nRecord wiht this user alredy exists!\n'


class ChangeRecordMenuText:
    options_message =\
    '\n{:^40}\n{:^40}\n'.format('---CHANGE RECORD MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. CHANGE RECORD NAME', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE RECORD PHONE', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. CHANGE RECORD EMAIL', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CHANGE RECORD BIRTHDAY', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('5. CHOOSE ANOTHER RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('6. DELETE RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)

    empty_records_book_message = '\nRecord book is empty. Nothing to change.\n'
    record_not_exists_message = "\nRecord do not exists. First create record\n"
    input_message = 'You are in "CHANGE RECORD MENU". What do you want to change?\n>>> '
    
    record_input_message = 'Input name of record.\n>>> '
    name_input_message = 'Input new name for user.\n>>> '
    phone_input_message = 'Input new or additional phone for user.\n>>> '
    email_input_message = 'Input new email for user.\n>>> '
    birthday_input_message = 'Input new birthday date for user.\n>>> '
    change_successful_message = '\nRecord has been successfully changed.\n'
    delete_input = 'Are you sure? Enter "y" to continue.\n>>> '
    delete_successful_message = '\nRecord has been successfully deleted.\n'
    
    
    premenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE RECORD PREMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE RECORD SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO CHANGE RECORD MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)


class ShowRecordsMenuText:
    options_message =\
    '\n{:^40}\n{:^40}\n'.format('---SHOW RECORDS MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. FIND RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. SHOW RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SHOW ALL RECORDS', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. DEBUG', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---SHOW RECORDS SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO CHANGE RECORD MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    input_message = 'You are in "SHOW RECORDS MENU". Choose one of the options.\n>>> '
    search_input_message = 'Enter name, phone or email to find record.\n>>> '
    no_matches_message = "\nNo matches. Try again\n"
    record_not_exists_message = "\nRecord do not exists. Nothing to show\n"
    record_input_message = 'You want to see some record? But who will it be?\n>>> '
    empty_records_book_message = '\nRecord book is empty. Nothing to look at.\n'


class ImportMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---IMPORT MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)

    input_message = 'Specify path to your backup of records book.\n>>> '
    file_not_exists_message = '\nThe specified path does not exist. Try again.\n'
    import_records_book_successful_message = '\nRecords book has been successfully updated!\n'


class ExportMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---EXPORT MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. TXT', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. PICKLE (RECOMENDED FOR BACKUP)', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. JSON', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CSV (TABLE WIEV)', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---EXPORT SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO EXPORT MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    input_message = 'Choose file format to export.\n>>> '
    txt_path_input_message = 'TXT. Specify the path for export.\n>>> '
    pickle_path_input_message = 'PICKLE. Specify the path for export.\n>>> '
    json_path_input_message = 'JSON. Specify the path for export.\n>>> '
    csv_path_input_message = 'CSV. Specify the path for export.\n>>> '
    records_book_successful_message = '\nRecords book has been successfully exported!\n'
