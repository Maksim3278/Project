import telebot
from telebot import types


TOKEN = '2094289863:AAG4p7PK5lbRcwL-LXKvwAcXkWU4eeeC7FA'
bot = telebot.TeleBot(TOKEN)


# Функция приветствия бота с пользователем:
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKGiV_bsL7G074Rky91YM5ChZkX3NfXAAIDAQACmY-lB2o_oywPbNSHHgQ')

    # плашка с клавишами
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_help = types.KeyboardButton('Помощь')
    item_start = types.KeyboardButton('Начать')

    markup.add(item_help, item_start)

    bot.send_message(message.chat.id,
                     'Приветствую тебя, {0.first_name}!\n Я - финансовый бот,'
                     'который поможет тебе проанализировать твои доходы/расходы.'.format(
                         message.form_user),
                     parse_mode='html', reply_markup=markup)
