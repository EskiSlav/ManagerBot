#Бот-менеджер   САША    1.0 BETA
import telebot
import json
import sqlite3
import constants
from functions import *
from keyboard import *
bot = telebot.TeleBot(constants.TOKEN)    

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


['keyboard1']
@bot.message_handler(content_types=['text'])
def send_text(message):
    TEXT = user_lang(message)
    ###### keyboard1
    print(TEXT['catalog'], message.text, TEXT['catalog'].split()[0] == message.text.split()[0])
    keyboard3_buttons = TEXT['keyboard3']
    if message.text == TEXT['catalog']:
        bot.send_message(message.chat.id, TEXT['choose_category'], reply_markup=keyboard2(message))
    elif message.text == TEXT['add_channel']:
        bot.send_message(message.chat.id, 'Для того чтобы твой канал видели остальные участники, тебе необходимо добавить его в нашу базу данных. Как это сделать ты увидишь после того как нажмешь на кнопку "Как добавить канал"', reply_markup=keyboard5)
    ###### keyboard2(message)
    elif message.text.lower() in constants.themes:
        bot.send_message(message.chat.id,'Выбери какое количество подписчиков ты хочешь видеть в канале', reply_markup=keyboard3)
    ######

    elif message.text.lower() == TEXT['back'].lower():
        bot.send_message(message.chat.id, TEXT['back_answer'], reply_markup=keyboard2(message))
    elif message.text.lower() == 'вернуться в главное меню':
        bot.send_message(message.chat.id, 'Ты вернулся в главное меню', reply_markup=keyboard1(message))
    ###### keyboard3
    elif message.text.lower() == keyboard3_buttons['sub1']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == keyboard3_buttons['sub2']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == keyboard3_buttons['sub3']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == keyboard3_buttons['sub4']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == keyboard3_buttons['sub5']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == keyboard3_buttons['sub6']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == keyboard3_buttons['sub7']:
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == '100k-500k':
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    elif message.text.lower() == '500k-1kk':
        bot.send_message(message.chat.id, TEXT['here_it_is'], reply_markup=keyboard4)
    else:
        bot.send_message(message.chat.id, 'Ошибка! ' + message.text)

bot.polling()
