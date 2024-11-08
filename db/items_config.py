import sqlite3

def add_item(item_name, room, group, details, color, added_by_user):
    my_db = sqlite3.connect('./db/items.db')     # verbindung db
    my_dbc = my_db.cursor()                     # cursor erstellen
    my_dbc.execute(f"IMPORT INTO items * VALUES {item_name, room, group, details, color, added_by_user}")     # volle itemangabe in db übertragen
    my_db.commit()                                                                                            # mittlere berechtigung


def delete_item(item_to_delete):
    my_db = sqlite3.connect('./db/items.db')     # verbindung db
    my_dbc = my_db.cursor()                     # cursor erstellen
    my_dbc.execute(f"DELETE FROM item WHERE {item_to_delete}")     # volle itemangabe in db übertragen
    my_db.commit()                                                 # mittlere Berechtigung
