import sqlite3

my_db = sqlite3.connect('users.db')
my_dbc = my_db.cursor()


#Tabelle erstellen: CREATE TABLE tabellenname (N_überschrift1 TEXT, N_überschrift2 BOOLEAN)
#Daten einfügen:    INSERT INTO tabellenname (überschrift1, überschrift2) VALUES (N_wert2 TEXT, N-wert2 BOOLEAN)
#Daten ändern:      UPDATE tabellenname SET überschrift1 = N_wert1 WHERE bedingung 
#   z.B. """UPDATE rollen2 SET add_user = 0 WHERE name = 'nutzer'"""
#ausführen: my_dbc.execute(sql)
#           my_db.commit()


def add_user(name, passw):
    sql = "INSERT INTO users (user_first_name, password) VALUES (?, ?)"
    my_dbc.execute(sql, (name,passw))
    my_db.commit()

def delete_user(zu_löschender_user):
    sql = """DELETE FROM users WHERE user_first_name = ?"""
    my_dbc.execute(sql, (zu_löschender_user,))
    my_db.commit()

def get_all_data() -> list[tuple]: # type: ignore
    my_dbc.execute("SELECT * FROM users")
    nutzer = my_dbc.fetchall()
    return nutzer


all_users = get_all_data()

while True:
    action = input("Was möchten sie tun?\n"
                   "1: Anmelden\n"
                   "2: Benutzer anlegen\n"
                   "3: datenbank ansehen\n"
                   "4: Nutzer per Name entfernen (Debug)\n"
                   "Ihre Auswahl: ")

    if action == '1':

        user = input("name: ").strip()  #leerzeichen werden entfernt
        if user == '':
            print("da muss schon was stehen")
            continue
        password = input("passwort: ").strip()  #leerzeichen werden entfernt
        if password == '' or password == ' ':
            print("abgebrochen")
            continue

        BothIsKnown = any(user.lower() == existing_user[1].lower() and password == existing_user[5] for
                        existing_user in all_users)

        if BothIsKnown:
            print("erfolgreich eingeloggt")
            # logged_in = True
        else:
            print("benutzername oder passwort ist falsch")

    elif action == '2':
        while True:
            user = input("name: ").strip()

            if user == '' or len(user) < 3 or len(user) > 16:
                print("Benutzername muss zwischen 6 und 16 zeichen sein")
                break

            OneIsKnown = any(user.lower() == existing_user[1].lower() for existing_user in all_users)
            if OneIsKnown:
                print("Benutzer bereits vergeben")
                continue
            password = input("passwort: ")
            if password == '' or len(password) < 6 or len(password) > 16:
                print("passwort muss zwischen 6 und 16 zeichen sein")
                break
            add_user(user, password)
            print("benutzer erfogreich hinzugefügt")
            break

    elif action == '3':
        all_users = get_all_data()
        print(all_users)

    elif action == '4':
        user_to_delete = input("Der zu löschende Name: ")
        if  any(user_to_delete.lower() == existing_user[1].lower() for existing_user in all_users):
            delete_user(user_to_delete)
            print("Nutzer erfolgreich entfernt")
        else:
            print("Nutzer nicht gefunden")
    else:
        my_db.close()
        break
#reteil