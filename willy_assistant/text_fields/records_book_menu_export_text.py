
class ExportMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---EXPORT MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. TXT', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. PICKLE (RECOMENDED FOR BACKUP)', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. JSON', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CSV (TABLE WIEV)', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO RECORDS BOOK MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---EXPORT SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO EXPORT MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    empty_records_book_message = '\nRecord book is empty. Nothing to export.\n'
    input_message = 'Choose file format to export.\n>>> '
    txt_path_input_message = 'TXT. Specify the path for export.\n>>> '
    pickle_path_input_message = 'PICKLE. Specify the path for export.\n>>> '
    json_path_input_message = 'JSON. Specify the path for export.\n>>> '
    csv_path_input_message = 'CSV. Specify the path for export.\n>>> '
    records_book_successful_message = '\nRecords book has been successfully exported!\n'
