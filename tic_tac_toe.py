spielbrett = [0, 0, 0, 0, 0, 0, 0, 0, 0 ]

print(spielbrett)

def spielbrett_ausdrucken():
    print(spielbrett[0], " | ", spielbrett[1], " | ", spielbrett[2])
    print("-------------")
    print(spielbrett[3], " | ", spielbrett[4], " | ", spielbrett[5])
    print("-------------")
    print(spielbrett[6], " | ", spielbrett[7], " | ", spielbrett[8])
    print()

spielbrett_ausdrucken()

while True:
    print("Spieler 1, geben sie das Spielfeld an: ")
    feld_nr = input()
    feld_nr = int(feld_nr)
    if spielbrett[feld_nr] == 0:
        spielbrett[feld_nr] = 1
    # Erste Zeile
    if spielbrett[0] == spielbrett[1] and spielbrett[1] == spielbrett[2] and spielbrett[0] !=0:
        print("Gewonnen!")
        quit()
    # Zweite Zeile
    if spielbrett[3] == spielbrett[4] and spielbrett[4] == spielbrett[5] and spielbrett[3] !=0:
        print("Gewonnen!")
        quit()
    spielbrett_ausdrucken()
    # Dritte Zeile
    if spielbrett[6] == spielbrett[7] and spielbrett[7] == spielbrett[8] and spielbrett[6] !=0:
        print("Gewonnen!")
        quit()
    spielbrett_ausdrucken()

    # Erste Spalte
    if spielbrett[0] == spielbrett[3] and spielbrett[3] == spielbrett[6] and spielbrett[6] !=0:
        print("Gewonnen!")
        quit()
    spielbrett_ausdrucken()
    # Zweite Spalte
    if spielbrett[1] == spielbrett[4] and spielbrett[4] == spielbrett[7] and spielbrett[7] !=0:
        print("Gewonnen!")
        quit()
    # Dritte Spalte
    spielbrett_ausdrucken()
    if spielbrett[2] == spielbrett[5] and spielbrett[5] == spielbrett[8] and spielbrett[8] !=0:
        print("Gewonnen!")
        quit()
    spielbrett_ausdrucken()

    # Erste Diagonale
    if spielbrett[0] == spielbrett[4] and spielbrett[4] == spielbrett[8] and spielbrett[8] !=0:
        print("Gewonnen!")
        quit()
    spielbrett_ausdrucken()

    # Zweite Diagonale
    if spielbrett[2] == spielbrett[4] and spielbrett[4] == spielbrett[6] and spielbrett[6] !=0:
        print("Gewonnen!")
        quit()
    spielbrett_ausdrucken()










    print("Spieler 2, geben sie das Spielfeld an: ")
    feld_nr = input()
    feld_nr = int(feld_nr)
    if spielbrett[feld_nr] == 0:
        spielbrett[feld_nr] = 2 

    spielbrett_ausdrucken()


