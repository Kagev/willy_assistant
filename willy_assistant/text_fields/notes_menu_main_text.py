
class NotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. ADD NEW NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE EXISTS NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SHOW NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CLEAR NOTES BOOK', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    input_message = 'You are in "NOTES MENU". Choose one of the options.\n>>> '
    clear_successful_message = '\nThe notes book has been cleared successfully!\n'
    clear_input = 'Are you sure? Enter "y" to continue.\n>>> '
    empty_notes_book_message = '\nNotes book is empty. Nothing to clear.\n'
