import telebot
from telebot import types

bot = telebot.TeleBot('6711986876:AAExxaa_9itzltEoMq_87KrHljAAPx3lhW0')

def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "👋 Привет! Введи слово которое хочешь проверить на палиндром!")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (is_palindrome(message.text.lower().replace(' ',''))):
        bot.send_message(message.from_user.id, "Да, это палиндром")
    else:
        bot.send_message(message.from_user.id, "Нет, это не палиндром")


bot.polling(none_stop=True, interval=0)