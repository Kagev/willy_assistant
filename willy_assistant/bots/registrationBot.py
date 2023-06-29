import re
import hashlib
import json
import pathlib
import os

from personal_assistant.src.project_willy.bots.mainBot import bot
# bot = telebot.TeleBot('6277441276:AAFKtWsi-3NyXBVeGkEJd7sXZ0wRgnQngiQ')

class Registration:
    def __init__(self, bot):
        self.users = {}
        self.key = None
        self.password = None
        self.identifier = None
        self.salt = None

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

    def validate_input(self, value, pattern, error_message):
        while not re.match(pattern, value):
            return error_message
        return value

    def registration_user(self, bot, chat_id):        
        self.load_user()

        username_pattern = r'^[A-Za-z]+$'
        email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
        phone_pattern = r'^(\d{12}|380\d{9})$'
        password_pattern = r'^.{4,16}$'

        msg = bot.send_message(chat_id, "Enter your login name (English characters only)")
        bot.register_next_step_handler(msg, self.process_username_step)

    def process_username_step(self, bot, message):
        self.username = self.validate_input(message.text.upper(), r'^[A-Za-z]+$', "Invalid username. Please enter an English username.")
        if any(user_data['username'] == self.username for user_data in self.users.values()):
            bot.send_message(message.chat.id, "Username already exists. Please choose a different username.")
            return

        msg = bot.send_message(message.chat.id, "Enter your email")
        bot.register_next_step_handler(msg, self.process_email_step)

    def process_email_step(self, bot, message):
        self.useremail = self.validate_input(message.text, r'^[\w.-]+@[\w.-]+\.\w+$', "Invalid email. Please enter a valid email address.")

        msg = bot.send_message(message.chat.id, "Enter your phone number (optional, in the format 380xxxxxxxxx)")
        bot.register_next_step_handler(msg, self.process_phone_step)

    def process_phone_step(self, bot, message):
        self.userphonenumber = message.text
        if self.userphonenumber:
            self.userphonenumber = self.validate_input(self.userphonenumber, r'^(\d{12}|380\d{9})$', "Invalid phone number. Please enter a 12-digit phone number or a phone number starting with '380'.")
        else:
            msg = bot.send_message(message.chat.id, "Enter your phone number (9-digit)")
            bot.register_next_step_handler(msg, self.process_phone_validation_step)
    
        msg = bot.send_message(message.chat.id, "Enter your password (4 to 16 characters)")
        bot.register_next_step_handler(msg, self.process_password_step)
        

    def process_phone_validation_step(self, bot, message):
        self.userphonenumber = '380' + self.validate_input(message.text, r'^\d{9}$', "Invalid phone number. Please enter a 9-digit phone number.")

        msg = bot.send_message(message.chat.id, "Enter your password (4 to 16 characters)")
        bot.register_next_step_handler(msg, self.process_password_step)

    def process_password_step(self, bot, message):
        self.password = message.text

        msg = bot.send_message(message.chat.id, "Enter your password again for confirmation")
        bot.register_next_step_handler(msg, self.process_confirm_password_step)

    def process_confirm_password_step(self, bot, message):
        confirm_password = message.text

        if self.password != confirm_password:
            bot.send_message(message.chat.id, "Your passwords do not match!")
            return

        self.salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100000)

        user_data = {
            'username': self.username,
            'email': self.useremail,
            'phone': self.userphonenumber,
            'salt': self.salt.hex(),
            'key': key.hex()
        }

        user_id = str(len(self.users) + 1)
        self.users[user_id] = user_data
        self.save_user()

        bot.send_message(message.chat.id, f"Registration successful. ID: {user_id} - {self.username}")

    # Обработчик команды /start
    @bot.message_handler(commands=['Registration'])
    def start(message):
        registration = Registration()
        registration.registration_user(message.chat.id)


