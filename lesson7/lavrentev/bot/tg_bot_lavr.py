import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def startBot(message):
    print(message.from_user.username, ': ', message.text)
    first_mess = "Что будем делать?"
    global markup
    markup = types.InlineKeyboardMarkup()
    button_pal = types.InlineKeyboardButton(text='Палиндром', callback_data='pal')
    button_sum = types.InlineKeyboardButton(text='Сумма чисел', callback_data='sum')
    markup.add(button_pal, button_sum)
    bot.send_message(message.chat.id, first_mess, reply_markup=markup)


def pal(message):
    print(message.from_user.username, ': ', message.text)
    s = message.text.lower()
    if s[::-1] == s:
        bot.send_message(message.chat.id, 'Да, "' + s + '" палиндром \nЧто дальше?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Нет, "' + s + '" не палиндром \nЧто дальше?', reply_markup=markup)


def summa(message):
    print(message.from_user.username, ': ', message.text)
    num = message.text
    ssum = sum(map(float, num.split()))
    bot.send_message(message.chat.id, "Сумма чисел = " + str(ssum) + "\nЧто дальше?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(call):
    print(call.message.from_user.username, ': ', call.message.text)
    print(call.data)
    if call.data == "pal":
        bot.send_message(call.message.chat.id, 'Отправь слово, которое хочешь проверить на полиндром')
        bot.register_next_step_handler(call.message, pal)
    elif call.data == "sum":
        bot.send_message(call.message.chat.id, 'Введи числа через пробел')
        bot.register_next_step_handler(call.message, summa)


bot.infinity_polling()
