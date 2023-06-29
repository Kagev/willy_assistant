
class ShowRecordsMenuText:
    options_message =\
    '\n{:^40}\n{:^40}\n'.format('---SHOW RECORDS MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. FIND RECORD', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. SHOW BIRTHDAYS', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SHOW ALL RECORDS', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. DEBUG INFO', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO RECORDS BOOK MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---SHOW RECORDS SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO SHOW RECORDS MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    input_message = 'You are in "SHOW RECORDS MENU". Choose one of the options.\n>>> '
    days_input_message = 'Enter number of days to search. [Only digits!]\n>>> '
    search_input_message = 'Enter name, phone or email to find record.\n>>> '
    no_matches_message = "\nNo matches. Try again\n"
    record_not_exists_message = "\nRecord do not exists. Nothing to show\n"
    record_input_message = 'You want to see some record? But who will it be?\n>>> '
    empty_records_book_message = '\nRecord book is empty. Nothing to look at.\n'
    birthday_info = '\nCurrent year info.\n'
                        