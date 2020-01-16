import constants
import sqlite3
import json

def check_not_lang_choose(message):
    with sqlite3.connect(constants.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id={message.chat.id} and status='{constants.LANG_CHOOSE}'")
        if len(cursor.fetchall()) == 1:
            return True
        elif len(cursor.fetchall()) == 0: 
            return False
        else:
            print('wtf?')
            return False


def open_connection():
    with sqlite3.connect(constants.DATABASE) as conn:
        return (conn, conn.cursor())


def check_channel_add(message):
    conn, cursor = open_connection()    
    cursor.execute(f"SELECT * from users WHERE user_id={message.chat.id} and status='{constants.CHANNEL_ADD}'")
    res = len(cursor.fetchall()) > 0
    conn.close()
    return res


def user_lang(message):
    conn, curr = open_connection()
    curr.execute(f"SELECT language FROM users WHERE user_id={message.chat.id}")
    lang = curr.fetchall()[0][0]
    print('lang: ', lang)
    conn.close()
    if lang == "EN":
        with open(constants.EN) as en:
            return json.load(en)
    elif lang == "RU":
        with open(constants.RU) as ru:
            return json.load(ru)


def set_status_none(message):
    conn, cursor = open_connection()
    cursor.execute(f"UPDATE users SET status='None' WHERE user_id={message.chat.id}")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    print(check_channel_add(394773843))