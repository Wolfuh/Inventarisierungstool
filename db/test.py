# from SQLite_db import *
# item_update_damage(8,"DMG","test","description")

import hashlib



password = input("was willst du Hashen? - ")
hash_password = hashlib.sha512(password.encode()).hexdigest()
print(hash_password)

# 🐧🐧🐧🐧🐧🐧