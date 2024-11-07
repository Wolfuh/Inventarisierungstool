import sqlite3


def login_lookup(username: str, password: str):
# Überprüfung der Anmeldedaten und gibt Erfolgsmeldung zurück

    password_hex = password                                                 # verschlüsseltes passwort
    
    my_db = sqlite3.connect('./db/users.db')     # verbindung db
    my_dbc = my_db.cursor()                     # cursor erstellen
    my_dbc.execute("""
                    SELECT * FROM users WHERE user_first_name = ? AND password = ?
                    """, (username, password_hex))
    
    res = my_dbc.fetchone()


    if res:     # überprüfung, ob passwort und benutzername übereinstimmen
        return True
        
    else:
        return False