import sqlite3
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

path:str = os.getcwd()+'./db/Inventarisierungs_DB.sqlite3'



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

def fetch_items():
    """
    - Gibt eine Liste von items zurück
    - Gibt Spaltenname zu allem mit
    """
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("SELECT * FROM items")
        rows = cur.fetchall()      
        return rows
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        my_db.close()

def fetch_items_headers():
    try:
        my_db = init_connection()
        cur = my_db.cursor()
        cur.execute("PRAGMA table_info(items)")
        alles = cur.fetchall()
        uberschrift = [i[1] for i in alles]       
        return uberschrift
    except sqlite3.Error as e:
        return [], "Fehler beim Abrufen der Hardware-Einträge:", str(e)
    finally:
        my_db.close()


root = tk.Tk()
root.title("Datenbank-Überschriften anzeigen")
root.geometry("600x400")
tree = ttk.Treeview(root, show="headings", height=15)
tree.pack(expand=True, fill="both")

#####################
# AB HIER EINBINDEN #



# Spaltennamen aus der Datenbank holen
uberschrift = fetch_items_headers()

# Überschriften konfigurieren
tree["columns"] = uberschrift
for up in uberschrift:
    tree.column(up, anchor=CENTER, width=100)
    tree.heading(up, text=up)

data = fetch_items()

# Daten aus DB einfügen

for i,row in enumerate(data):
    formatted_row = [value if value is not None else "-" for value in row] # Leere Felder durch "-" ersetzen
    color = "#f3f3f3" if i % 2 == 0 else "white"
    tree.insert("", "end", values=formatted_row, tags=("even" if i % 2 == 0 else "odd"))



# BIS HIER #
############

root.mainloop()


