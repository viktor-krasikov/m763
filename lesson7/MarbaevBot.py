import telebot
from telebot import types

bot = telebot.TeleBot('6711986876:AAExxaa_9itzltEoMq_87KrHljAAPx3lhW0')

def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)

def num_sum(text):
    text = text.lower().replace(' ', '')
    if text.isnumeric:
        text = [int(i) for i in list(text)]
        return sum(text)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить на палиндром")
    btn2 = types.KeyboardButton('Сумма цифр')
    markup.add(btn1,btn2)
    bot.send_message(message.from_user.id, "👋 Привет! Что хочешь сделать?", reply_markup=markup)

palindrome = False
summa = False

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global palindrome
    global summa
    if palindrome == True:

        if (is_palindrome(message.text.lower().replace(' ',''))):
            bot.send_message(message.from_user.id, "Да, это палиндром")
        else:
            bot.send_message(message.from_user.id, "Нет, это не палиндром")
        palindrome = False

    if summa == True:
        bot.send_message(message.from_user.id, "Сумма цифр = " + str(num_sum(message.text)))
        summa = False

    if message.text == 'Проверить на палиндром':
        palindrome = True
        bot.send_message(message.from_user.id, "Введи слово")

    if message.text == 'Сумма цифр':
        summa = True
        bot.send_message(message.from_user.id, "Введите число")




bot.infinity_polling()