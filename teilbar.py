
# Eine funktion erstellen die ermittelt ob eine zahl gerade oder geungrade ist.
def gerade_oder_ungerade(zahl):
    rest = zahl % 2
    if rest == 0:
        print("gerade")
    else:
        print("ungerade")

gerade_oder_ungerade(9)
gerade_oder_ungerade(15)

# Ob eine zahl durch drei teilbar ist.
def durch_drei_teilbar_oder_nicht(zahl):
    rest = zahl % 3
    if rest == 0:
        print("durch drei teilbar")
    else:
        print("nicht teilbar")

durch_drei_teilbar_oder_nicht(15)



