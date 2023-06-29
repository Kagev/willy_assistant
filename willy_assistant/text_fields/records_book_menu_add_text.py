
class AddRecordMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---ADDING RECORD MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO RECORDS BOOK MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    record_exists_message =  '\nRecord wiht this user alredy exists!\n'
    
    name_input_message = 'Input user first name and last, please. [First name required]\n>>> '
    phone_input_message = 'Input user phone and phone type, please. [Phone required]\n>>> '
    email_input_message = 'Input user email, please. [Not required]\n>>> '
    birthday_input_message = 'Input user birthday, please.[Not required]\n>>> '
    
    add_successful_message = '\nRecord has been successfully added to record book!\n'
