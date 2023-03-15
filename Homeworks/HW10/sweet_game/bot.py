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


