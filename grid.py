from serial import *
from tkinter import *

serialPort = "/dev/cu.usbmodem1421"
baudRate = 9600
ser = Serial(serialPort , baudRate, timeout=0, writeTimeout=0)

root = Tk()
root.title("Roboter Arm")
root.geometry("150x105")


def callback():
    print( "click!") # hier einzelne funktionen von dem was der servo machen soll
	#aufrufen von code in c - wegen der bibliothek 
	#um dann mit dem atuino programm ihn in python zu lesen
	
def fuck():
    print("MOTHERFUCKER!")

w = Label(root, text="Bottom")
w.grid(sticky=E)
w = Label(root, text="Middle")
w.grid(sticky=E)
w = Label(root, text="Top")
w.grid(sticky=E)



w = Button(root, text="Open", bg="green", fg="white", command=fuck)
w.grid(row=3, column=1)
w = Button(root, text="Close", bg="red", fg="black", command=fuck)
w.grid(row=3, column=2)

w = Button(root, text="←", bg="white", command=callback)
w.grid(row=2, column=1)
w = Button(root, text="→", bg="white", command=callback)
w.grid(row=2, column=2)

w = Button(root, text="↑", bg="White", command=callback)
w.grid(row=1, column=1)
w = Button(root, text="↓", bg="white",command=callback)
w.grid(row=1, column=2)

w = Button(root, text="←", bg="white", command=callback)
w.grid(row=0, column=1)
w = Button(root, text="→", bg="white", command=callback)
w.grid(row=0, column=2)

mainloop()
