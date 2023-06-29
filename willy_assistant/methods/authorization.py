from abc import abstractmethod, ABC
import hashlib
import os
import pathlib
import json
import getpass
import re


class Authorization(ABC):
    @abstractmethod
    def __init__(self):
        self.user_data = None
        self.users = {}
        self.key = None
        self.password = None
        self.identifier = None
        self.salt = None
        self.max_attempts = 5

    @abstractmethod
    def load_users(self):
        pass

    @abstractmethod
    def validate_input(self, value, pattern, error_message):
        while not re.match(pattern, value):
            return error_message
        return value

    @abstractmethod
    def login(self):
        print("Enter your login name (email, phone number, or username)")
        self.identifier = input(">>>: ")

        for user_data in self.users.values():
            if (
                self.identifier.upper() == user_data["username"].upper()
                or self.identifier.lower() == user_data["email"].lower()
                or self.identifier == user_data["phone"]
            ):
                self.user_data = user_data

                for attempt in range(self.max_attempts):
                    print(f"Hello {self.identifier}! Enter your password")
                    self.password = getpass.getpass("Password: ")

                    self.salt = os.urandom(32)
                    self.salt = bytes.fromhex(self.user_data["salt"])
                    self.key = bytes.fromhex(self.user_data["key"])
                    new_key = hashlib.pbkdf2_hmac(
                        "sha256", self.password.encode("utf-8"), self.salt, 100000
                    )

                    if self.key == new_key:
                        print("Login successful")
                        print(
                            f'{self.user_data["username"]}, your personal assistant "Willy" welcomes you'
                        )
                        break
                    else:
                        print("Invalid password. Please try again.")
                else:
                    print("Exceeded maximum number of login attempts.")
                break
        else:
            print("User not found")


class AuthorizationUser(Authorization, ABC):
    def load_users(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / "data"
            file_path = data_folder.joinpath("users.json")
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = (
                        {}
                    )  # Initialize as an empty dictionary if the loaded data is not a dictionary
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}
            return False


class AuthorizationAdmin(Authorization, ABC):
    def load_users(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / "data"
            file_path = data_folder.joinpath("admin.json")
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = (
                        {}
                    )  # Initialize as an empty dictionary if the loaded data is not a dictionary
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}
            return False


if __name__ == "__main__":
    admin_authorization = AuthorizationAdmin()
    admin_authorization.load_users()
    admin_authorization.login()

    user_authorization = AuthorizationUser()
    user_authorization.load_users()
    user_authorization.login()
