file_obj = open("Teil2/datenquelle.txt")
datensenke = open("Teil2/datensenke.txt","w")

print("In die Datensenke geschrieben:")
for line in file_obj:
    datensenke.write(str(float(line))+"\n")
    print(float(line))
file_obj.close()    
