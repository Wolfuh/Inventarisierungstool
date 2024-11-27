import sqlite3
import os
import hashlib





def init_connection():
    """
    Hilfsfunktion zur Herstellung einer Verbindung mit der SQLite-Datenbank.
    - Die Datenbankdatei muss unter dem angegebenen Pfad existieren.
    - row_factory wird auf sqlite3.Row gesetzt, um die Ergebnisse als Dictionaries zurückzugeben.
    """
    path:str = os.path.join(os.path.dirname(__file__), 'Inventarisierungs_DB.sqlite3')      #+'./db/Inventarisierungs_DB.sqlite3'
    my_db = sqlite3.connect(path)
    # Wichtig ist das hier der Root-Pfad angegeben wirddaadvjrnjrmgkmvkmvlddmvlmvk,vfg fifmvlf ,gr,or,vorr,ogl

    my_db.row_factory = sqlite3.Row  # Rückgabe von Zeilen als Dictionary
    return my_db

def fetch_items():
    """
    - Gibt eine Liste von items zurück
    - Gibt Spaltenname zu allem mit
    """
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("SELECT * FROM items")
        items_rows = cur.fetchall()      
        return items_rows
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()

def fetch_items_headers():
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("PRAGMA table_info(items)")
        it_alles = cur.fetchall()
        entfernungs_liste = ["product_id", "added_by_user"]     # blendet die übeschriften aus
        items_uberschrift = [i[1] for i in it_alles if i[1].lower() not in entfernungs_liste]
        return items_uberschrift
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()

def fetch_users():
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("SELECT * FROM benutzer")
        users_row = cur.fetchall()
        return users_row
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der User-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()

def fetch_users_headers():
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("PRAGMA table_info(benutzer)")
        us_all = cur.fetchall()
        users_uberschrift = [i[1] for i in us_all]       
        return users_uberschrift
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der User-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()

def login_lookup(username: str, password: str):
    
    users_db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'Inventarisierungs_DB.sqlite3')) # Verbindung DB
    users_dbc = users_db.cursor()               # Cursor erstellen
    users_dbc.execute(f"SELECT passwort FROM benutzer WHERE Benutzername = '{username}'") # Hash des Passwortes des eingebenen Nutzers abfragen
    back_password = users_dbc.fetchone()
    # print(password)
    hash_password = hashlib.sha512(password.encode()).hexdigest()
    
    users_db.close()
    try:
        return hash_password == back_password[0]
        # print(hash_password)
        # print(back_password[0])
    except:
        return False


# login_lookup("Hans","123456")

#############################
### BIS HIER HIN BEHALTEN ###
#############################






























# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

# from db.SQLite_db import *






# root = tk.Tk()
# root.title("miau")
# root.geometry("600x400")
# tree = ttk.Treeview(root, show="headings", height=15)
# tree.pack(expand=True, fill="both")

# ##################### Einfügen: Profiles -> 185 - 198 (Diese Datei importieren)
# # AB HIER EINBINDEN #



# # Spaltennamen aus der Datenbank holen
# users_uberschrift = fetch_users_headers()

# # Überschriften konfigurieren
# tree["columns"] = users_uberschrift
# for up in users_uberschrift:
#     tree.column(up, anchor='center', width=100)
#     tree.heading(up, text=up)

# users_data = fetch_users()

# # Daten aus DB einfügen

# for i,row in enumerate(users_data):
#     us_formatted_row = [value if value is not None else "-" for value in row] # Leere Felder durch "-" ersetzen
#     color = "#f3f3f3" if i % 2 == 0 else "white"
#     tree.insert("", "end", values=us_formatted_row, tags=("even" if i % 2 == 0 else "odd"))



# # BIS HIER #
# ############

# root.mainloop()












# root = tk.Tk()
# root.title("FOLKSWAGEN")
# root.geometry("600x400")
# tree = ttk.Treeview(root, show="headings", height=15)
# tree.pack(expand=True, fill="both")

# ##################### Einfügen: Overview -> 236 - 250 (Diese Datei importieren)
# # AB HIER EINBINDEN #



# # Spaltennamen aus der Datenbank holen
# items_uberschrift = fetch_items_headers()

# # Überschriften konfigurieren
# tree["columns"] = items_uberschrift
# for up in items_uberschrift:
#     tree.column(up, anchor=CENTER, width=100)
#     tree.heading(up, text=up)

# items_data = fetch_items()

# # Daten aus DB einfügen

# for i,row in enumerate(items_data):
#     formatted_row = [value if value is not None else "-" for value in row] # Leere Felder durch "-" ersetzen
#     color = "#f3f3f3" if i % 2 == 0 else "white"
#     tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))



# # BIS HIER #
# ############

# root.mainloop()


