from SQLite_db import *
#item_update_damage("lil", "Lul",8,"DMG","test","description")
conn = init_connection()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='history';")
print(cursor.fetchone())



# import hashlib

# password = input("was willst du Hashen? - ")
# hash_password = hashlib.sha512(password.encode()).hexdigest()
# print(hash_password)

# # 🐧🐧🐧🐧🐧🐧