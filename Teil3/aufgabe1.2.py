import re
#2 Den Inhalt einer gesamten Python - Kommentarzeile
daten = "#Das ist mein Beispielkommentar in Python"
muster = r"^#\s*[^#\n]*$"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")