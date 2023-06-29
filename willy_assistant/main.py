import getpass
import json
import sys
import pathlib

from project_willy.methods.registration import Registration
from project_willy.methods.authorization import Authorization
from project_willy.menu.main_menu import MainMenu
from project_willy.text_fields.general_text import GeneralText
from text_fields.auth_menu_text import AuthMenuText
from abc import abstractmethod, ABC


# ----------ENTER TO MAIN MENU----------
def main() -> None:
    print(AuthMenuText.auth_message)
    choice = input(
        " Pleas SING IN or REGISTER in programm.\n Enter your choice (1 or 2 or EXIT).\n\n >>>:  "
    )

    if choice == "0" or choice.upper() == "EXIT":
        print(f"Goodbye {getpass.getuser()}")
        sys.exit()
    elif choice == "1":
        registration = Registration()
        registration.registration_user()
        main()
    elif choice == "2":
        authorization = Authorization()
        authorization.load_users()
        authorization.login()

        if authorization.key:
            print("Authorization successful.")
            print("-------")
            print(GeneralText.start_message)
            input(GeneralText.continue_input_message)
            MainMenu()
        else:
            print("Try again")
            print(" ")
            main()

    else:
        print("Invalid choice")
        print("Try again")
        print(" ")
        main()


# ----------ENTRY POINT----------
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
    main()
