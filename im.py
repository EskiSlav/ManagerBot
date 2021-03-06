#Бот-менеджер   САША    1.0 BETA
import telebot
import json
import sqlite3
import constants
from keyboard import *
bot = telebot.TeleBot(constants.TOKEN)        
TEXT = {}




help_text = "Приветствую!\n Этот бот был создан для *бла-бла*."

##keyboards
##@bot.message_handler(content_types=['text'])
##def keyboard(message):
  ##  keyboard1()



## Отправка/прием сообщений
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я твой персональный менеджер. Ты можешь выбрать любой канал с моего каталога и купить в нем рекламу. Если тебе интересно на что я существую так сказать, то я беру 10% за услуги с сумы админа.', reply_markup=keyboard1)
    with sqlite3.connect(constants.DATABASE) as conn:
        user = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, 'EN','LANG_CHOOSE')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id='{message.chat.id}';")
        if len(cursor.fetchall()):
            print("Such user already exists")
        else:
            cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", user)
            cursor.execute("SELECT * FROM users;")
            conn.commit()
            print(cursor.fetchall())
            bot.send_message(message.chat.id, "Choose language", reply_markup=language_keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    ###### keyboard1
    if message.text.lower()  ==  'категории каналов':
        bot.send_message(message.chat.id, 'Выбери категорию канала', reply_markup=keyboard2)
    elif message.text.lower()   ==    'добавить канал':
        bot.send_message(message.chat.id, 'Для того чтобы твой канал видели остальные участники, тебе необходимо добавить его в нашу базу данных. Как это сделать ты увидишь после того как нажмешь на кнопку "Как добавить канал"', reply_markup=keyboard5)
    ###### keyboard2
    elif message.text.lower() in constants.themes:
        bot.send_message(message.chat.id,'Выбери какое количество подписчиков ты хочешь видеть в канале', reply_markup=keyboard3)
    ######

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Ты вернулся назад', reply_markup=keyboard2)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Ты вернулся назад', reply_markup=keyboard1)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Ты вернулся назад', reply_markup=keyboard3)
    elif message.text.lower() == 'вернуться в главное меню':
        bot.send_message(message.chat.id, 'Ты вернулся в главное меню', reply_markup=keyboard1)


    ###### keyboard3
    elif message.text.lower() == '1-500 под':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '500-1k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '1k-5k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '5k-10k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '10k-20k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '20k-50k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '50k-100k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '100k-500k':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    elif message.text.lower() == '500k-1kk':
        bot.send_message(message.chat.id, 'Вот каналы с таким количеством подписчиков', reply_markup=keyboard4)
    else:
        bot.send_message(message.chat.id, 'Ошибка!', reply_markup=keyboard1)

bot.polling()
