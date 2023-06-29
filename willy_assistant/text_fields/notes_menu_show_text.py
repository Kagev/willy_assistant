
class ShowNotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---SHOW NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. FIND NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. SORT ALL BY A-Z', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SORT ALL BY DATE', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. DEBUG INFO', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    empty_notes_book_message = '\nNotes book is empty. Nothing to look at.\n'
    input_message = 'You are in "SHOW NOTES MENU". Choose one of the options.\n>>> '
    search_input_message = 'Enter tags to find notes.\n>>> '
    no_matches_message = '\nNo matches. Try again\n'
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---SHOW NOTES SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO SHOW NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
