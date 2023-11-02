import telebot
from telebot import types

bot = telebot.TeleBot('6834905940:AAFrIbfx0Lv6xcQBSgEv8qcziMTcV_F4638')

#Функция для проверки на полиндром
def check_palindrome(message):
    # transversing the string from last to first
    reversed_string = message[::-1]
    return message.lower() == reversed_string.lower()

def summarize(message):
    separeted_numbers = message.split(" ")
    return sum(separeted_numbers)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Палиндром")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Введите текст:",reply_markup=markup)
    bot.register_next_step_handler(message, get_name)
    
def get_name(message): 
    name = message.text
    if(check_palindrome(name)):
        bot.send_message(message.chat.id,"Введенное сообщение палиндром")
    else:
        bot.send_message(message.chat.id,"Введенное сообщение не палиндром")
 

bot.polling(none_stop=True, interval=0)