import re
#Eine (gültige) E‐Mail Adresse

daten ="test@gmail.com"
muster = r"^\w+@\w+\.\w+$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")