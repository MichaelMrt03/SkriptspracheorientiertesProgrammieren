import re
#Eine negative Zahl mit 4 Nachkommastellen
daten = "-234.3134"
muster = r"^-\d+(\,|\.)\d{4}$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")