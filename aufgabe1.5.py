import re
# eine IP-Adresse(nicht auf 255 begrenzt, muss 3 Ziffern haben pro Segment)
daten ="46.123.112.231"
muster = r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}$"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")