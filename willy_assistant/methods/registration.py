from abc import abstractmethod, ABC
import re
import hashlib
import os
import pathlib
import json
import getpass


def validate_input(value, pattern, error_message):
    while not re.match(pattern, value):
        print(error_message)
        value = input(">>>: ")
    return value


class Registration(ABC):
    @abstractmethod
    def __init__(self):
        self.useremail = None
        self.userphonenumber = None
        self.password = None
        self.username = None
        self.salt = None
        self.users = {}

    @abstractmethod
    def load_user(self):
        pass

    def save_user(self):
        pass

    def registration_user(self):
        self.load_user()

        username_pattern = r"^[A-Za-z]+$"
        email_pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
        phone_pattern = r"^(\d{12}|380\d{9})$"
        password_pattern = r"^.{4,16}$"

        print("Enter your login name (English characters only)")
        self.username = validate_input(
            input(">>>: ").upper(),
            username_pattern,
            "Invalid username. Please enter an English username.",
        )

        if any(
            user_data["username"] == self.username for user_data in self.users.values()
        ):
            print("Username already exists. Please choose a different username.")
            return

        print("Enter your email")
        self.useremail = validate_input(
            input(">>>: "),
            email_pattern,
            "Invalid email. Please enter a valid email address.",
        )

        print("Enter your phone number (optional, in the format 380xxxxxxxxx)")
        self.userphonenumber = input(">>>: ")
        if self.userphonenumber:
            self.userphonenumber = validate_input(
                self.userphonenumber,
                phone_pattern,
                "Invalid phone number. Please enter a 12-digit phone number or a phone number starting with '380'.",
            )
        else:
            self.userphonenumber = "380" + validate_input(
                input(">>>: "),
                r"^\d{9}$",
                "Invalid phone number. Please enter a 9-digit phone number.",
            )

        print("Enter your password (4 to 16 characters)")
        self.password = getpass.getpass(prompt="Password: ", stream=None)
        print("Enter your password again for confirmation")
        confirm_password = getpass.getpass(prompt="Password: ", stream=None)

        if self.password != confirm_password:
            print("Your passwords do not match!")
            return

        self.salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            "sha256", self.password.encode("utf-8"), self.salt, 100000
        )

        user_data = {
            "username": self.username,
            "email": self.useremail,
            "phone": self.userphonenumber,
            "salt": self.salt.hex(),
            "key": key.hex(),
        }

        user_id = str(len(self.users) + 1)
        self.users[user_id] = user_data
        self.save_user()

        print(f"Registration successful. ID: {user_id} - {self.username}")


class RegistrationAdmin(Registration, ABC):
    def __init__(self):
        super().__init__()

    def load_user(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / "data"
            file_path = data_folder.joinpath("admin.json")
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = (
                        {}
                    )  # Initialize as an empty dictionary if the loaded data is not a dictionary
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def save_user(self):
        data_folder = pathlib.Path(__file__).resolve().parent.parent / "data"
        data_folder.mkdir(parents=True, exist_ok=True)

        file_path = data_folder.joinpath("admin.json")
        with open(file_path, "w") as file:
            json.dump(
                self.users, file, indent=2
            )  # Add indent parameter for pretty formatting
            file.write("\n")  # Add newline character after each user


class RegistrationUser(Registration, ABC):
    def __init__(self):
        super().__init__()

    def load_user(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / "data"
            file_path = data_folder.joinpath("users.json")
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = (
                        {}
                    )  # Initialize as an empty dictionary if the loaded data is not a dictionary
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def save_user(self):
        data_folder = pathlib.Path(__file__).resolve().parent.parent / "data"
        data_folder.mkdir(parents=True, exist_ok=True)

        file_path = data_folder.joinpath("users.json")
        with open(file_path, "w") as file:
            json.dump(
                self.users, file, indent=2
            )  # Add indent parameter for pretty formatting
            file.write("\n")  # Add newline character after each user


if __name__ == "__main__":
    user_registration = RegistrationUser()
    user_registration.registration_user()

    admin_registration = RegistrationAdmin()
    admin_registration.registration_user()
