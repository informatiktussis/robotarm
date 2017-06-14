from tkinter import *
from serial import *
import socket

root=Tk()
root.title("Roboterarm")
root.geometry("680x360")


connected = False

serialPort = "COM3"
baudRate=9600
ser = Serial(timeout=1., writeTimeout=0)
ser.port = serialPort
ser.baudrate = baudRate
ser.open()

sk= socket.socket()
sk.connect(('172.20.10.5', 30303))
sk.setblocking(False)

sk.send(b'Hello World\n')

addr = sk.accept()
print ('Got connection from', addr)
sk.setblocking(1) # Make it blocking.
connections.append( [c, addr] )

sk.recv(1024)


p=IntVar()

v=IntVar()

def on_press(event):
    print("Button is pressed.")
	
def on_release(event):
    print("Button is released.")

'''Buttons'''
	
def case_1(event):
    ser.write("a".encode("utf-8"))
	
def case_2(event):
    ser.write("b".encode("utf-8"))

def case_3(event):
    ser.write("c".encode("utf-8"))
	
def case_4(event):
    ser.write("d".encode("utf-8"))

def case_5(event):
    ser.write("e".encode("utf-8"))

def case_6(event):
    ser.write("f".encode("utf-8"))

def case_7(event):
    ser.write("g".encode("utf-8"))

def case_8(event):
    ser.write("h".encode("utf-8"))

def case_9(event):
    ser.write("i".encode("utf-8"))
	
def case_10(event):
    ser.write("j".encode("utf-8"))
	
def case_standard(event):
    ser.write("k".encode("utf-8"))
	
	
'''Geschwindigkeit'''
	
def case_schneller(event):
    ser.write("1".encode("utf-8"))
    print("w")

def case_schnell(event):
    ser.write("2".encode("utf-8"))
    print("e")
	
def case_mittelaf(event):
    ser.write("3".encode("utf-8"))
    print("bla")
	
def case_mittel(event):
    ser.write("4".encode("utf-8"))
 
def case_langsamer(event):
    ser.write("5".encode("utf-8"))
	
def case_langsam(event):
    ser.write("6".encode("utf-8"))
	

	


 
skizze= PhotoImage(file="skizze_neu.gif")
skizze2 = PhotoImage(file="skizze2_neu.gif")

w = Label(root, compound = CENTER, image=skizze).grid(row=0,column=0)
w = Label(root, compound = CENTER, image=skizze2).grid(row=4,column=0)

w = Label(root, text="Top", font = "Impact 18").place(x=170, y=10)
w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=73)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=135)


w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=210)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=280)

tempo = Label(root, text="Speed", font="Impact 15").place(x=520, y= 25) 

'''p = Scale(root, from_=5, to=20, length= 260, bd=0, orient=VERTICAL)#Funktionen
p.place(x=600, y=50)'''


h = Button(root, text="Open", bg="green", width=5, height=1, font="10", fg="white")
h.place(x=370, y=57)
h.bind("<ButtonPress>", case_7)
h.bind("<ButtonRelease>", case_standard) #case 7
i = Button(root, text="Close", bg="red", width=5, height=1, font="10", fg="black")
i.place(x=370,y=98) 
i.bind("<ButtonPress>", case_8)
i.bind("<ButtonRelease>", case_standard)#case 8

j = Button(root, text="↑", bg="white", font="Times 16", width=2, height=1)
j.place(x=270,y=10) 
j.bind("<ButtonPress>", case_6)
j.bind("<ButtonRelease>", case_standard)#case 5
k = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1)
k.place(x=320, y=10)
k.bind("<ButtonPress>", case_5)
k.bind("<ButtonRelease>", case_standard) #case 6

l = Button(root, text="↑", bg="White", font="Times 16", width=2, height=1)
l.place(x=270, y=73)
l.bind("<ButtonPress>", case_3)
l.bind("<ButtonRelease>", case_standard) #case 3
m = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1)
m.place(x=320, y=73)
m.bind("<ButtonPress>", case_4)
m.bind("<ButtonRelease>", case_standard) #case4

n = Button(root, text="←", bg="white", font="Times 16", width=2, height=1)
n.place(x=270, y=135)
n.bind("<ButtonPress>", case_2)
n.bind("<ButtonRelease>", case_standard) #case 2
o = Button(root, text="→", bg="white", font="Times 16", width=2, height=1)
o.place(x=320, y=135)
o.bind("<ButtonPress>", case_1)
o.bind("<ButtonRelease>", case_standard) #case 1

'''untere Buttons'''
a = Button(root, text="Open", bg="green", width=5, height=1, font="10", fg="white")
a.place(x=370, y=225)
a.bind("<ButtonPress>", case_7)
a.bind("<ButtonRelease>", case_standard) #case 7
b = Button(root, text="Close", bg="red", width=5, height=1, font="10", fg="black")
b.place(x=370,y=265)
b.bind("<ButtonPress>", case_8)
b.bind("<ButtonRelease>", case_standard) #case 8


c = Button(root, text="↑", bg="White", font="Times 16", width=2, height=1)
c.place(x=270, y=210)
c.bind("<ButtonPress>", case_9)
c.bind("<ButtonRelease>", case_standard) #case 9
d = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1)
d.place(x=320, y=210)
d.bind("<ButtonPress>", case_10)
d.bind("<ButtonRelease>", case_standard) #case 10

e = Button(root, text="←", bg="white", font="Times 16", width=2, height=1)
e.place(x=270, y=280) 
e.bind("<ButtonPress>", case_2)
e.bind("<ButtonRelease>", case_standard)#case2
f = Button(root, text="→", bg="white", font="Times 16", width=2, height=1)
f.place(x=320, y=280)
f.bind("<ButtonPress>", case_1)
f.bind("<ButtonRelease>", case_standard) #case 1



x=Radiobutton(root, text="Snail", font="Fixedsys 12", variable=p, value=1, command= lambda : case_langsam(None))
x.place(x=520,y=70)
q=Radiobutton(root, text="SuperSlow", font="Fixedsys 12", variable=p, value=2, command= lambda : case_langsamer(None)) 
q.place(x=520, y=110)
r=Radiobutton(root, text="Normal", font="Fixedsys 12", variable=p, value=3, command= lambda : case_mittel(None))  
r.place(x=520,y=150)
s=Radiobutton(root, text="SuperNormal", font="Fixedsys 12", variable=p, value=4, command= lambda : case_mittelaf(None))
s.place(x=520, y=190) 
t=Radiobutton(root, text="SuperSpeed", font="Fixedsys 12", variable=p, value=5, command= lambda : case_schnell(None))
t.place(x=520,y=230)
u=Radiobutton(root, text="Hyperspeed", font="Fixedsys 12", variable=p, value=6, command= lambda : case_schneller(None)) 
u.place(x=520, y=270)



root.mainloop()

