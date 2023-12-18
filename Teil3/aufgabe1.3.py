import re
#Ein Zeichen, das eine Ziffer oder ein Vorzeichen (also + oder ‐) ist
daten = "9"
muster = r"^[0-9,+-]$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")