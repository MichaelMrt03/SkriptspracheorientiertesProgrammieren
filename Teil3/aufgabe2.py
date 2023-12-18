import re
#Gesamtbetrag einer Bestellung berechnen
file_obj = open("Teil3/bestellung.txt")
gesamtpreis=0

for line in file_obj:
    #Anzahl rauslesen
    muster = r"\d{2}"
    ergebnis = re.search(muster,line)
    if ergebnis:
        anzahl = ergebnis.group()
        
    #Preis rauslesen
    muster = r"\d+\.\d{2}"
    ergebnis = re.search(muster,line) 
    if ergebnis:
        preis = ergebnis.group()
        gesamtpreis += float(preis)*int(anzahl) #Zeilenpreis drauf addieren zur Gesamtsumme
        
#Runden und ausgeben
gesamtpreis = round(gesamtpreis,2)
print("Der Gesamtpreis beträgt: "+str(gesamtpreis)+"€")
        
    
        