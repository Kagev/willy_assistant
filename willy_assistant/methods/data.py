
from project_willy.methods.file_operations_methods import FileOperations
from project_willy.methods.records_book_methods import RecordsBook
from project_willy.methods.notes_methods import NotesBook

# RECORDS BOOK
def create_or_restore_records_book() -> RecordsBook:
    if FileOperations.AUTOSAVE_PATH.is_file():
        records_book, notes_book = FileOperations.import_from_pickle(FileOperations.AUTOSAVE_PATH)
        result = records_book
    else:
        result = RecordsBook()
    return result

# NOTES BOOK
def create_or_restore_notes_book() -> NotesBook:
    if FileOperations.AUTOSAVE_PATH.is_file():
        records_book, notes_book = FileOperations.import_from_pickle(FileOperations.AUTOSAVE_PATH)
        result = notes_book
    else:
        result = NotesBook()
    return result

# AUTOSAVE
def autosave():
    FileOperations.autosave_to_pickle(FileOperations.AUTOSAVE_PATH, RECORDS_BOOK, NOTES_BOOK)

RECORDS_BOOK = create_or_restore_records_book()
NOTES_BOOK = create_or_restore_notes_book()
