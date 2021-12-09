# Einleitung: Speilbrett

spielbrett = [0, 0, 0, 0, 0, 0, 0, 0, 0]
def spielbrett_ausdrucken():
    print(spielbrett[0], spielbrett[1], spielbrett[2])
    print(spielbrett[3], spielbrett[4], spielbrett[5])
    print(spielbrett[6], spielbrett[7], spielbrett[8])

spielbrett_ausdrucken()
# chip einfügen
spielbrett_ausdrucken()
# chip einfügen
spielbrett_ausdrucken()
# ...

# Euro in Yen konvertiern mit einer Eingabe 
# durch die konsole 
def euro_zu_yen():
    euro = input("Euro: ")
    euro = float(euro)
    yen =  131.70 * euro
    print("Yen: ", yen)
#euro_zu_yen()


 # Yen in Euro konventieren mit einer Eingabe 
 # durch die konsole
def yen_zu_euro():
     yen = input("yen: ")
     yen = float(yen)
     euro = (1/131.70) * yen
     print("euro: ",euro)
#yen_zu_euro()


# Bitcoin in Euro konventieren mit einer Eingabe
# durch die Konsole
def bitcoin_zu_euro():
    bitcoin = input("bitcoin: ")
    bitcoin = float(bitcoin)
    euro = (49571.37) * bitcoin
    print("Euro: ", euro)
#bitcoin_zu_euro()


# Zentimenter in Kilometer konventieren mit einer Eingabe 
# durch die Konsole
def zentimeter_zu_kilometer():
    zentimeter = input("zentimeter: ")
    zentimeter = float(zentimeter)
    kilometer = zentimeter / 100000
    print("Kilometer: ", kilometer)

# Meter in millimeter konventieren mit einem Eingabeparameter
def meter_zu_millimeter(meter):
    # meter = 6
    millimeter = 1000 * meter
    print("Millimeter: ", millimeter)
meter_zu_millimeter(6)
# millilieter in Liter konventieren mit einem Eingabeparameter
def milliliter_zu_liter(ml):
    liter = 0.001 * ml
    print("Liter: ", liter)
milliliter_zu_liter(10000)

# Getränkeautomat
def getraenkeautomat(anzahl_1cent, anzahl_2cent,  anzahl_5cent, anzahl_10cent, anzahl_20cent, anzahl_50cent, anzahl_1euro, anzahl_2euro):
    summe = 0.01 * anzahl_1cent + 0.02 * anzahl_2cent + 0.05 * anzahl_5cent + 0.10 * anzahl_10cent + 0.20 * anzahl_20cent + 0.50 * anzahl_50cent + 1 * anzahl_1euro + 2 * anzahl_2euro
    print("Gesamtbetrag:", summe)
getraenkeautomat(1, 7, 1, 0, 1, 3, 4, 5)

# Das Maximum von einer Auswahl, bestehend aus 2 Zahlen, berechnen
def maximum(zahl1, zahl2):
    if zahl1 > zahl2:
        print(zahl1)
    else:
        print(zahl2)

maximum(4, 6)

# Das Minimum von einer Auswahl, bestehend aus 2 Zahlen berechnen
def minimum(zahl1, zahl2):
    if zahl1 > zahl2:
        print(zahl1)
    else:
        print(zahl2)
    
        
       

# das Maximum von einer Auswahl, bestehend aus 3 Zahlen, berechnen
def maximum_von_3_Zahlen(zahl1, zahl2, zahl3):
    if zahl1 > zahl3 and zahl1 > zahl2:
        print(zahl1)
    
    elif zahl2 > zahl1 and zahl2 > zahl3:
        print(zahl2)
    else:
        print(zahl3)
maximum_von_3_Zahlen


# Eine neue liste, "Einkaufswagen", erstellen
einkaufswagen = [7.50, 18.32, 10.99, 49.58, 7.10]


# Eine Funktion erstellen die alle Elemente des Einkaufswagens (jewiels auf einer neuen Zeile) ausdruckt.
laenge = len(einkaufswagen)
i = 0
while i < laenge:
    print(einkaufswagen[i]) 
    i = i + 1

# Eine Funktion erstellen die den Gesamtpreis des Einkaufswagens ermittelt.
einkaufswagen = [7.50, 18.32, 10.99, 49.58, 7.10]
i = 0
summe = 0
while i < len (einkaufswagen):
    summe = summe + einkaufswagen[i]
    i = i + 1
print("Gesamtsumme:", summe)


# Eine funktion erstellen die den durchschnittspreis des Einkaufswagens ermittelt.
anzahl = len(einkaufswagen)
print("Durchschnittspreis:", summe / anzahl)







  





