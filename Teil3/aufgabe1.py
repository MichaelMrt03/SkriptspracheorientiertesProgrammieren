import re

#1. Das Wort "Python" oder "python" am Anfang einer Zeile
"""
daten = "Python am Anfang"
muster = "^[Pp]ython"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")
"""
#2 Den Inhalt einer gesamten Python - Kommentarzeile
daten = "#Das ist mein Beispielkommentar in Python"
muster = r"^#\s*[^#\n]*$"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")