import sqlite3
import functions
import constants
import json
# conn = sqlite3.connect("data/database.db")
# cursor = conn.cursor()
us_id = "111111"
# cursor.execute(f"SELECT * FROM users WHERE user_id={us_id};")
# cursor.execute("DELETE FROM users WHERE username='yardvlad'")

# cursor.execute("SELECT * FROM users;")
# fetch = cursor.fetchall()
# if len(fetch) == 0:
#     print("yes")
# else:
#     print(fetch)
# conn.commit()
# conn.close()

# TEXT = {}
# var = 394773843
# conn, cursor = functions.open_connection()
# cursor.execute(f"UPDATE users SET status='EN' WHERE user_id={var};")
# print(cursor.fetchall())
# conn.close()


# conn, curr = functions.open_connection()
# curr.execute(f"SELECT status FROM users WHERE user_id='394773843'")
# lang = curr.fetchall()[0][0]
# conn.close()
# if "ru" == "EN":
#     with open(constants.EN, 'r') as en:
#         TEXT = json.load(en)
# elif "RU" == "RU":
#     with open(constants.RU, 'r') as ru:
#         TEXT = json.load(ru)

# print(TEXT['keyboard1'])
# import json

# with open("data/RU.json", 'r') as enjson:
#     data = json.load(enjson)
#     print(data)


# data = {"Hello": "World",
#         "key1": {"subkey1": "subvalue1"}
#         }

# with open ("data/EX.json", "w") as exjson:
#     json.dump(data,exjson)

# lst = [1,2,3,4,5]
# div = 2
# print(lst[len(lst)-1])


conn, curr = functions.open_connection()
curr.execute("""
CREATE TABLE IF NOT EXISTS "channels" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT NOT NULL,
	"owner"	TEXT NOT NULL,
	"user_id"	INTEGER,
	"username"	TEXT,
	"subscribers"	NUMERIC NOT NULL,
	"date"	TEXT NOT NULL,
	"image"	INTEGER,
	FOREIGN KEY("user_id") REFERENCES "users"("user_id")
);""")

curr.execute("""
CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	TEXT NOT NULL UNIQUE,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"username"	TEXT,
	"language"	TEXT DEFAULT 'EN',
	"status"	TEXT DEFAULT 'LANG_CHOOSE',
	PRIMARY KEY("user_id")
);""")

functions.execute_query("""INSERT INTO "users" VALUES ('394773843','EskiSlav',NULL,'EskiSlav','RU','IN_MAIN_MENU');""")
functions.execute_query("""INSERT INTO "users" VALUES ('364983751','LEON',NULL,'yardvlad','RU','None');""")
functions.execute_query("""INSERT INTO "users" VALUES ('781965757','Вячеслав',NULL,'eskislav2','EN','None');""")
conn.commit()

conn.close()


