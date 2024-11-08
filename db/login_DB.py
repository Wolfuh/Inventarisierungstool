import sqlite3
from argon2 import PasswordHasher

ph = PasswordHasher()
def login_lookup(username: str, password: str):
# Überprüfung der Anmeldedaten und gibt Erfolgsmeldung zurück

    my_db = sqlite3.connect('./db/users.db')    # Verbindung DB
    my_dbc = my_db.cursor()                     # Cursor erstellen
    my_dbc.execute("SELECT password_hash FROM users WHERE user_first_name = '" + username + "'") # Hash des Passwortes des eingebenen Nutzers abfragen
    password_hash = my_dbc.fetchone()

    try:
        ph.verify(password_hash[0], password)     # Überprüfung, ob Passwort und Benutzername übereinstimmen
        return True
    except:
        return False