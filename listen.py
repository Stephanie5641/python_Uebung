einkaufswagen = ["Schuh", "Hut", "Socken"]
liste = [2, "Random Text", 4.5, True, [1, 4, 5]]

# das dritte Element ausdrucken
print(liste[2])

# das dritte Element verändern
print(liste)
liste[2] = 5.5
print(liste)

# das erste Element ausdrucken 
print(liste[0])

# das zweite Element verändern
liste[1] = "New Text"

# Ein neues Element am Ende hinzufügen
einkaufswagen.append("Hose")
print(einkaufswagen)

# Eine Liste mit 1000 Nullen kreiern
liste2 = [0] * 1000
print(liste2)

# Eine Liste mit allen Werten 1 bis 100 (1er Schritte) kreiern
liste3 = list(range(1, 101))