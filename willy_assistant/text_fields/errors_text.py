
class ErrorsText:

    index_error_message = '\nSomething wrong, try again. [IndexError]\n'
    key_error_message = "\nI don't know what is this, sorry. [KeyError]\n"
    type_error_message = '\nSomething wrong, try again. [TypeError]\n'
    value_error_message = '\nSomething wrong, try again. [ValueError]\n'
    phone_error_message = '\nPhone must be numeric with 12 symbols. Phone type must be is one of "work", "mobile" or "home".\n'
    name_error_message = '\nFirst name or last name must be greater than one symbol and less than 16 symbols\n'
    email_error_message = '\nEmail must be less than 32 char and valid!\n'
    birthday_error_message = '\nBirthday must be in [dd-mm-yyyy] format and not in the future!\n'
    notes_error_message = '\nNotes must have tags and text no longer than 300 symbols!\n'
    exit_message = \
    '\n{:^40}\n'.format('---GOOD BYE---')+\
    '\n{:^40}\n'.format("HOPE WE MEET AGAIN!")
