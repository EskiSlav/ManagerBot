#Бот-менеджер   САША    1.0 BETA
import telebot
import json
import sqlite3
from credentials import TOKEN
from functions import *
from keyboard import *
from constants import (
    LANG_CHOOSE,
    CHANNEL_ADD,
    themes
)
bot = telebot.TeleBot(TOKEN)    

help_text = "Приветствую!\n Этот бот был создан для *бла-бла*."

## Отправка/прием сообщений
@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, 'Привет, я твой персональный менеджер. Ты можешь выбрать любой канал с моего каталога и купить в нем рекламу. Если тебе интересно на что я существую так сказать, то я беру 10% за услуги с сумы админа.')
    with sqlite3.connect(constants.DATABASE) as conn:
        user = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, 'EN','LANG_CHOOSE')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id='{message.chat.id}';")
        fetch = cursor.fetchall()
        print(fetch)
        if len(fetch):
            print("Such user already exists")
        else:
            cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", user)
            cursor.execute("SELECT * FROM users;")
            conn.commit()
            print(fetch)
            bot.send_message(message.chat.id, "Choose language", reply_markup=language_keyboard)


@bot.message_handler(commands=['language'])
def change_language(message):
    bot.send_message(message.chat.id, "Choose language:", reply_markup=language_keyboard)
    conn, cursor = open_connection()
    cursor.execute(f"UPDATE users SET language='None',status='{constants.LANG_CHOOSE}' WHERE user_id={message.chat.id};")
    conn.commit()
    conn.close()


@bot.message_handler(commands=['exit'])
def status_none(message):
    set_status_none(message)


@bot.message_handler(content_types=['text'], func=check_not_lang_choose)
def lang_choose(message):
    conn, cursor = open_connection()
    if message.text == "English 🇬🇧":
        cursor.execute(f"UPDATE users SET language='EN',status='None' WHERE user_id={message.chat.id};")
        conn.commit()
        bot.send_message(message.chat.id, "Language is English.", reply_markup=keyboard1(message))
    elif message.text == "Русский 🇷🇺":
        cursor.execute(f"UPDATE users SET language='RU',status='None' WHERE user_id={message.chat.id};")
        conn.commit()
        bot.send_message(message.chat.id, "Язык русский", reply_markup=keyboard1(message))
    else:
        bot.send_message(message.chat.id, "Plese, before makeking requests choose one of the languages below =)")
    conn.close()


@bot.message_handler(content_types=['text'], func=check_channel_add)
def channel_add(message):
    if message.forward_from_chat is None:
        bot.send_message(message.chat.id, 'Forward message from channel you want to add')
    else:
        print((channel := message.forward_from_chat))
        print(type(channel), bot.get_chat(channel.id))
        if channel.type == 'channel':
            bot.send_message(message.chat.id, "Yes, this is channel")

@bot.message_handler(content_types=['text'])
def send_text(message):
    
    # print(bot.get_chat_administrators(message.forward_from_chat.id)[0].user.id)
    TEXT = user_lang(message)
    keyboard3_buttons = TEXT['keyboard3']
    if message.text == TEXT['catalog']:
        bot.send_message(message.chat.id, TEXT['choose_category'], reply_markup=keyboard2(message))
    elif message.text == TEXT['add_channel']:
        bot.send_message(message.chat.id, 'Для того чтобы твой канал видели остальные участники, тебе необходимо добавить его в нашу базу данных. Как это сделать ты увидишь после того как нажмешь на кнопку "Как добавить канал"', reply_markup=keyboard5(message))
        conn, cursor = open_connection()
        cursor.execute(f"UPDATE users SET status='{CHANNEL_ADD}' WHERE user_id={message.chat.id};")
        conn.commit()
        conn.close()
    ###### keyboard2(message)
    elif message.text.lower() in constants.themes:
        bot.send_message(message.chat.id,'Выбери какое количество подписчиков ты хочешь видеть в канале', reply_markup=keyboard3(message))
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
