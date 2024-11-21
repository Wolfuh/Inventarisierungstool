import sqlite3

my_db = sqlite3.connect('./db/items.db')     # verbindung db
my_dbc = my_db.cursor()                      # cursor erstellen


   
    


i = 0
eingabe = 0
while not eingabe == "yes":

    eingabe = input("filtersuche: ")
    if eingabe == "reset":
            i = 0
            print("resetted ;)")
            continue
    auswahl = input("1: ganze Eingabe\n2: Einzelne eingabe\n3: Gruppensuche\nAuswahl: ")

    if auswahl == '1':
        my_dbc.execute("SELECT name FROM items WHERE name LIKE ?", (eingabe + '%',))
    elif auswahl == '2':
        

        if i == 0:
            ausgabe = eingabe
        else:
            ausgabe += eingabe
        my_dbc.execute("SELECT name FROM items WHERE name LIKE ?", ('%' + ausgabe + '%',))
        i+=1
    elif auswahl == '3':
        my_dbc.execute("SELECT name FROM items WHERE [group] IS ?", (eingabe,))


    ergebnisse = my_dbc.fetchall() 

    for eintrag in ergebnisse:
        print(eintrag)
    
    print(i)
    print(eingabe)
    print(ergebnisse)






   