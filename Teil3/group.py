import re
daten = "12345abcd"
muster = r"([1-5]+)([a-d])+"
ergebnis = re.search(muster,daten)
if(ergebnis):
    print("gefunden")
    print(ergebnis.group(1))
else:
    print("nicht gefunden")