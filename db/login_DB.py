# import sqlite3
# from argon2 import PasswordHasher

# ph = PasswordHasher()

# def login_lookup(username: str, password: str):
    # Überprüfung der Anmeldedaten, gibt Erfolgsmeldung zurück
    # users_db = sqlite3.connect('./db/users.db') # Verbindung DB
    # users_dbc = users_db.cursor()               # Cursor erstellen
    # users_dbc.execute(f"SELECT password_hash FROM users WHERE user_first_name = '{username}'") # Hash des Passwortes des eingebenen Nutzers abfragen
    # password_hash = users_dbc.fetchone()

    # try:
        # ph.verify(password_hash[0], password)   # Überprüfung, ob Passwort und Benutzername übereinstimmen
        # return True
    # except:
        # return False