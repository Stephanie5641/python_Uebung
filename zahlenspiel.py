import random
zufallszahl = random.randint(1, 1000)
i = 1
while i <= 20:
    print("Geben sie eine Zahl zwischen 1 und 1000 bitte ein:")
    x = input()
    x = int(x)
    print(zufallszahl)
    print(abs(zufallszahl - x)

    if zufallszahl == x:
        print("Richtig")
    if zufallszahl != x:
        print("Falsch")
    if zufallszahl > x:
        print("zu niedrig")
    if zufallszahl < x:
        print("zu hoch")
    i = i + 1
