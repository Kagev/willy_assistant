
class ChangeRecordMenuText:
    options_message =\
    '\n{:^40}\n{:^40}\n'.format('---CHANGE RECORD MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. CHANGE RECORD NAME', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE RECORD PHONE', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. CHANGE RECORD EMAIL', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CHANGE RECORD BIRTHDAY', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('5. CHOOSE ANOTHER RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('6. DELETE RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO RECORDS BOOK MENU', '-'*40)+\
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
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO RECORDS BOOK MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE RECORD SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO CHANGE RECORD MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
