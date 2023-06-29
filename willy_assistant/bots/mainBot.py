# bot = telebot.TeleBot('6277441276:AAFKtWsi-3NyXBVeGkEJd7sXZ0wRgnQngiQ')
import telebot
from telebot import types
import re
import hashlib
import json
import pathlib
import os

bot = telebot.TeleBot('6277441276:AAFKtWsi-3NyXBVeGkEJd7sXZ0wRgnQngiQ')


def validate_input(value, pattern, error_message):
    while not re.match(pattern, value):
        return error_message
    return value


class Authorization:
    def __init__(self, bot):
        self.bot = bot
        self.users = {}
        self.key = None
        self.password = None
        self.identifier = None
        self.salt = None
        self.max_attempts = 5
        self.authorized_users = set()  # Set to store authorized Telegram IDs

    def load_users(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / 'data'
            file_path = data_folder.joinpath('users.json')
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = {}  # Initialize as an empty dictionary if the loaded data is not a dictionary
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}
            return False

    def save_users(self):
        data_folder = pathlib.Path(__file__).resolve().parent.parent / 'data'
        file_path = data_folder.joinpath('users.json')
        with open(file_path, "w") as file:
            json.dump(self.users, file, indent=4)

    def authorization_user(self, chat_id):
        self.load_users()

        username_pattern = r'^[A-Za-z]+$'
        email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
        phone_pattern = r'^(\d{12}|380\d{9})$'
        password_pattern = r'^.{4,16}$'

        msg = self.bot.send_message(chat_id, "Enter your login/phone/e-mail (English characters only)")
        self.bot.register_next_step_handler(msg, self.process_login_step)

    def process_login_step(self, message):
        self.identifier = validate_input(message.text.upper(), r'^[A-Za-z]+$', "Invalid username. Please enter an English username.")

        # Check if a user with the given identifier exists
        for user_data in self.users.values():
            if (
                self.identifier.upper() == user_data['username'].upper()
                or self.identifier.lower() == user_data['email'].lower()
                or self.identifier == user_data['phone']
            ):
                self.user_data = user_data
                break
        else:
            self.bot.send_message(message.chat.id, "User does not exist.")
            return

        msg = self.bot.send_message(message.chat.id, "Enter your password")
        self.bot.register_next_step_handler(msg, self.process_password_step)

    def process_password_step(self, message):
        self.password = message.text

        # Check the password
        self.salt = bytes.fromhex(self.user_data['salt'])
        self.key = bytes.fromhex(self.user_data['key'])
        new_key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100000)

        if self.key == new_key:
            # Correct password
            self.authorized_users.add(str(message.chat.id))  # Add Telegram ID to authorized users
            self.bot.send_message(message.chat.id, "Authorization successful. Welcome!")
        else:
            # Incorrect password
            self.bot.send_message(message.chat.id, "Invalid password. Please try again.")


class Registration:
    def __init__(self, bot):
        self.bot = bot
        self.users = {}

    def load_users(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / 'data'
            file_path = data_folder.joinpath('users.json')
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = {}  # Initialize as an empty dictionary if the loaded data is not a dictionary
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}
            return False

    def save_users(self):
        data_folder = pathlib.Path(__file__).resolve().parent.parent / 'data'
        file_path = data_folder.joinpath('users.json')
        with open(file_path, "w") as file:
            json.dump(self.users, file, indent=4)

    def registration_user(self, chat_id):
        self.load_users()

        msg = self.bot.send_message(chat_id, "Enter your login name (English characters only)")
        self.bot.register_next_step_handler(msg, self.process_username_step)

    def process_username_step(self, message):
        username = validate_input(message.text, r'^[A-Za-z]+$', "Invalid username. Please enter an English username.")

        if any(user_data['username'].lower() == username.lower() for user_data in self.users.values()):
            self.bot.send_message(message.chat.id, "Username already exists. Please choose a different username.")
            return

        msg = self.bot.send_message(message.chat.id, "Enter your email")
        self.bot.register_next_step_handler(msg, self.process_email_step, username)

    def process_email_step(self, message, username):
        email = validate_input(message.text, r'^[\w.-]+@[\w.-]+\.\w+$', "Invalid email. Please enter a valid email.")

        if any(user_data['email'].lower() == email.lower() for user_data in self.users.values()):
            self.bot.send_message(message.chat.id, "Email already exists. Please choose a different email.")
            return

        msg = self.bot.send_message(message.chat.id, "Enter your phone number (optional, in the format 380xxxxxxxxx)")
        self.bot.register_next_step_handler(msg, self.process_phone_step, username, email)

    def process_phone_step(self, message, username, email):
        phone = validate_input(message.text, r'^(\d{12}|380\d{9})$', "Invalid phone number. Please enter a valid phone number.")

        if any(user_data['phone'] == phone for user_data in self.users.values()):
            self.bot.send_message(message.chat.id, "Phone number already exists. Please choose a different phone number.")
            return

        msg = self.bot.send_message(message.chat.id, "Enter your password (4-16 characters)")
        self.bot.register_next_step_handler(msg, self.process_password_step, username, email, phone)

    def process_password_step(self, message, username, email, phone):
        password = validate_input(message.text, r'^.{4,16}$', "Invalid password. Please enter a password between 4 and 16 characters.")

        msg = self.bot.send_message(message.chat.id, "Confirm your password")
        self.bot.register_next_step_handler(msg, self.process_confirm_password_step, username, email, phone, password)

    def process_confirm_password_step(self, message, username, email, phone, password):
        confirm_password = message.text
        if confirm_password != password:
            self.bot.send_message(message.chat.id, "Passwords do not match. Please try again.")
            return

        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        user_id = str(len(self.users) + 1)

        self.users[user_id] = {
            'username': username,
            'email': email,
            'phone': phone,
            'salt': salt.hex(),
            'key': key.hex()
        }

        self.save_users()
        self.bot.send_message(message.chat.id, "Registration successful. Welcome!")

    def return_to_menu(self, message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Authorization', 'Registration')
        msg = self.bot.send_message(message.chat.id, 'Choose one of the options:', reply_markup=markup)
        self.bot.register_next_step_handler(msg, self.process_menu_choice)

    def process_menu_choice(self, message):
        choice = message.text.lower()
        if choice == 'authorization':
            auth = Authorization(self.bot)
            auth.authorization_user(message.chat.id)
        elif choice == 'registration':
            reg = Registration(self.bot)
            reg.registration_user(message.chat.id)
        else:
            self.return_to_menu(message)


@bot.message_handler(commands=['start', 'menu'])
def handle_start_menu(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Authorization', 'Registration')
    msg = bot.send_message(message.chat.id, 'Choose one of the options:', reply_markup=markup)
    bot.register_next_step_handler(msg, Registration(bot).process_menu_choice)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    