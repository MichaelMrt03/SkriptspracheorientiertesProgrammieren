import kreis

radius = float(input("Bitte Radius eingeben: "))

flaeche = kreis.berechne_flaeche(radius)
umfang = kreis.berechne_umfang(radius)

print("flaeche: "+str(flaeche))
print("Umfang: "+str(umfang))