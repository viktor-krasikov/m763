import os

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_r = types.KeyboardButton("RIGHT")
    btn_d = types.KeyboardButton("DOWN")
    btn_l = types.KeyboardButton("LEFT")
    btn1 = types.KeyboardButton("-")
    btn_up = types.KeyboardButton("UP")
    btn2 = types.KeyboardButton("-")
    markup.add(btn2, btn_up, btn1, btn_l, btn_d, btn_r)
    bot.send_message(message.chat.id, "yo", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "UP"):
        if os.path.exists("left.txt"):
            os.rename("left.txt", "up.txt")
        if os.path.exists("right.txt"):
            os.rename("right.txt", "up.txt")
        if os.path.exists("down.txt"):
            os.rename("down.txt", "up.txt")

    elif (message.text == "DOWN"):
        if os.path.exists("left.txt"):
            os.rename("left.txt", "down.txt")
        if os.path.exists("right.txt"):
            os.rename("right.txt", "down.txt")
        if os.path.exists("up.txt"):
            os.rename("up.txt", "down.txt")

    elif (message.text == "RIGHT"):
        if os.path.exists("left.txt"):
            os.rename("left.txt", "right.txt")
        if os.path.exists("down.txt"):
            os.rename("down.txt", "right.txt")
        if os.path.exists("up.txt"):
            os.rename("up.txt", "right.txt")

    elif (message.text == "LEFT"):
        if os.path.exists("right.txt"):
            os.rename("right.txt", "left.txt")
        if os.path.exists("down.txt"):
            os.rename("down.txt", "left.txt")
        if os.path.exists("up.txt"):
            os.rename("up.txt", "left.txt")


bot.infinity_polling()
