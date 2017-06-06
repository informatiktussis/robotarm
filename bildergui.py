from tkinter import *

root=Tk()
root.title("Roboterarm")
root.geometry("600x360")

v=IntVar()

def callback():
    print( "click!") # hier einzelne funktionen von dem was der servo machen soll
	#aufrufen von code in c - wegen der bibliothek 
	#um dann mit dem atuino programm ihn in python zu lesen
	
def fuck():
    print("MOTHERFUCKER!")

skizze= PhotoImage(file="C:/Users/Waleriya/Desktop/skizze.gif")
skizze2 = PhotoImage(file="C:/Users/Waleriya/Desktop/skizze2.gif")

w = Label(root, compound = CENTER, image=skizze).grid(row=0,column=0)
w = Label(root, compound = CENTER, image=skizze2).grid(row=4,column=0)

w = Label(root, text="Top", font = "Impact 18").place(x=170, y=10)
w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=73)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=135)


w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=210)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=280)



w = Button(root, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=fuck).place(x=370, y=57)
w = Button(root, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=fuck).place(x=370,y=98)

w = Button(root, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=fuck).place(x=370, y=225)
w = Button(root, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=fuck).place(x=370,y=265)

w = Button(root, text="←", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=270,y=10)
w = Button(root, text="→", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=320, y=10)

w = Button(root, text="↑", bg="White", font="Times 16", width=2, height=1, command=callback).place(x=270, y=73)
w = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=320, y=73)

w = Button(root, text="←", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=270, y=135)
w = Button(root, text="→", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=320, y=135)

w = Button(root, text="↑", bg="White", font="Times 16", width=2, height=1, command=callback).place(x=270, y=210)
w = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=320, y=210)

w = Button(root, text="←", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=270, y=280)
w = Button(root, text="→", bg="white", font="Times 16", width=2, height=1, command=callback).place(x=320, y=280)

Radiobutton(root, text="Manuell", font="Impact 14", variable=v, value=1).place(x=430,y=83)
Radiobutton(root, text="Automatisch", font="impact 14", variable=v, value=2).place(x=430, y=245)

root.mainloop()

