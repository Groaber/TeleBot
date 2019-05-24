import requests
import telebot
from telebot import types
import json


@bot.message_handler(content_types= ['text'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add('Boop')
    msg = bot.send_message(message.chat.id, 'Time to Boop', reply_markup= markup)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    if message.text == 'Boop':
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        chat_id = message.from_user.id
        bot.send_photo(chat_id=chat_id, photo=url)
        send_welcome(message)
bot.polling(none_stop= True)


