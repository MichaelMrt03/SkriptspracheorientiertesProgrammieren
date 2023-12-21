from tkinter import *

def move_up():
    global y
    y=y-5
    canvas.create_oval(x,y,x+5,y+5,fill="white")
    
def move_left():
        global x
        x=x-5
        canvas.create_oval(x,y,x+5,y+5,fill="white")
        
def move_right():
        global x
        x=x+5
        canvas.create_oval(x,y,x+5,y+5,fill="white")
        
def move_down():
        global y
        y=y+5
        canvas.create_oval(x,y,x+5,y+5,fill="white")

main = Tk()

main.geometry("300x300")
canvas = Canvas(main,width=200,height=200)
canvas.create_rectangle(0,0,200,200,fill="black")

x=97
y=103
canvas.create_oval(x,y,x+5,y+5,fill="white") #Startpunkt

button_up = Button(main,text="UP",command=move_up)
button_left = Button(main,text="LEFT",command=move_left)
button_right = Button(main,text="RIGHT",command=move_right)
button_down = Button(main,text="DOWN",command=move_down)

canvas.pack()
button_up.pack(side=TOP)
button_left.pack(side=LEFT)
button_right.pack(side=RIGHT)
button_down.pack(side=BOTTOM)


mainloop()