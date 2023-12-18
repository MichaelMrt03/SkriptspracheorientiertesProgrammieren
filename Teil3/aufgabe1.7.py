import re
# Ein Datum (z.B.: 11.4.2012 oder 03.02.2012 oder 01.02.12 )
daten = "01.02.12"
muster = r"^(0[1-9]|[1-2][0-9]|3[0-1])|\d{1}\.(0[1-9]|1[0-2])|\d{1}\.\d+$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")