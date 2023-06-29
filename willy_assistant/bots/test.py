import telebot
import re
import hashlib
import os
import pathlib
import json

# Создание экземпляра бота с указанием токена
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Класс для авторизации пользователя
class Authorization:
    def __init__(self):
        self.users = {}
        self.key = None
        self.password = None
        self.identifier = None
        self.salt = None
        self.max_attempts = 5
        
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

    def authorization_user(self, chat_id):
        self.load_users()

        username_pattern = r'^[A-Za-z]+$'
        email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
        phone_pattern = r'^(\d{12}|380\d{9})$'
        password_pattern = r'^.{4,16}$'

        msg = bot.send_message(chat_id, "Enter your login/phone/e-mail (English characters only)")
        bot.register_next_step_handler(msg, self.process_login_step)

    def process_login_step(self, message):
        self.identifier = self.validate_input(message.text.upper(), r'^[A-Za-z]+$', "Invalid username. Please enter an English username.")

        # Проверяем, существует ли пользователь с таким идентификатором
        for user_data in self.users.values():
            if (user_data['username'].upper() == self.identifier.upper() or
                    user_data['email'].lower() == self.identifier.lower() or
                    user_data['phone'] == self.identifier):
                self.user_data = user_data
                break
        else:
            bot.send_message(message.chat.id, "User does not exist.")
            return

        msg = bot.send_message(message.chat.id, "Enter your password")
        bot.register_next_step_handler(msg, self.process_password_step)

    def process_password_step(self, message):
        self.password = message.text

        # Проверяем пароль
        self.salt = bytes.fromhex(self.user_data['salt'])
        self.key = bytes.fromhex(self.user_data['key'])
        new_key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100000)

        if self.key == new_key:
            # Пароль верный
            bot.send_message(message.chat.id, "Authorization successful. Welcome!")
        else:
            # Пароль неверный
            bot.send_message(message.chat.id, "Invalid password. Authorization failed.")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    authorization = Authorization()
    authorization.load_users()
    authorization.authorization_user(message.chat.id)

# Запуск прослушивания сообщений
bot.polling()
