import sqlite3
import os
import hashlib
import re

username_global = "Benutzername Ungültig"
item_ID_set = ""

def init_connection():      # verbindung mit DB erstellen und Variable der Verbindung geben
    path:str = os.path.join(os.path.dirname(__file__), 'Inventarisierungs_DB.sqlite3')    # DB weg, der mit VS Code und PyCharm erreichbar ist
    my_db = sqlite3.connect(path)
    return my_db


def login_lookup(username: str, password: str): # überprüfung eingehendes Passwort und Benutzername    
    try:
        global username_global    # Variable soll außerhalb der Definition nutzbar sein (Speicherung des Benutzernamen)
        my_db = init_connection() # Verbindung DB
        cur = my_db.cursor()      # Cursor erstellen
        cur.execute(f"SELECT passwort FROM benutzer WHERE Benutzername = '{username}'")         
        back_password = cur.fetchone()
        # gibt das Passwort des eingegebenen Benutzers wieder (bereits gehashed), falls dieser Existiert

        username_global = username  # Globaler Benutzername auf die Benutzername Eingabe Gesetzt
        hash_password = hashlib.sha512(password.encode()).hexdigest() # Das eingegebene Passwort hashen
        start_password = hashlib.sha512("StartNow!".encode()).hexdigest() # StartNow! (Standartpasswort)
        if hash_password == back_password[0]: # überprüfung ob das gehashte passwort von der Eingabe, mit dem aus der DB übereinstimmt
            if hash_password == start_password: 
                return "change_password" # Wenn das Passwort das Standartpasswort ist, wird der Benutzer aufgefordert, es zu ändern
            else:
                return "keep_going"
        else:
            username_global = ""  # Globalen Benutzernamen leeren
    except:
        username_global = ""
        return False
    finally:
        if my_db:
            my_db.close()

def ist_passwort_stark(passwort):
    """Prüft, ob das Passwort stark genug ist."""
    if len(passwort) < 8:
        return False, "Das Passwort muss mindestens 8 Zeichen lang sein."
    if not re.search(r'[A-Z]', passwort):
        return False, "Das Passwort muss mindestens einen Großbuchstaben enthalten."
    if not re.search(r'[a-z]', passwort):
        return False, "Das Passwort muss mindestens einen Kleinbuchstaben enthalten."
    if not re.search(r'\d', passwort):
        return False, "Das Passwort muss mindestens eine Zahl enthalten."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', passwort):
        return False, "Das Passwort muss mindestens ein Sonderzeichen enthalten."
    return True, "Passwort erfolgreich geändert! Melden Sie sich erneut an."

def save_only_password(password):
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        hash_password = hashlib.sha512(password.encode()).hexdigest()
        print(username_global)
        cur.execute(f"UPDATE benutzer SET Passwort = '{hash_password}' WHERE Benutzername = '{username_global}'")
        my_db.commit()
        pass
    except:
        pass
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
        cur.execute(f"SELECT Email FROM benutzer WHERE Benutzername = '{username_global}'")
        email = cur.fetchone()
        my_db.close()    
        return role, first_name, last_name, class_name, email, username_global
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)


def search_bar_update(table, excluded_columns, search): # Aktualisiert die Sucheingabe für die items Tabelle - muss noch eingefügt werden
    try:
        my_db = init_connection()
        cur = my_db.cursor()

        cur.execute(f"PRAGMA table_info({table})")  # Spaltennamen der Tabelle wiedergeben
        uberschriften = cur.fetchall()
        columns = [row[1] for row in uberschriften if row[1] not in excluded_columns]  # Spaltennamen wiedergeben
        column_names = ", ".join(columns)  # Erzeugt eine durch Kommas getrennte Liste der Spaltennamen

        # durchsucht alles aus der items Tabelle und gibt die komplette Zeile zurück
        where_clause = " OR ".join([f"{col} LIKE ?" for col in columns])
        query = f"SELECT {column_names} FROM {table} WHERE {where_clause}"
        cur.execute(query, [f"%{search}%"] * len(columns))
        answer_search = cur.fetchall()
        return answer_search
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)


def add_user(new_username, new_first_name, new_last_name, new_class, new_role, email):
    # fügt neuen Benutzer hinzu, benötigt 5 eingaben und überprüft diese
    try:
        new_username = new_username.replace(" ", "")
        new_first_name = new_first_name.replace(" ", "")
        new_last_name = new_last_name.replace(" ", "")
        new_class = new_class.replace(" ", "")
        new_role = new_role.replace(" ", "")
        my_db = init_connection()
        cur = my_db.cursor()

        hash_password = hashlib.sha512("StartNow!".encode()).hexdigest() # StartNow! als Standartpasswort festgelegt

        cur.execute("INSERT INTO benutzer (Benutzername, Vorname, Nachname, Klasse, Passwort, Rolle, Email) VALUES (?,?,?,?,?,?,?)", 
                                (new_username, new_first_name, new_last_name, new_class, hash_password, new_role, email))
        my_db.commit() # führt die funktion aus
         
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)
    finally:
        if my_db:
            my_db.close()  

