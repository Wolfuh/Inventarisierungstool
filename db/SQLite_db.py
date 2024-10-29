import sqlite3

my_db = sqlite3.connect('test.db')
my_dbc = my_db.cursor()

#sql = """
#        CREATE TABLE rollen2(
#            name TEXT,
#            add_user BOOLEAN
#        )
#    """
#my_dbc.execute(sql)
#my_db.commit()

sql = """ALTER TABLE rollen2
ADD """

def addUser(name, passw):
    sql = f"""
        INSERT INTO rollen2 (name, add_user) VALUES (
            '{name}',
            '{bool(passw)}'
        )
    """
    my_dbc.execute(sql)
    my_db.commit()

def get_all_data() -> list[tuple[str, str]]:  # type: ignore
    my_dbc.execute("SELECT * FROM rollen2")
    nutzer = my_dbc.fetchall()
    return nutzer
all_users = get_all_data()

while True:
    action = input("Was möchten sie tun?\n"
                   "1: Anmelden\n"
                   "2: Benutzer anlegen\n"
                   "3: datenbank ansehen\n"
                   "Ihre Auswahl: ")

    if action == '1':

        user = input("name: ")
        if user == '' or user == ' ':
            print("abgebrochen")
            continue
        password = input("passwort: ")
        if password == '' or password == ' ':
            print("abgebrochen")
            continue

        BothIsKnown = any(user.lower() == existing_user.lower() and password == existing_password for (existing_user, existing_password) in all_users)

        if BothIsKnown:
            print("erfolgreich eingeloggt")
            logged_in = True
        else:
            print("benutzername oder passwort ist falsch")

    elif action == '2':
        while True:
            user = input("name: ")

            if user == '' or user == ' ':
                print("abgebrochen")
                break

            OneIsKnown = any(user.lower() == existing_user.lower() for (existing_user, _) in all_users)
            if OneIsKnown:
                print("Benutzer bereits vergeben")
                continue
            password = input("passwort: ")
            if password == '' or password == ' ':
                print("abgebrochen")
                break
            addUser(user, password)
            print("benutzer erfogreich hinzugefügt")
            break
    elif action == '3':
        all_users = get_all_data()
        print(all_users)
    else:
        break