import constants
import sqlite3

def check_lang_choose(m):
    with sqlite3.connect(constants.DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id={m.chat.id} and status='{constants.LANG_CHOOSE}'")
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