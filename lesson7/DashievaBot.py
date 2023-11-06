import telebot

bot = telebot.TeleBot('')

from telebot import types


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать, является ли палиндромом введеная строка")
    btn2 = types.KeyboardButton("Найти сумму чисел")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Что хотите сделать?', reply_markup=markup)

check_palindrom = False
check_sum = False

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global check_palindrom
    global check_sum

    if check_palindrom:
        if message.text == message.text[::-1]:
            bot.send_message(message.from_user.id, 'Строка является палиндромом')
        else:
            bot.send_message(message.from_user.id, 'Строка не является палиндромом')
        check_palindrom = False

    if check_sum:
        bot.send_message(message.from_user.id, 'Сумма чисел - ' + str(sum(list(map(int, message.text.split(' '))))))
        check_sum = False

    if message.text == "Узнать, является ли палиндромом введеная строка":
        check_palindrom = True
        bot.send_message(message.from_user.id, 'Введите строку для проверки на палиндром')

    if message.text == "Найти сумму чисел":
        check_sum = True
        bot.send_message(message.from_user.id, 'Введите числа перечисленные через пробел')


bot.infinity_polling()
