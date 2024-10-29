import random, json

try:
    with open("users.txt", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
money = 200

while True:
    if money == 0:
        print("Kein Geld mehr!!!")
        break
    auswahl = input("\n\n\n\n\n1: Lotto Spielen\n"
                    "2: einfache Personalverwaltung\n"
                    "3: Palindrom Test\n"
                    "9: beenden\n\n"
                    "Dein Geld: " + str(money) + "€\n"
                    "Wählen sie eine Möglichkeit: ")

    if auswahl == '1':
        wiederholung = 1
        treffer = 0
        if money == 0:
            print("Kein Geld mehr!!!")
            break
        print("Geben sie 6 Zahlen zwischen 1 und 49 ein.")
        guesses = []
        while len(guesses) < 6:
            guess = input("Bitte geben sie die " + str(wiederholung) + ". Zahl ein: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Bitte eine Zahl eingeben")
                continue
            if (guess in guesses) or guess >= 50 or guess <= 0:
                print("Bitte geben sie eine gültige Zahl\n")
                continue
            guesses.append(guess)

        lottozahlen = []
        while len(lottozahlen) < 6:
            zufallszahl = random.randint(1,49)
            if zufallszahl in lottozahlen:
                continue
            if zufallszahl in guesses:
                #treffer += 1
                continue
            lottozahlen.append(zufallszahl)
        guesses.sort(reverse=False)
        lottozahlen.sort(reverse=False)
        print("Deine Zahlen: ",guesses)
        print("Lottozahlen: ",lottozahlen)
        print("Treffer: ",treffer)

    elif auswahl == '2':
            cont: bool = True

            while cont:
                erg_ver = input("1:   Nutzer Hinzufügen\n"
                          "2:   Nutzer Anzeigen\n"
                          "3:   Nutzer Entfernen\n"
                          "4:   Zurück\n"
                          "Bitte eine Aktion Ausw\u00e4hlen (1-4): ")

                if erg_ver == '1':
                    nachN = input("Nachname: ")
                    vorN = input("Vorname: ")
                    geb = input("Geburtsdatum: ")
                    adresse = input("Wohnadresse: ")
                    email = input("E-Mail-Adresse: ")
                    user = [nachN, vorN, geb, adresse, email]
                    users.append(user)
                    with open("users.txt", "w") as f:
                        json.dump(users, f)
                    
                    
                elif erg_ver == '2':
                    print("Index  Name         Vorname      Geburtstag    Wohnadresse          E-Mail")
                    print("-" * 90)
                    index: int = 0
                    for user in users:
                        print(f"{index:<6} {user[0][:12]:<12} {user[1][:12]:<12} {user[2][:12]:<13} {user[3][:19]:<20} {user[4][:30]:<30}")
                        index += 1
                    print()
                    
                elif erg_ver == '3':
                    ind: str = input("Zu löschender Index: ")
                    users.remove(users[int(ind)])
                    with open("users.txt", "w") as f:
                        json.dump(users, f)
                    
                elif erg_ver == '4':
                    cont = False
                    
    elif auswahl == '3':
        wort = input("Geben Sie Ein Wort ein: ")
        wort = wort.lower().replace(" ","")
        print(wort == wort[::-1])


    elif auswahl == '9':   
        print("Ausgabe Beendet")
        break 
