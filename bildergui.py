from tkinter import *
from serial import *

root=Tk()
root.title("Roboterarm")
root.geometry("600x360")


connected = False

serialPort = "COM7"
baudRate=9600
ser = Serial(timeout=1, writeTimeout=0)
ser.port = serialPort
ser.baudrate = baudRate
ser.open()



v=IntVar()


def case_1():
    ser.write("a".encode("utf-8"))
  # ser.write(51)
  # print(ser.write("3".encode("utf-8")))
##
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
 
skizze= PhotoImage(file="C:/Users/Waleriya/Desktop/Projekt/robotarm/skizze.gif")
skizze2 = PhotoImage(file="C:/Users/Waleriya/Desktop/Projekt/robotarm/skizze2.gif")

w = Label(root, compound = CENTER, image=skizze).grid(row=0,column=0)
w = Label(root, compound = CENTER, image=skizze2).grid(row=4,column=0)

w = Label(root, text="Top", font = "Impact 18").place(x=170, y=10)
w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=73)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=135)


w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=210)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=280)



h = Button(root, state=DISABLED, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=case_7)
h.place(x=370, y=57) #case 7
i = Button(root, state=DISABLED, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=case_8)
i.place(x=370,y=98) #case 8

j = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=case_5)
j.place(x=270,y=10) #case 5
k = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=case_6)
k.place(x=320, y=10) #case 6

l = Button(root, state=DISABLED, text="↑", bg="White", font="Times 16", width=2, height=1, command=case_3)
l.place(x=270, y=73) #case 3
m = Button(root, state=DISABLED, text="↓", bg="white", font="Times 16", width=2, height=1, command=case_4)
m.place(x=320, y=73) #case4

n = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=case_2)
n.place(x=270, y=135) #case 2
o = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=case_1)
o.place(x=320, y=135) #case 1

'''untere Buttons'''
a = Button(root, state=DISABLED, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=case_7)
a.place(x=370, y=225) #case 7
b = Button(root, state=DISABLED, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=case_8)
b.place(x=370,y=265) #case 8


c = Button(root, state=DISABLED, text="↑", bg="White", font="Times 16", width=2, height=1, command=case_9)
c.place(x=270, y=210) #case 9
d = Button(root, state=DISABLED, text="↓", bg="white", font="Times 16", width=2, height=1, command=case_10)
d.place(x=320, y=210) #case 10

e = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=case_2)
e.place(x=270, y=280) #case2
f = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=case_1)
f.place(x=320, y=280) #case 1



Radiobutton(root, text="Manuell", font="Impact 14",  width = 15, variable=v, value=1, command=normal).place(x=430,y=83)   
Radiobutton(root, text="Automatisch", font="impact 14",  width = 15, variable=v, value=2, command=black).place(x=430, y=245) 


root.mainloop()

