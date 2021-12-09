import random

zahl_kreiert_ohne_duplizierte_ziffern = False
while zahl_kreiert_ohne_duplizierte_ziffern == False:
    print(5)
    zufallszahl = random.randint(1000, 9999)
    zufallszahl_liste =[int(i) for i in str(zufallszahl)] 
    #print(zufallszahl_liste)
    set_zufallszahl = set(zufallszahl_liste)
        
    if len (set_zufallszahl) == len(zufallszahl_liste):
        print("Keine duplizierte Ziffern")
        zahl_kreiert_ohne_duplizierte_ziffern = True
    else:
        print("duplizierte Ziffern")



while True:
    

    eingabe = input()
    zufallszahl_liste = [int(i) for i in str(zufallszahl)]
    # print(zufallszahl_liste)
    eingabe_liste = [int(i) for i in str(eingabe)]

    if(str(zufallszahl) == eingabe):
        print("Richtig")
    else:
        print("Falsch")

    #if zufallszahl == 
    bulls = 0 
    if zufallszahl_liste[0] == eingabe_liste[0]:
        bulls = bulls + 1
    if zufallszahl_liste[1] == eingabe_liste[1]:
        bulls = bulls + 1
    if zufallszahl_liste[2] == eingabe_liste[2]:
        bulls = bulls + 1
    if zufallszahl_liste[3] == eingabe_liste[3]:
        bulls = bulls + 1

    cows = 0
    if eingabe_liste[0] in zufallszahl_liste:
        cows = cows + 1
    if eingabe_liste[1] in zufallszahl_liste:
        cows = cows + 1
    if eingabe_liste[2] in zufallszahl_liste:
        cows = cows + 1
    if eingabe_liste[3] in zufallszahl_liste:
        cows = cows + 1
    cows = cows - bulls

    print(bulls, "bulls")
    print(cows, "cows")