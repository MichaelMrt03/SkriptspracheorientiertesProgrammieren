import re
#Ein Zeichen, das kein Buchstabe ist
daten ="!"
muster = r"^[^a-z]$"

ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")