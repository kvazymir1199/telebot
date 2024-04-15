from config import bot
from buttons import button_start_markup, markup_back
from reg import register
from menu import handle_func
import wiki
from telebot.types import CallbackQuery

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@bot.message_handler(commands=['start'])
def start(message):
    us_nam = message.from_user.first_name
    us_id = message.chat.id
    register(user_name=us_nam, user_id=message.chat.id)
    bot.send_photo(us_id, open(f"{BASE_DIR}/source/fk/Greetings.png", 'rb'))
    bot.send_message(us_id, f"<b>{us_nam}</b>, привет!\nВыбери что тебя интересует", reply_markup=button_start_markup)


@bot.callback_query_handler(func=lambda call: True)
def response(request: CallbackQuery):
    user_id = request.message.chat.id
    handle_func(request, user_id)
    if request.data == "kalendar":
        bot.send_photo(user_id, open(f'{BASE_DIR}/source/fk/Calendar.png', 'rb'), reply_markup=markup_back)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, wiki.getwiki(message.text))


bot.polling()
