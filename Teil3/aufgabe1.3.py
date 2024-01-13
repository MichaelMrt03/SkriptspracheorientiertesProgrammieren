import re
#Ein Zeichen, das eine Ziffer oder ein Vorzeichen (also + oder ‐) ist
daten = "+"
muster = r"^[0-9,+-]$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
    print(ergebnis.group())
else:
    print("nicht gefunden")