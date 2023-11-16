import telebot

bot = telebot.TeleBot('6721083425:AAF5KAQLGlGTowvyPb_2eqyB1YGRnTVP0Qk')

from telebot import types

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("-")
    btn2 = types.KeyboardButton("U")
    btn3 = types.KeyboardButton("-")
    btn4 = types.KeyboardButton("L")
    btn5 = types.KeyboardButton("D")
    btn6 = types.KeyboardButton("R")


    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    bot.send_message(message.from_user.id, 'Нажмите на любую кнопку, чтобы запустить змейку', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global check_palindrom
    global check_sum

    if message.text == 'U':
        file = open("data.txt", "w")
        file.write('U')
        file.close()

    if message.text == 'L':
        file = open("data.txt", "w")
        file.write('L')
        file.close()

    if message.text == 'D':
        file = open("data.txt", "w")
        file.write('D')
        file.close()

    if message.text == 'R':
        file = open("data.txt", "w")
        file.write('R')
        file.close()


bot.infinity_polling()
