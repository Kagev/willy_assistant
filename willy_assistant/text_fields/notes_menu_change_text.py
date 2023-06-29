
class ChangeNotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. CHANGE TAGS', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE NOTES TEXT', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. DELETE NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CHOOSE ANOTHER NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    tags_input_message = 'Input some tags to begin.\n>>> '
    input_message = 'You are in "CHANGE NOTES MENU". Choose one of the options.\n>>> '
    tags_input_message = 'Input tags for notes, please.\n>>> '
    text_input_message = 'Input text of notes, please.\n>>> '
    empty_notes_book_message = '\nNotes book is empty. Nothing to look at.\n'
    notes_indx_input_message = 'Input number of one of notes to change.\n>>> '
    delete_input = 'Are you sure? Enter "y" to continue.\n>>> '
    change_successful_message = '\nThe notes has been changed successfully!\n'
    delete_successful_message = '\nThe notes has been deleted successfully!\n'
    no_matches_message = '\nNo matches. Try again\n'

    premenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE NOTES PREMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)

    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE NOTES SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO CHANGE NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
