from constants import (
    DATABASE,
    EN, RU,
    IN_MAIN_MENU_STATUS,
    CHANNEL_ADD_STATUS,
    LANG_CHOOSE_STATUS
)
import sqlite3
import json

def check_not_lang_choose(message):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id={message.chat.id} and status='{LANG_CHOOSE_STATUS}'")
        if len(cursor.fetchall()):
            return True
        return False


def open_connection():
    with sqlite3.connect(DATABASE) as conn:
        return (conn, conn.cursor())


def check_channel_add(message):
    conn, cursor = open_connection()    
    cursor.execute(f"SELECT * from users WHERE user_id={message.chat.id} and status='{CHANNEL_ADD_STATUS}'")
    res = len(cursor.fetchall()) > 0
    conn.close()
    return res

def check_main_menu(message):
    conn, cursor = open_connection()
    cursor.execute(f'SELECT status FROM users WHERE user_id={message.chat.id}')
    status = cursor.fetchall()[0][0]
    conn.close()
    if status == IN_MAIN_MENU_STATUS:
        return True

def user_lang(message):
    conn, curr = open_connection()
    curr.execute(f"SELECT language FROM users WHERE user_id={message.chat.id}")
    lang = curr.fetchall()[0][0]
    print(f'{lang=}')
    conn.close()
    if lang == "EN":
        with open(EN) as en:
            return json.load(en)
    elif lang == "RU":
        with open(RU) as ru:
            return json.load(ru)


def set_status_none(message):
    conn, cursor = open_connection()
    cursor.execute(f"UPDATE users SET status='None' WHERE user_id={message.chat.id}")
    conn.commit()
    conn.close()

def execute_query(query):
    conn, cursor = open_connection()
    cursor.execute(query)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print(check_channel_add(394773843))