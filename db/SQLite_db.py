import sqlite3
import os

path:str = os.getcwd()+'./db/items.db'

print("Mathis du Hurensohn, arbeite mal lieber")

def init_connection():
    """
    Hilfsfunktion zur Herstellung einer Verbindung mit der SQLite-Datenbank.
    - Die Datenbankdatei muss unter dem angegebenen Pfad existieren.
    - row_factory wird auf sqlite3.Row gesetzt, um die Ergebnisse als Dictionaries zurückzugeben.
    """
    my_db = sqlite3.connect(path)
    # Wichtig ist das hier der Root-Pfad angegeben wirddaadvjrnjrmgkmvkmvlddmvlmvk,vfg fifmvlf ,gr,or,vorr,ogl

    my_db.row_factory = sqlite3.Row  # Rückgabe von Zeilen als Dictionary
    return my_db

def fetch_hardware():
    """
    Ruft alle Hardware-Einträge aus der Tabelle `Hardware` ab.
    - Gibt eine Liste von Dictionaries zurück.
    """
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("SELECT * FROM items")
        rows = cur.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        my_db.close()
