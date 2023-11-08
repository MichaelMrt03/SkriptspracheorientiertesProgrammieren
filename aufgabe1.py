temp_in_C = input("Wie viel viel Grad in °C ist es?")

def temp_umrechner(temp_in_C):
    return (float(temp_in_C)*1.8 +32)

temp_in_F = temp_umrechner(temp_in_C)

print("Die Temperatur in F beträgt:" + str(temp_in_F))


    
