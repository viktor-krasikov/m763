import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)

s = ''
num = ''


@bot.message_handler(commands=['start'])
def startBot(message):
    first_mess = "Что будем делать?"
    global markup
    markup = types.InlineKeyboardMarkup()
    button_pal = types.InlineKeyboardButton(text='Палиндром', callback_data='pal')
    button_sum = types.InlineKeyboardButton(text='Сумма двух чисел', callback_data='sum')
    markup.add(button_pal, button_sum)
    bot.send_message(message.chat.id, first_mess, reply_markup=markup)


def pal(message):
    s = message.text.lower()
    if s[::-1] == s:
        bot.send_message(message.chat.id, 'Да, палиндром',reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Нет, "' + s + '" не палиндром',reply_markup=markup)


def summa(message):
    num = message.text
    ssum = sum(map(float, num.split()))
    bot.send_message(message.chat.id, "Сумма чисел = " + str(ssum),reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(call):
    if call.data == "pal":
        bot.send_message(call.message.chat.id, 'Введи слово')
        bot.register_next_step_handler(call.message, pal)
    elif call.data == "sum":
        bot.send_message(call.message.chat.id, 'Введи числа')
        bot.register_next_step_handler(call.message, summa)


# def palindrome():
#     @bot.message_handler(content_types=['text'])
#     def pal(message):
#         s = message.text.lower()
#         if s[::-1] == s:
#             bot.send_message(message.chat.id, 'Да, палиндром')
#         else:
#             bot.send_message(message.chat.id, 'Нет, "' + s + '" не палиндром')
#         return
#
# def summa_chisel():
#     @bot.message_handler(content_types=['text'])
#     def summa(message):
#         num = message.text
#         ssum = sum(map(float, num.split()))
#         bot.send_message(message.chat.id, "Сумма чисел = " + str(ssum))
#         return


bot.infinity_polling()
