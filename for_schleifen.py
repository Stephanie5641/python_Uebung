# Zahlen zwischen 0 und 6 inklusive ausdruckt.
for i in range(7):
    print(i) 

# Zahlen zwischen 3 und 8 ausdruckt.
for i in range(3, 9):
    print(i)

# Zahlen zwischen 2 und 30 inklusive (3er schritte) ausdruckt.
for i in range(2, 31, 3):
    print(i)

# Die liste soll 6 preise enthalten.
produktliste = [3.99, 49.59, 7.00, 6.95, 10.99, 18.78]

# Die produktliste mit einer while Schleife ausdrucken.
print(produktliste)
i = 0
laenge = len(produktliste)
while i  < laenge:
    print(produktliste[i])
    i = i + 1

for i in range(laenge):
    print(produktliste[i])


staedte = ["München", "Paris"]
laenge2 = len(staedte)
for i in range(laenge2):
    print(staedte[i])


laender = ["Frankreich", "Spanien", "Korea"]
for land in laender:
    print("meine lieblings laender sind", land)


