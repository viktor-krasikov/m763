import telebot
from telebot import types

token = '6958457682:AAFp-TE7e65vo5dVR35jxdNd6zMB0xDxpSc'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_palindrome = types.KeyboardButton('Палиндром')
    key_sum = types.KeyboardButton('Сумма чисел')
    markup.add(key_palindrome, key_sum)
    bot.send_message(message.from_user.id, "Привет! Что хочешь сделать?", reply_markup=markup)


palindrome = False
summa = False


def is_palindrome(str):
    str = str.lower().replace(' ', '')
    return str == str[::-1]


def sum_num(text):
    text = text.lower()
    if text.isnumeric:
        text = [int(i) for i in text.split(' ')]
        return sum(text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global palindrome
    global summa
    if palindrome:
        if (is_palindrome(message.text)):
            bot.send_message(message.from_user.id, "Да, это палиндром")
        else:
            bot.send_message(message.from_user.id, "Нет, это не палиндром")
        palindrome = False
    if summa:
        bot.send_message(message.from_user.id, "Сумма чисел = " + str(sum_num(message.text)))
        summa = False
    match message.text:
        case 'Палиндром':
            palindrome = True
            bot.send_message(message.from_user.id, "Введи слово")
        case 'Сумма чисел':
            summa = True
            bot.send_message(message.from_user.id, "Введи числа")


bot.polling(none_stop=True, interval=0)