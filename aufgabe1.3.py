import re
#Ein Zeichen, das eine Ziffer oder ein Vorzeichen (also + oder ‐) ist
daten = "+"
muster = r"^[1234567890+-]$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")