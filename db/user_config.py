import sqlite3



# def add_user_(name, permission):
#     my_db = sqlite3.connect('./db/users.db')     # verbindung db
#     my_dbc = my_db.cursor()                     # cursor erstellen
#     my_dbc.execute("IMPORT INTO users (user_first_name, password, permission) VALUES (?, ?, ?)", name, permission)      # nameneingabe und rolleneingabe in db übertragen
#     my_db.commit()                                                                                                      # erstellung von z.B. Admin


def delete_user(zu_loeschende_person):
    my_db = sqlite3.connect('./db/users.db')     # verbindung db
    my_dbc = my_db.cursor()                     # cursor erstellen
    my_dbc.execute("DELETE FROM users WHERE ?",(zu_loeschende_person))      # user löschen
    my_db.commit()                                                          # hohe rechte benötigt


def register_new_user(own_name, own_password):
    my_db = sqlite3.connect('./db/users.db')     # verbindung db
    my_dbc = my_db.cursor()                     # cursor erstellen
    my_dbc.execute("IMPORT INTO user (user_first_name, password) VALUES (?, ?)", own_name, own_password)    # erstellung name und passwort
    my_db.commit()                                                                                          # für neue nutzer


def correct_user(index_pos, new_name, new_permission):
    my_db = sqlite3.connect('./db/users.db')     # verbindung db
    my_dbc = my_db.cursor()                     # cursor erstellen
    my_dbc.execute(f"IMPORT INTO user (user_first_name, permission) WHERE index = {index_pos} VALUES ({new_name}, {new_permission})")   # bearbeitung existierender person
    my_db.commit()                                                                                                                      # sehr hohe rechte benötigt