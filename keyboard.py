#Клавиатура
from functions import open_connection, user_lang
import telebot
import constants
import json

language_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
language_keyboard.row("RU", "EN")

def keyboard1(message):
    TEXT = user_lang(message)['keyboard1']
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row(TEXT['catalog'], TEXT['add_channel'])
    return keyboard1

def keyboard2(message):
    TEXT = user_lang(message)['keyboard2']
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
    print(TEXT)
    values = list(TEXT['buttons'].values())
    length = len(values)
    div = length % 3
    for i in range(0,length-div,3):
        keyboard2.add(values[i], values[i+1], values[i+2])
    if div == 2:
        keyboard2.add(values[length-2], values[length-1])
    elif div == 1:
        keyboard2.add(values[length-1])
    keyboard2.add(TEXT['back_buttons']['back'], TEXT['back_buttons']['back_on_main_menu'])
    return keyboard2

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.add('1-500 под', '500-1k', '1k-5k', '5k-10k', '10k-20k',  '20k-50k','50k-100k','100k-500k','500k-1kk')
keyboard3.add('Назад', 'Вернуться в главное меню')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.add('Назад','Заказать')
keyboard4.add('Вернуться в главное меню')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.add('Назад','Как добавить бота')

keyboard10 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard10.add('Сhannel categories', 'Add channel')