def fetch_headers(table_name, excluded_columns):  # Gibt die Überschriften der items DB zurück, ohne die Anzahl zu kennen
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute(f"PRAGMA table_info({table_name})") # sucht die Überschriften
        it_alles = cur.fetchall()
        items_uberschrift = [i[1] for i in it_alles if i[1] not in excluded_columns]   
        # überprüft, ob weitere Überschriften da sind und wenn ja, dann wird diese kleingeschrieben zurück gegeben

        return items_uberschrift
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        if my_db:
            my_db.close()

def fetch_tables(table_name, excluded_columns): 
    # table_name soll den Tabellenname Erhalten und excluded_columns soll die Liste mit den auszublendenen Spalten geben
    try:
        my_db = init_connection()
        cur = my_db.cursor()

        columns = fetch_headers(table_name, excluded_columns)
        # columns = [row[0] for row in cur.fetchall()]

        if columns:
            cur.execute(f"SELECT {', '.join(columns)} FROM {table_name};")
            results = cur.fetchall()

            return results
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)
    finally:
        if my_db:
            my_db.close()


def table_sort(table_name, sorted_by, excluded_columns, DESC_OR_ASC):  #sortiert die gegebene Tabelle nach der Überschrift 
    try:
        my_db = init_connection()
        cur = my_db.cursor()

        columns = fetch_headers(table_name, excluded_columns)
        cur.execute(f"SELECT * FROM {table_name} ORDER BY {sorted_by} {DESC_OR_ASC};") 
        # ASC macht es Alphabetisch DESC würde es unkehren
        sort_answer = cur.fetchall()

        return sort_answer        
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)
    finally:
        if my_db:
            my_db.close()

def item_update_damage(name,tag,foreign_item_num, type, image, description, entry_date=None, end_date=None):
    """
    Inserts data into the database table with columns:
    foreign_item_num, indexnum (auto-increment), type, image, description, entry_date, end_date.

    Parameters:
        name (str): Itemname
        Tag (str): an welchem Tag wurde es hochgeladen
        foreign_item_num (int): Foreign key referring to an item.
        type (str): Type of the data.
        image (str): Path or URL to the image.
        description (str): Description of the data.
        entry_date (str): Entry date in YYYY-MM-DD format (optional).
        end_date (str): End date in YYYY-MM-DD format (optional).

    Returns:
        bool: True if the insertion was successful, False otherwise.
    """
    from datetime import datetime
    

    
    if entry_date is None:
        entry_date = datetime.now().strftime('%d.%m.%Y')

    try:
        # Connect to the SQLite database
        conn = init_connection()
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute(
            """
            INSERT INTO history(name, tag, foreign_item_num, type, image, description, entry_date, end_date)
            VALUES (? ,?, ?, ?, ?, ?, ?, ?)
            """,
            (name, tag, foreign_item_num, type, image, description, entry_date, end_date)
        )

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def update_item(item_data):
    """
    Aktualisiert einen bestehenden Eintrag in der Tabelle 'items' anhand der ID.

    :param db_path: Pfad zur SQLite-Datenbankdatei
    :param item_data: Ein Dictionary mit den Schlüsseln:
                      'ID', 'Name', 'Gruppe', 'Raum', 'amount',
                      'Details', 'service_tag', 'added_by_user',
                      'Typ', 'Status'
    """

    try:
        # Verbindung zur Datenbank herstellen
        connection = init_connection()
        cursor = connection.cursor()



        query = """
            UPDATE items
            SET Name = ?, 
                Gruppe = ?, 
                Raum = ?, 
                amount = ?, 
                Details = ?, 
                service_tag = ?, 
                added_by_user = ?, 
                Typ = ?, 
                Status = ?
            WHERE ID = ?;
        """

        # Beispiel: item_data enthält die Werte für die Abfrage
        cursor.execute(query, (
            item_data[1],  # Name
            item_data[2],  # Gruppe
            item_data[3],  # Raum
            item_data[4],  # amount
            item_data[5],  # Details
            item_data[6],  # service_tag
            item_data[9],  # added_by_user
            item_data[7],  # Typ
            item_data[8],  # Status
            item_data[0]   # ID (WHERE-Bedingung)
))

        # Änderungen speichern
        connection.commit()
        if cursor.rowcount > 0:
            print("Eintrag erfolgreich aktualisiert.")
        else:
            print("Kein Eintrag mit der angegebenen ID gefunden.")

    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Informationen:", str(e)

    finally:
        # Verbindung schließen
        if connection:
            connection.close()


