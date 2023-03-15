import telebot
from telebot import types
import random


bot = telebot.TeleBot("5903419564:AAEQEnawCtrDpprHbJ9M-IG-kpbSiT4X2l0")

sweets = 221
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ""

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, "Приветствую вас в игре!")
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    flag = random.choice(["user", "bot"])
    if flag == "user":
        bot.send_message(message.chat.id, "Первый ваш ход.")
        controller(message)
    else:
        bot.send_message(message.chat.id, "Первый мой ход.")
        controller(message)


def controller(message):
    global flag
    if sweets>0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход: введите количество конфет от 0 до {max_sweet}.")
            bot.register_next_step_handler(message,user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")


def bot_input(message):
    global sweets,bot_turn,flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"Бот взял {bot_turn} конфет.")
    bot.send_message(message.chat.id, f"Осталось {sweets} конфет.")
    flag = "user" if flag == "bot" else "bot"
    controller(message)


