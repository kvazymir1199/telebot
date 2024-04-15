import os
import data

from pathlib import Path
from config import bot
from buttons import (markup_back,
                     button_catalog_markup,
                     button_day_of_weeks_markup,
                     button_lessons_markup)

BASE_DIR = Path(__file__).resolve().parent.parent


def handle_func(function_call, user_id):
    request_data = function_call.data
    data_to_message = {
        "question_1": lambda: send_message(user_id, data.question_1),
        "addition_lessons": lambda: send_message(user_id, data.addition_lessons),
        "students": lambda: send_message(user_id, data.students),
        "monday": lambda: send_message(user_id, data.monday),
        "tuesday": lambda: send_message(user_id, data.thursday),
        "wednesday": lambda: send_message(user_id, data.wednesday),
        "thursday": lambda: send_message(user_id, data.thursday),
        "friday": lambda: send_message(user_id, data.friday),
        "teachers": lambda: send_message(user_id, data.teachers),
        "russian": lambda: show_images(user_id, 'russian'),
        "geometria": lambda: show_images(user_id, 'geometria'),
        "algebra": lambda: show_images(user_id, 'algebra'),
        "physics": lambda: show_images(user_id, 'physics'),
        "VS": lambda: show_images(user_id, 'vs'),
        "select_day": lambda: show_menu(user_id, data.select_day, button_day_of_weeks_markup),
        "back": lambda: show_menu(user_id, data.main_menu, button_catalog_markup),
        "theory": lambda: show_menu(user_id, data.select_lesson, button_lessons_markup)
    }

    message_function = data_to_message.get(request_data)
    if message_function:
        message_function()


def show_menu(user_id, text, markup):
    bot.send_message(user_id, text, reply_markup=markup)


def send_message(user_id, message):
    bot.send_message(user_id, message, reply_markup=markup_back)


def show_images(user_id, folder):
    address = f'{BASE_DIR}/source/{folder}'
    for filename in os.listdir(address):
        bot.send_photo(user_id, open(os.path.join(address, filename), 'rb'))
    bot.send_message(user_id, data.vse, reply_markup=markup_back)
