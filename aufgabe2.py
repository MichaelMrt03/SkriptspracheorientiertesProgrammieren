endwert = input("Bitte Anzahl an Zahlen eingeben:")
endwert = int(endwert)

def fib(endwert):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(endwert):
        fibzahl = a+b
        a=b
        b=fibzahl
        print (fibzahl)
    
fib(endwert)

    