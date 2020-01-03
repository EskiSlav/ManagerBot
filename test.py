import sqlite3
conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()
us_id = "111111"
# cursor.execute(f"SELECT * FROM users WHERE user_id={us_id};")
# cursor.execute("DELETE FROM users WHERE username='yardvlad'")

cursor.execute("SELECT * FROM users;")
fetch = cursor.fetchall()
if len(fetch) == 0:
    print("yes")
else:
    print(fetch)
conn.commit()
conn.close()



# import json

# with open("data/RU.json", 'r') as enjson:
#     data = json.load(enjson)
#     print(data)


# data = {"Hello": "World",
#         "key1": {"subkey1": "subvalue1"}
#         }

# with open ("data/EX.json", "w") as exjson:
#     json.dump(data,exjson)