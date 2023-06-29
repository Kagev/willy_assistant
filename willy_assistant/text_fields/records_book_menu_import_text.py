
class ImportMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---IMPORT MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO RECORDS BOOK MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)

    input_message = 'Specify path to your backup of records book.\n>>> '
    file_not_exists_message = '\nThe specified path does not exist. Try again.\n'
    invalid_file_message = '\nFile at the specified path is not valid.\n'
    import_records_book_successful_message = '\nRecords book has been successfully updated!\n'
