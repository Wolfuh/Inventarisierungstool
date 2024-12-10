import sqlite3
import os
import hashlib

username_global = "Benutzername Ungültig"

def init_connection():      # verbindung mit DB erstellen und Variable der Verbindung geben
    path:str = os.path.join(os.path.dirname(__file__), 'Inventarisierungs_DB.sqlite3')    # DB weg, der mit VS Code und PyCharm erreichbar ist
    my_db = sqlite3.connect(path)
    return my_db


def fetch_items():  # Gibt die items aus der items DB zurück
    try:
        my_db = init_connection()
        cur = my_db.cursor()       # cur für cursor, welcher SQLite funktionen ausführen kann
        cur.execute("SELECT * FROM items")
        items_rows = cur.fetchall()      
        return items_rows
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()   # egal was passiert, die DB wird Geschlossen


def fetch_items_headers():  # Gibt die Überschriften der items DB zurück, ohne die Anzahl zu kennen
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("PRAGMA table_info(items)") # sucht die Überschriften
        it_alles = cur.fetchall()
        entfernungs_liste = ["product_id", "added_by_user"]     # blendet die Übeschriften aus (nur hier veränderbar)
        items_uberschrift = [i[1] for i in it_alles if i[1].lower() not in entfernungs_liste]   
        # überprüft, ob weitere Überschriften da sind und wenn ja, dann wird diese kleingeschrieben zurück gegeben

        return items_uberschrift
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()


def fetch_users():  # Gibt die Benutzertabelle wieder
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


def fetch_users_headers():  # Gibt die Überschriften der Benutzertabelle wieder
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


def login_lookup(username: str, password: str): # überprüfung eingehendes Passwort und Benutzername    
    try:
        global username_global    # Variable soll außerhalb der Definition nutzbar sein
        my_db = init_connection() # Verbindung DB
        cur = my_db.cursor()      # Cursor erstellen
        cur.execute(f"SELECT passwort FROM benutzer WHERE Benutzername = '{username}'")         
        back_password = cur.fetchone()
        # gibt das Passwort des eingegebenen Benutzers wieder (bereits gehashed), falls dieser Existiert

        username_global = username  # Globaler Benutzername auf die Benutzername Eingabe Gesetzt
        hash_password = hashlib.sha512(password.encode()).hexdigest() # Das eingegebene Passwort hashen
        if hash_password == back_password[0]: # überprüfung ob das gehashte passwort von der Eingabe, mit dem aus der DB übereinstimmt 
            return True
        else:
            username_global = ""  # Globalen Benutzernamen leeren
    except:
        username_global = ""
        return False
    finally:
        if my_db:
            my_db.close()





def lookup_user_stuff(): # Gibt die Nutzerinformationen
    try:    # Nutzt den Globalen Benutzername um an Informationen zu gelangen
        my_db = init_connection() # Verbindung DB
        cur = my_db.cursor()      # Cursor erstellen
        cur.execute(f"SELECT Rolle FROM benutzer WHERE Benutzername = '{username_global}'") 
        role = cur.fetchone()
        cur.execute(f"SELECT Vorname FROM benutzer WHERE Benutzername = '{username_global}'") 
        first_name = cur.fetchone()
        cur.execute(f"SELECT Nachname FROM benutzer WHERE Benutzername = '{username_global}'") 
        last_name = cur.fetchone()
        cur.execute(f"SELECT Klasse FROM benutzer WHERE Benutzername = '{username_global}'") 
        class_name = cur.fetchone()
        my_db.close()    
        return role, first_name, last_name, class_name
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)















##############################
## UNBENUTZTE DEFINITIONEN: ##
##############################


def search_bar_update(search): # Aktualisiert die Sucheingabe für die items Tabelle - muss noch eingefügt werden
    try:
        my_db = init_connection()
        cur = my_db.cursor()

        cur.execute(f"PRAGMA table_info(items)")
        columns = [row[1] for row in cur.fetchall()]  # Spaltennamen wiedergeben

        if not columns:
            return "Die Tabelle hat keine Spalten oder existiert nicht."

        # durchsucht alles aus der items Tabelle und gibt die komplette Zeile zurück
        where_clause = " OR ".join([f"{col} LIKE ?" for col in columns])
        query = f"SELECT * FROM items WHERE {where_clause}"
        cur.execute(query, [f"%{search}%"] * len(columns))
        answer_search = cur.fetchall()
        return answer_search
    except:
        return


def add_user(new_username, new_first_name, new_last_name, new_class, new_role):
    # fügt neuen Benutzer hinzu, benötigt 5 eingaben und überprüft diese
    try:
        new_username = new_username.replace(" ", "")
        new_first_name = new_first_name.replace(" ", "")
        new_last_name = new_last_name.replace(" ", "")
        new_class = new_class.replace(" ", "")
        new_role = new_role.replace(" ", "")
        my_db = init_connection()
        cur = my_db.cursor()

        hash_password = hashlib.sha512("Startnow!".encode()).hexdigest() # StartNow! als Standartpasswort festgelegt

        cur.execute("INSERT INTO benutzer (Benutzername, Vorname, Nachname, Klasse, Passwort, Rolle) VALUES (?,?,?,?,?,?)", 
                                (new_username, new_first_name, new_last_name, new_class, hash_password, new_role))
        my_db.commit() # führt die funktion aus
         
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)
    finally:
        if my_db:
            my_db.close()  


#############################
### BIS HIER HIN BEHALTEN ###
#############################







############### DEBUG STUFF ###############
# login_lookup("Mathis","123456")
# lookup_role()
# print(username_global)
# sibllllll = search_bar_update("et")
# print(sibllllll)
# ha=add_user("peter", "Peter", "Pan", "FI99", "viewer")
# print(ha)
############### ENDE DEBUG ################









#################################
# def delete_username_global(): #
#     global username_global    #   eventuell später einfügen
#     username_global = ""      #
#################################







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


