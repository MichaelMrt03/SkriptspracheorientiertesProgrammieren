import re
#Ein Zeichen, das kein Buchstabe ist
daten ="!"
muster = r"^[^A-z]$"
ergebnis = re.search(muster,daten)
if ergebnis:
    print("gefunden")
else:
    print("nicht gefunden")