def show_image_from_db(indexnum):
    from tkinter import Toplevel, Label
    from PIL import Image, ImageTk
    import io
    try:
        # Connect to the SQLite database
        conn = init_connection()
        cursor = conn.cursor()
        
        # Fetch the image data for the secified index number
        cursor.execute("SELECT image FROM history WHERE indexnum = ?", (indexnum,))
        result = cursor.fetchone()
        
        if result is None or result[0] is None:
            print("No image found for the given index number.")
            return None
        print("Image selected")
        image_data = result[0]
        conn.close()
        
        # Create a popup window
        popup = Toplevel()
        popup.title(f"Image Viewer - Index {indexnum}")
        
        # Convert binary data to an image
        image = Image.open(io.BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        
        # Display the image in the popup window
        label = Label(popup, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()
        
        popup.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")


def show_history_table(item_ID, excluded_columns):
    try:
        global item_ID_set
        item_ID_set = item_ID
        my_db = init_connection()
        cur = my_db.cursor()
        columns = fetch_headers("history", excluded_columns)
        if columns:
            cur.execute(f"SELECT {', '.join(columns)} FROM history WHERE foreign_item_num = ?", (item_ID,))
            results = cur.fetchall()
        
        return results
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Historie:", str(e)
    finally:
        if my_db:
            my_db.close()


def delete_item():
    try:
        if item_ID_set:
            # Verbindung zur Datenbank herstellen
            connection = init_connection()
            cursor = connection.cursor()

            # SQL-Abfrage zum Löschen eines Eintrags
            cursor.execute("DELETE FROM items WHERE ID = ?", (item_ID_set,))

            # Änderungen speichern
            connection.commit()
        else:
            pass

    except sqlite3.Error as e:
        return [], "Fehler beim Löschen des Eintrags:", str(e)

    finally:
        # Verbindung schließen
        if connection:
            connection.close()


def does_user_have_the_right(which_right):
    try:
        # Überprüfen, ob der Benutzername gültig ist
        if username_global == "Benutzername Ungültig":
            return False

        # Verbindung zur Datenbank herstellen
        my_db = init_connection()
        cur = my_db.cursor()

        # Sichere Abfragen mit Platzhaltern verwenden, um SQL-Injection zu vermeiden
        cur.execute("SELECT Rolle FROM benutzer WHERE Benutzername = ?", (username_global,))
        role = cur.fetchone()

        # Prüfen, ob die Rolle gefunden wurde
        if not role:
            return False

        cur.execute("SELECT * FROM permissions WHERE roles = ?", (role[0],))
        right = cur.fetchone()

        # Verbindung schließen
        my_db.close()

        # Prüfen, ob die Rechte vorhanden sind und ob das gewünschte Recht gesetzt ist
        if right and right[which_right] == "True":
            return True
        else:
            return False
    except sqlite3.Error as e:
        print("Fehler beim Abrufen der Informationen:", e)
        return False

def get_group_icon(groupId):
    conn = init_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT Gruppen_Bild FROM Gruppen WHERE ID = {groupId}")
    result = cursor.fetchone()[0]
    conn.close()
    return result


def add_group_in_DB(group_name, group_icon):
    try:
        conn = init_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Gruppen (Gruppen_name, Gruppen_Bild) VALUES (?, ?)", (group_name, group_icon))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


##############################
## UNBENUTZTE DEFINITIONEN: ##
##############################

# def group_search(search_number):
#     try:
#         my_db = init_connection()
#         cur = my_db.cursor()
#         cur.execute("SELECT * FROM items WHERE Gruppe = ?", search_number)
#         gruppen_suchen_ergebnis = cur.fetchall()
#         return gruppen_suchen_ergebnis
#     except sqlite3.Error as e:
#         return [], "Fehler beim Abrufen der Gruppensuche:", str(e)
#     finally:
#         if my_db:
#             my_db.close()










#############################
### BIS HIER HIN BEHALTEN ###
#############################




def get_group_table_lenght():
    try:
        my_db = init_connection()
        cur = my_db.cursor()

        # Query to fetch the maximum index
        query = "SELECT MAX(`ID`) AS max_index FROM Gruppen;"
        
        # Execute the query
        cur.execute(query)
        result = cur.fetchone()

        # Extract the maximum index value
        max_index = result[0] if result else None

        return max_index

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Always close the cursor and connection
        cur.close()
        my_db.close()

def get_group_information_from_db(groupindex):
    try:
        # Initialize the database connection
        my_db = init_connection()
        cur = my_db.cursor()

        # Query to fetch groupname and image based on groupindex
        query = """
            SELECT Gruppen_name, Gruppen_Bild 
            FROM Gruppen 
            WHERE `ID` = ?;
        """

        # Execute the query with the provided groupindex
        cur.execute(query, (groupindex,))
        result = cur.fetchone()

        if result:
            groupname, image = result
            return {"groupname": groupname, "image": image}
        else:
            return None  # No matching row found

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        cur.close()
        my_db.close()