#Бот-менеджер   САША    1.0 BETA
import telebot
import json
import sqlite3
from credentials import TOKEN
from functions import *
from keyboard import *
from constants import (
    LANG_CHOOSE_STATUS,
    CHANNEL_ADD_STATUS,
    IN_MAIN_MENU_STATUS,
    CHOOSE_CATEGORY_STATUS,
    themes
)
bot = telebot.TeleBot(TOKEN)    

help_text = "Приветствую!\n Этот бот был создан для *бла-бла*."

## Отправка/прием сообщений
@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, 'Привет, я твой персональный менеджер. Ты можешь выбрать любой канал с моего каталога и купить в нем рекламу. Если тебе интересно на что я существую так сказать, то я беру 10% за услуги с сумы админа.')
    with sqlite3.connect(constants.DATABASE) as conn:
        user = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, 'EN', LANG_CHOOSE_STATUS)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id='{message.chat.id}';")
        if len(cursor.fetchall()):
            print("Such user already exists")
        else:
            cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", user)
            cursor.execute("SELECT * FROM users;")
            conn.commit()
            bot.send_message(message.chat.id, "Choose language", reply_markup=language_keyboard)


@bot.message_handler(commands=['language'])
def change_language(message):
    bot.send_message(message.chat.id, "Choose language:", reply_markup=language_keyboard)
    conn, cursor = open_connection()
    cursor.execute(f"UPDATE users SET language='None',status='{LANG_CHOOSE_STATUS}' WHERE user_id={message.chat.id};")
    conn.commit()
    conn.close()


@bot.message_handler(commands=['exit'])
def status_none(message):
    set_status_none(message)


@bot.message_handler(content_types=['text'], func=check_not_lang_choose)
def lang_choose(message):
    if message.text == "English 🇬🇧":
        execute_query(f"UPDATE users SET language='EN',status='{IN_MAIN_MENU_STATUS}' WHERE user_id={message.chat.id};")
        bot.send_message(message.chat.id, "Language is English.", reply_markup=keyboard1(message))
    elif message.text == "Русский 🇷🇺":
        execute_query(f"UPDATE users SET language='RU',status='{IN_MAIN_MENU_STATUS}' WHERE user_id={message.chat.id};")
        bot.send_message(message.chat.id, "Язык русский", reply_markup=keyboard1(message))
    else:
        bot.send_message(message.chat.id, "Please, before making requests choose one of the languages below =)")


@bot.message_handler(content_types=['text'], func=check_channel_add)
def channel_add(message):
    TEXT = user_lang(message)
    if message.forward_from_chat is None and message.text != TEXT['back']:
        bot.send_message(message.chat.id, 'Forward message from channel you want to add')
    elif message.text == TEXT['back']:
        bot.send_message(message.chat.id, TEXT['back_answer'], reply_markup=keyboard1(message))
        execute_query(f"UPDATE users SET status='{IN_MAIN_MENU_STATUS}' WHERE user_id={message.chat.id};")
    else:
        print((channel := message.forward_from_chat))
        print(type(channel), bot.get_chat(channel.id))
        if channel.type == 'channel':
            bot.send_message(message.chat.id, "Yes, this is channel")

# MAIN_MENU
@bot.message_handler(content_types=['text'], func=check_main_menu)
def main_menu_handler(message):
    TEXT = user_lang(message)
    if (text := message.text) == TEXT['catalog']:        
        bot.send_message(message.chat.id, TEXT['choose_category'], reply_markup=keyboard2(message))
    elif text == TEXT['add_channel']:
        bot.send_message(message.chat.id, TEXT['instructions'], reply_markup=keyboard5(message))
        execute_query(f"UPDATE users SET status='{CHANNEL_ADD_STATUS}' WHERE user_id={message.chat.id};")
    elif text == TEXT['back']:
        bot.send_message(message.chat.id, TEXT["back_answer"], reply_markup=keyboard1(message))
        execute_query(f"UPDATE users SET status='{IN_MAIN_MENU_STATUS}' WHERE user_id={message.chat.id};")


# @bot.message_handler(content_types=['text'], func=check_)

@bot.message_handler(content_types=['text'])
def send_text(message):
    
    # print(bot.get_chat_administrators(message.forward_from_chat.id)[0].user.id)
    TEXT = user_lang(message)
    keyboard3_buttons = TEXT['keyboard3']
    if message.text == TEXT['catalog']:
        pass
   
    ###### keyboard2(message)
    elif message.text.lower() in constants.themes:
        bot.send_message(message.chat.id, TEXT['choose_sub'], reply_markup=keyboard3(message))
    ######

    elif message.text == TEXT['back']:
        bot.send_message(message.chat.id, TEXT['back_answer'], reply_markup=keyboard2(message))
    elif message.text == TEXT['back_in_menu']:
        bot.send_message(message.chat.id, TEXT['back_in_menu_answer'], reply_markup=keyboard1(message))
    ###### keyboard3
    elif message.text == keyboard3_buttons['sub1']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    elif message.text == keyboard3_buttons['sub2']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    elif message.text == keyboard3_buttons['sub3']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    elif message.text == keyboard3_buttons['sub4']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    elif message.text == keyboard3_buttons['sub5']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    elif message.text == keyboard3_buttons['sub6']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    elif message.text == keyboard3_buttons['sub7']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4(message))
    else:
        bot.send_message(message.chat.id, 'Ошибка! ' + message.text)

bot.polling()
