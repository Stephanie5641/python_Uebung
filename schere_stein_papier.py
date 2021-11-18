
import random


zufallszahl = random.randint(0, 2)

liste =["schere", "stein", "papier"]

computer = liste[zufallszahl]


print("Schere, Stein oder Papier?")
zettel = input()

if zettel == "stein":
    if computer == "schere":
        print("gewonnen")
    if computer == "papier":
        print("verloren")
    if computer == "stein":
        print("unentschieden")

if zettel == "schere":
    if computer == "schere":
        print("unentschieden")
    if computer == "papier":
        print("gewonnen")
    if computer == "stein":
        print("verloren")

if zettel == "papier":
    if computer == "schere":
        print("verloren")
    if computer == "stein":
        print("gewonnen")
    if computer == "papier":
        print("unentschieden")
