import re
#2 Den Inhalt einer gesamten Python - Kommentarzeile
daten = "#python okok jajaj 1232131231"
muster = r"^.*"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")