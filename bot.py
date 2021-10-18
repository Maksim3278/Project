import telebot
from telebot import types

TOKEN = '2094289863:AAG4p7PK5lbRcwL-LXKvwAcXkWU4eeeC7FA'
bot = telebot.TeleBot(TOKEN)

#Функция приветствия бота с пользователем:
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDG4hhbVdLXiXszV5C8BO_OujZE-EGfQAC6AQAAvPyjj-be41RjBUoYyEE') #Отправка стикера

    #плашка с клавишами
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_help = types.KeyboardButton('Помощь')
    item_start = types.KeyboardButton('Начать')

    markup.add(item_help, item_start)
