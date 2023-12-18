import re
#Eine Textzeile mit genau drei Zeichen
daten = "d9!"
muster = r"^.{3}$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")
