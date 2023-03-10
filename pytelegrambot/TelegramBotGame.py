
import telebot 
from telebot import types
import random

token = '6034619025:AAELuxZJeoc6bvhi_atkpv7YooB6ac8aMXk'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton("Играть")
button2 = types.KeyboardButton("нет")
keyboard.add(button1,button2)

@bot.message_handler(commands=['start','game'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(message2, check_answer)


def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ок тогда вот правила: нужно угадать число от 1 до 10 за 3 попытки')
        number = random.choice(range(1,11))
        game(message, 3, number)
    else: 
        bot.send_message(message.chat.id, "Хорошо, пока!")
        

def game(message,attempts, number):
    message2 = bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message2, check_number, attempts-1, number)



def check_number(message,attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Поздравляю, ты выиграл!!')
        start_message(message)
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Сорри, у тебя закончились попытки')
        start_message(message)
    else:
        bot.send_message(message.chat.id, f'Не верно, у тебя остаось {attempts} попыток, попробуй еще раз ввести число')
        game(message, attempts, number)


bot.polling()
