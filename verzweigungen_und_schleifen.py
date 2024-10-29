
print()
#Aufgabe 2.1:
money1 = 0
monate1 = 0
while money1 < 1000:
    money1 = money1 + 20
    monate1 = monate1 + 1
    money1 = money1 + (money1 * 0.1)
    pass

print ("Ich muss " ,monate1, " Monate Warten, um mein Kontostand auf 1000€ zu erhöhen")


#Aufgabe 2.2:
money2 = 2000   #schulden
n = 12
r = 0.05

erg2 = (money2 * r * ((1+ r)**n)) / (((1+r)**n) - 1)    #formel für die Zinseszinzrechnung

print ("Ich muss " ,erg2,"€ pro Monat bezahlen.")


#Aufgabe 2.3:
while True:    
    print()
    print()
    print("1: alle ganzzahligen werte von 0 bis 100")
    print("2: alle geraden Zahlen von 0 bis 100")
    print("3: alle durch 3 und 5 Teilbaren Zahlen zwischen 0 und 100")
    print("4: Zahl in Binärzahl umwandeln")
    print("q: Ausgabe beenden")
    answer = input("Was soll angezeigt werden? ")

    if answer == '1':
        werte = 0
        while werte < 101:
            print(werte,end=' ')
            werte = werte + 1
    elif answer == '2':
        werte2 = 2
        while werte2 < 101:
            print(werte2,end=' ')
            werte2 = werte2 + 2
    elif answer == '3':
        werte3 = 15
        num1 = 3
        num2 = 5
        while werte3 < 101:
            look = (werte3 % num1) + (werte3 % num2)
            if look == 0:
                print (werte3,end=' ')
            werte3 = werte3 + 1

    elif answer == '4':
        zahl_1 = float(input("Dezimalzahl zwischen 0 und 1000: "))
        if zahl_1 >= 0 and zahl_1 <= 1000:
            print(bin(int(zahl_1))[2:])
        else:
            print("ungültige Eingabe")
    elif answer == 'q':
        print("Ausgabe beendet.")
        break
    else:
        print("Ungültige eingabe")
