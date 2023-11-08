matrix = [["X","0","X"],["X","0","X"],["X","0","X"]]
ausgabe=""
for i in range(3):
    if i!=0:
     ausgabe+="\n"
    for k in range(3):
     ausgabe +=" "+(matrix[i][k])
     
print(ausgabe)