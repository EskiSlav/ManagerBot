#Клавиатура
from functions import open_connection, user_lang
import telebot
import constants
import json

language_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
language_keyboard.row("Русский 🇷🇺", "English 🇬🇧")

def keyboard1(message):
    TEXT = user_lang(message)
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row(TEXT['catalog'], TEXT['add_channel'])
    return keyboard1

def keyboard2(message):
    TEXT = user_lang(message)
    BUTTONS = TEXT['keyboard2']
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
    values = list(BUTTONS.values())
    length = len(values)
    div = length % 3
    for i in range(0,length-div,3):
        keyboard2.add(values[i], values[i+1], values[i+2])
    if div == 2:
        keyboard2.add(values[length-2], values[length-1])
    elif div == 1:
        keyboard2.add(values[length-1])
    keyboard2.add(TEXT['back'], TEXT['back_in_menu'])
    return keyboard2


def keyboard3(message):
    TEXT = user_lang(message)
    BUTTONS = TEXT['keyboard3']
    keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard3.add(BUTTONS['sub1'], BUTTONS['sub2'], BUTTONS['sub3'])
    keyboard3.add(BUTTONS['sub4'], BUTTONS['sub5'], BUTTONS['sub6'])
    keyboard3.add(BUTTONS['sub7'])
    keyboard3.add(TEXT['back'], TEXT['back_in_menu'])
    return keyboard3

def keyboard4(message):
    TEXT = user_lang(message)
    keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard4.add(TEXT['keyboard4']['order'], TEXT['back'])
    keyboard4.add(TEXT['back_in_menu'])
    return keyboard4

def keyboard5(message):
    TEXT = user_lang(message)
    BUTTONS = TEXT['addkeyboard1']
    keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard5.add(BUTTONS['indicate_catalog'])
    keyboard5.add(BUTTONS['how_add_channel'], BUTTONS['how_add_bot_admin'])
    keyboard5.add(TEXT['back'])
    return keyboard5

