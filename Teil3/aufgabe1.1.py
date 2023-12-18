import re
#1. Das Wort "Python" oder "python" am Anfang einer Zeile
daten = "Python am Anfang"
muster = "^[Pp]ython"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")

