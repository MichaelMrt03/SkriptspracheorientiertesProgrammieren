#Erstellen Sie bitte ein Programm zur Bearbeitung einer Protokolldatei über Telefongespräche.
#Anstelle der gesamten Telefonnummer soll „xxxx.xxxx“ sichtbar sein.
#Die modifizierten Einträge werden in einer neuen Datei gespeichert.
import re
file_obj = open("Teil3/Log.txt")
log_zensiert = open("Teil3/Log_zensiert.txt","w") #a-> append w->write(überschreibt/neue Datei) r->read
muster = r"(\d{4}\/\d+)"
ersatz = "xxxx.xxxx"

for line in file_obj:
    ergebnis = re.sub(muster,ersatz,line) #zensieren
    ergebnis = ergebnis.strip()
    if ergebnis:
        print(ergebnis)
        #In Datei schreiben
        log_zensiert.write(ergebnis+"\n")
        