print("Bitte wählen:")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")
auswahl = input("(1/2/3/4)")
auswahl = int(auswahl)
zahl1 = input("Bitte Zahl1 eingeben: ")
zahl1 = float(zahl1)
zahl2 = input("Bitte Zahl2 eingeben: ")
zahl2 = float(zahl2)

def addition(zahl1,zahl2):
    print(zahl1+zahl2)

def subtraktion(zahl1,zahl2):
    print(zahl1-zahl2)
    
def multiplikation(zahl1,zahl2):
    print(zahl1*zahl2)
    
def division(zahl1,zahl2):
    if zahl2!=0:
     print(zahl1/zahl2)
    else: print("Man kann nicht durch Null teilen!")

    
    
if auswahl==1:
    addition(zahl1,zahl2)
elif auswahl==2:
    subtraktion(zahl1,zahl2)
elif auswahl==3:
    multiplikation(zahl1,zahl2)
elif auswahl==4:
    division(zahl1,zahl2)