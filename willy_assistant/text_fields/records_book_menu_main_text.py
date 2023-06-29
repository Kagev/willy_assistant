
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
    empty_notes_book_message = '\nRecords book is empty. Nothing to clear.\n'
    clear_input = 'Are you sure? Enter "y" to continue.\n>>> '
    clear_successful_message = '\nThe record book has been cleared successfully!\n'
