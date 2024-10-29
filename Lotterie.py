import random
import json

try:
    with open("lotterie_leaderboard.txt", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []

while True:
    x = input("Benutzername eingeben (max.15): ")
    if len(x) > 2 and len(x) < 16:
        tag = x
        break
    else:
        print("Nochmal")
        continue 


existing_user = next((user for user in users if user[0] == tag), None)

money = 1000
if existing_user:
    money = existing_user[1]

else:
    user = [tag, money]
    users.append(user)

null = 0

with open("lotterie_leaderboard.txt", "w") as f:
    json.dump(users, f)
sorted_users = sorted(users, key=lambda user: user[1], reverse=True)
with open("lotterie_leaderboard.txt", "w") as f:
    json.dump(sorted_users, f, indent=4)



while True:
    
    sorted_users = [user for user in sorted_users if user[0] != tag]
    with open("lotterie_leaderboard.txt", "w") as f:
        json.dump(sorted_users,f,indent=1) 
    with open("lotterie_leaderboard.txt", "w") as f:
        json.dump(sorted_users, f, indent=4)

    user = [tag, money]
    sorted_users.append(user)    
    with open("lotterie_leaderboard.txt", "w") as f:
        json.dump(sorted_users, f)
    loose = 0
    if money == 0:
        print("Kein Geld mehr!!!")
        break
    Spielauswahl =  input("\n\n\n\n\n\n\n\n\n\n\n\n\nHier können sie ein Spiel auswählen\n"
                    "0: Leaderboard\n"
                    "1: Roulette\n"
                    "2: Slotmaschine\n"
                    "9: Pause machen\n\n"
                    "Ihr Aktuelles Geld: " + str(money) + "€ \n" 
                    "Ihre Auswahl: ")
        
    if Spielauswahl == '0':
        print("Index  Name             Geld")
        print("-" * 40)
        index: int = 0
        for user in sorted_users:
            print(f"{index + 1:<6} {user[0][:16]:<16} {user[1]:<10} €")
            index += 1
        input("zurück: ")
           
    elif Spielauswahl == '1':
        while True:
            if money == 0:
                    print("Kein Geld mehr!!!")
                    break
            roulette_try = input("\n\n\n\n\nWillkommen bei Roulette\n\n" 
                                "a: um die Auswahlmöglichkeiten zu sehen\n"    
                                "unbenutztes um das Spiel zu wechseln\n\n"  
                                "Ihr Aktuelles Geld: " + str(money) + "€ \n"
                                "Ihre Auswahl : ")
            if roulette_try == 'a':
                roulette_try = input("Ihre Auswahlmöglichkeiten:\n"
                                "0-36 bestimmte Zahl erraten   (x*36)\n"
                                "r für rote Zahl               (x*2)\n" 
                                "s für schwarze Zahl           (x*2)\n" 
                                "u für ungerade Zahl           (x*2)\n" 
                                "g für gerade Zahl             (x*2)\n" 
                                "112  für Zahlen von 1  bis 12 (x*3)\n"    
                                "1324 für Zahlen von 13 bis 14 (x*3)\n"    
                                "2536 für Zahlen von 25 bis 36 (x*3)\n"     
                                "118  für Zahlen von 1  bis 18 (x*2)\n"     
                                "1936 für Zahlen von 19 bis 36 (x*2)\n"
                                "unbenutztes um das Spiel zu wechseln\n\n"  
                                f"Ihr Aktuelles Geld: {money}€ \n"
                                "Ihre Auswahl : ")
            try:
                roulette_try = int(roulette_try)
            except ValueError:
                pass
            if roulette_try == 'q':
                break
            roulette_erg = random.randint(0,36)             #zufallszahl
            roulette_liste = ['r','s']
            roulette_farbe = random.choice(roulette_liste)  #zufallsfarbe
            #if roulette_farbe == 'r':
            #    roulette_farbe = random.choice(roulette_liste)  #rigged to black
            if (isinstance(roulette_try,int) and roulette_try >= 0) or roulette_try in ['r','s','u','g']:
                einsatz = input("Wieviel möchten sie Setzen: ")
                try:
                    einsatz = int(einsatz)
                    if einsatz <= 0 or einsatz > money:
                        raise ValueError("Ungültiger Einsatz!")
                except ValueError:
                    print("Ungültige Eingabe, bitte versuchen Sie es erneut.")
                    continue
                money = money - einsatz
                print("Dein Versuch: ",roulette_try)
                if roulette_erg == 0:
                    print("Das Ergebnis: ",roulette_erg)
                    null = 1
                else:
                    print("Das Ergebnis: ",roulette_farbe,roulette_erg)
                    null = 0
                if isinstance(roulette_try,int):
                    if roulette_try >= 0 and roulette_try <= 36:
                        if roulette_try == roulette_erg:
                            money = money + einsatz * 36
                            print("OMG du hast es Getroffen!!! hier dein Aktuelles Geld: ",money)
                        else:
                            loose = 1
                    elif roulette_try == 112:
                        if roulette_erg >= 1 and roulette_erg <= 12:
                            money = money + einsatz * 3
                            print("Herzlichen Glückwunsch, die Zahl ist im ersten Drittel! Hier ihr aktuelles Geld: ",money)
                        else:
                            loose = 1
                    elif roulette_try == 1324:
                        if roulette_erg >= 13 and roulette_erg <= 24:
                            money = money + einsatz * 3
                            print("Herzlichen Glückwunsch, die Zahl ist im zweiten Drittel! Hier ihr aktuelles Geld: ",money)
                        else:
                            print("Schade diesmal hattest du kein Glück... Dein Geld: ",money)
                            loose = 1
                    elif roulette_try == 2536:
                        if roulette_erg >= 25 and roulette_erg <= 36:
                            money = money + einsatz * 3
                            print("Herzlichen Glückwunsch, die Zahl ist im letzten Drittel! Hier ihr aktuelles Geld: ",money)
                        else:
                            loose = 1
                    elif roulette_try == 118:
                        if roulette_erg >= 1 and roulette_erg <= 18:
                            money = money + einsatz * 2
                            print("Herzlichen Glückwunsch, die Zahl ist in der ersten hälfte! Hier ihr aktuelles Geld: ",money)
                        else:
                            loose = 1
                    elif roulette_try == 1936:
                        if roulette_erg >= 19 and roulette_erg <= 36:
                            money = money + einsatz * 2
                            print("Herzlichen Glückwunsch, die Zahl ist in der letzten hälfte! Hier ihr aktuelles Geld: ",money)
                        else:
                            loose = 1
                    else:
                        break
                elif (roulette_erg % 2) == 0 and roulette_try in ['g','u'] and null == 0:
                    if roulette_try == 'g':
                        money = money + einsatz * 2
                        print("Herzlichen Glückwunsch, die Zahl ist Gerade! Hier ihr aktuelles Geld: ",money)
                    else:
                        loose = 1
                elif roulette_try in ['g','u'] and null == 0:
                    if roulette_try == 'u':
                        money = money + einsatz * 2
                        print("Herzlichen Glückwunsch, die Zahl ist Ungerade! Hier ihr aktuelles Geld: ",money)
                    else:
                        loose = 1
                elif roulette_try == 's' and null == 0:
                    if roulette_farbe == 's':
                        money = money + einsatz * 2
                        print("Herzlichen Glückwunsch, die Zahl ist Schwarz! Hier ihr aktuelles Geld: ",money)
                    else:
                        loose = 1
                elif roulette_try == 'r' and null == 0:
                    if roulette_farbe == 'r':
                        money = money + einsatz * 2
                        print("Herzlichen Glückwunsch, die Zahl ist Rot! Hier ihr aktuelles Geld: ",money)
                    else:
                        loose = 1
                elif null == 1:
                    loose = 1
                if loose == 1:
                    print("Schade, aber beim nächsten mal Gewinnen sie bestimmt :) ")
                continue                  
            else:
                break
    
    elif Spielauswahl == '2':
        while True:
            automat_eingabe = input("\n\n\n\nHezlich Willkommen beim Spielautomaten\n"
                                    "buchstabe um das Spiel zu wechseln\n\n\n"
                                    "Ihr Aktuelles Geld: " + str(money) + "€ \n"
                                    "Ihr Einsatz: ")
            if automat_eingabe == "":
                automat_eingabe = ehemalige_eingabe
                if ehemalige_eingabe > money:
                    print("nicht genus Geld")
                    break
            try:
                automat_eingabe = int(automat_eingabe)
            except ValueError:
                print("Ausgabe Beendet")
                break
            if automat_eingabe >= 0 and automat_eingabe <= money:
                tipps_system: list = []
                duplicates = []
                i = 0
                anzahl = 0
                money = money - automat_eingabe
                while i < 3:
                    zahl = random.randint(1,9)
                    i+=1
                    if zahl in tipps_system:                        
                        anzahl = anzahl + 1
                    tipps_system.append(zahl)
                    if tipps_system.count(zahl) > 1 and zahl not in duplicates:
                            duplicates.append(zahl)                 
                
                #print(tipps_system)
                #print(zahl)
                #print(duplicates)
                
                
                print(tipps_system)
                print("Treffer: ",anzahl)
                if anzahl == 1:                          #Treffer Warscheinlichkeiten: 30,85% und für 3: 1,235%
                    money = money + (automat_eingabe * 2)
                    print("Sie haben Getroffen!!!")
                elif anzahl == 2:
                    if zahl == '9':
                        money = money + ((automat_eingabe * 2) ** 2)
                    elif zahl == '7':
                        money = money + ((automat_eingabe * 3) ** 2)
                        
                    else:
                        money = money + automat_eingabe * 4
                    print("WOW 3 gleiche!!! Die Chansen dafür sind 1,235%!!!")
                        
                else:
                    print("Schade, vielleicht beim Nächsten mal")
                ehemalige_eingabe = automat_eingabe
            else:
                print("Nicht genug Geld!")
                continue
            
    elif Spielauswahl == '9':
        break
    else:
        break