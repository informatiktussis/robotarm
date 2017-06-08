from tkinter import *
from serial import *

root=Tk()
root.title("Roboterarm")
root.geometry("600x360")


connected = False

<<<<<<< HEAD
serialPort = "COM3"
=======
serialPort = "COM6"
>>>>>>> 7c263b1a8e3afdd81bd16cde857ebc0c68c8430f
baudRate=9600
ser = Serial(timeout=1, writeTimeout=0)
ser.port = serialPort
ser.baudrate = baudRate
ser.open()



v=IntVar()

def on_press(event):
    print("Button is pressed.")
	
def on_release(event):
    print("Button is released.")


def case_1():
    ser.write("a".encode("utf-8"))
	
def case_2():
    ser.write("b".encode("utf-8"))

def case_3():
    ser.write("c".encode("utf-8"))
	
def case_4():
    ser.write("d".encode("utf-8"))

def case_5():
    ser.write("e".encode("utf-8"))

def case_6():
    ser.write("f".encode("utf-8"))

def case_7():
    ser.write("g".encode("utf-8"))

def case_8():
    ser.write("h".encode("utf-8"))

def case_9():
    ser.write("i".encode("utf-8"))
	
def case_10():
    ser.write("j".encode("utf-8"))
	
'''test'''
def black():
 a.config(state=NORMAL) 
 a.config(state=NORMAL) 
 b.config(state=NORMAL)
 c.config(state=NORMAL)
 d.config(state=NORMAL)
 e.config(state=NORMAL)
 f.config(state=NORMAL)
 
 h.config(state = 'disabled')
 i.config(state = 'disabled')
 j.config(state = 'disabled')
 k.config(state = 'disabled')
 l.config(state = 'disabled') 
 m.config(state = 'disabled')
 n.config(state = 'disabled')
 o.config(state = 'disabled')
def normal():
 a.config(state='disabled') 
 b.config(state='disabled')
 c.config(state='disabled')
 d.config(state='disabled')
 e.config(state='disabled')
 f.config(state='disabled')
 
 h.config(state = NORMAL)
 i.config(state = NORMAL)
 j.config(state = NORMAL)
 k.config(state = NORMAL)
 l.config(state = NORMAL) 
 m.config(state = NORMAL)
 n.config(state = NORMAL)
 o.config(state = NORMAL)
 
skizze= PhotoImage(file="skizze.gif")
skizze2 = PhotoImage(file="skizze2.gif")

w = Label(root, compound = CENTER, image=skizze).grid(row=0,column=0)
w = Label(root, compound = CENTER, image=skizze2).grid(row=4,column=0)

w = Label(root, text="Top", font = "Impact 18").place(x=170, y=10)
w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=73)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=135)


w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=210)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=280)



h = Button(root, state=DISABLED, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=case_7)
h.place(x=370, y=57)
h.bind("<ButtonPress>", on_press)
h.bind("<ButtonRelease>", on_release) #case 7
i = Button(root, state=DISABLED, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=case_8)
i.place(x=370,y=98) 
i.bind("<ButtonPress>", on_press)
i.bind("<ButtonRelease>", on_release)#case 8

j = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=case_5)
j.place(x=270,y=10) 
j.bind("<ButtonPress>", on_press)
j.bind("<ButtonRelease>", on_release)#case 5
k = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=case_6)
k.place(x=320, y=10)
k.bind("<ButtonPress>", on_press)
k.bind("<ButtonRelease>", on_release) #case 6

l = Button(root, state=DISABLED, text="↑", bg="White", font="Times 16", width=2, height=1, command=case_3)
l.place(x=270, y=73)
l.bind("<ButtonPress>", on_press)
l.bind("<ButtonRelease>", on_release) #case 3
m = Button(root, state=DISABLED, text="↓", bg="white", font="Times 16", width=2, height=1, command=case_4)
m.place(x=320, y=73)
m.bind("<ButtonPress>", on_press)
m.bind("<ButtonRelease>", on_release) #case4

n = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=case_2)
n.place(x=270, y=135)
n.bind("<ButtonPress>", on_press)
n.bind("<ButtonRelease>", on_release) #case 2
o = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=case_1)
o.place(x=320, y=135)
o.bind("<ButtonPress>", on_press)
o.bind("<ButtonRelease>", on_release) #case 1

'''untere Buttons'''
a = Button(root, state=DISABLED, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=case_7)
a.place(x=370, y=225)
a.bind("<ButtonPress>", on_press)
a.bind("<ButtonRelease>", on_release) #case 7
b = Button(root, state=DISABLED, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=case_8)
b.place(x=370,y=265)
b.bind("<ButtonPress>", on_press)
b.bind("<ButtonRelease>", on_release) #case 8


c = Button(root, state=DISABLED, text="↑", bg="White", font="Times 16", width=2, height=1, command=case_9)
c.place(x=270, y=210)
c.bind("<ButtonPress>", on_press)
c.bind("<ButtonRelease>", on_release) #case 9
d = Button(root, state=DISABLED, text="↓", bg="white", font="Times 16", width=2, height=1, command=case_10)
d.place(x=320, y=210)
d.bind("<ButtonPress>", on_press)
d.bind("<ButtonRelease>", on_release) #case 10

e = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=case_2)
e.place(x=270, y=280) 
e.bind("<ButtonPress>", on_press)
e.bind("<ButtonRelease>", on_release)#case2
f = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=case_1)
f.place(x=320, y=280)
f.bind("<ButtonPress>", on_press)
f.bind("<ButtonRelease>", on_release) #case 1



Radiobutton(root, text="Manuell", font="Impact 14",  width = 15, variable=v, value=1, command=normal).place(x=450,y=83)   
Radiobutton(root, text="Automatisch", font="impact 14",  width = 15, variable=v, value=2, command=black).place(x=450, y=245) 


root.mainloop()

