import re
# eine Festnetznummer mit je einem Stern davor und danach (*Vorwahl/Nummer*)
daten = "*02904/123456789*"
muster = r"^\*\d{5}\/\d{9}\*$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")