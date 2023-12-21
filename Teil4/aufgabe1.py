from tkinter import *

main = Tk()

def berechneVerbrauch():
    km = eingabe1.get()
    liter = eingabe2.get()
    verbrauch = (float(liter)*100)/float(km) # Einheit: l/100km
    verbrauch = round(verbrauch,2)
    text3.configure(text="Der durschnittliche Verbrauch beträgt: "+str(verbrauch)+" L/100km")
    canvas.create_rectangle(x1+30,200,x2+30,200-(verbrauch*10),fill="blue")
    canvas.create_text(x1+80,200-(verbrauch*10),text=str(verbrauch))
    

text1 = Label(main,text="Geben Sie bitte die gefahrenen Kilometer ein:")
eingabe1 = Entry(main)
text2 = Label(main,text="Geben Sie bitte die getankten Liter ein:")
eingabe2 = Entry(main)
button = Button(main,text="Berechnen",command=berechneVerbrauch)
text3 = Label(main,text="Der durschnittliche Verbrauch beträgt: 0")

x1=50
x2=70
canvas = Canvas(main,width=150,height=200,bg="white")
canvas.create_rectangle(x1,130,x2,200,fill="green")
canvas.create_rectangle(x1,130,x2,100,fill="yellow")
canvas.create_rectangle(x1,100,x2,0,fill="red")
canvas.create_text(20,190,text="0 Liter")
canvas.create_text(20,130,text="7 Liter")
canvas.create_text(20,100,text="10 Liter")
canvas.create_text(20,10,text="20 Liter")

text1.pack()
eingabe1.pack()
text2.pack()
eingabe2.pack()
button.pack()
text3.pack()
canvas.pack()
mainloop()