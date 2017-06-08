from tkinter import *
from serial import *

root=Tk()
root.title("Roboterarm")
root.geometry("600x360")


connected = False
ser = serial.Serial("COM7", 9600)
ser = Serial(serialPort, baudRate, timeout=0, writeTimeout=0)


while(True): #loop
    if(ser.inWaiting() > 0): #wenn Datai nicht gleich wie null ist
        ser.write(ser.read())#print it out
		''' switchfunktion einordnen '''
		
## loop until the arduino tells us it is ready
while not connected:
    serin = ser.read()
    connected = True


v=IntVar()
variable = 0

class servo:

def switchVariable(self, python_button_var):
    self.python_button_var = python_button_var
    global variable
    variable = self.python_button_var
    print(python_button_var) #ser.read
>>>>>>> da701e57f6b998465e7c89be03af9115d04bf958
	
	
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



h = Button(root, state=DISABLED, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=lambda *args: switchVariable(7))
h.place(x=370, y=57) #case 7
i = Button(root, state=DISABLED, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=lambda *args: switchVariable(8))
i.place(x=370,y=98) #case 8

j = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(5))
j.place(x=270,y=10) #case 5
k = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(6))
k.place(x=320, y=10) #case 6

l = Button(root, state=DISABLED, text="↑", bg="White", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(3))
l.place(x=270, y=73) #case 3
m = Button(root, state=DISABLED, text="↓", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(4))
m.place(x=320, y=73) #case4

n = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(2))
n.place(x=270, y=135) #case 2
o = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(1))
o.place(x=320, y=135) #case 1

'''untere Buttons'''
a = Button(root, state=DISABLED, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=lambda *args: switchVariable(7))
a.place(x=370, y=225) #case 7
b = Button(root, state=DISABLED, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=lambda *args: switchVariable(8))
b.place(x=370,y=265) #case 8


c = Button(root, state=DISABLED, text="↑", bg="White", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(9))
c.place(x=270, y=210) #case 9
d = Button(root, state=DISABLED, text="↓", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(10))
d.place(x=320, y=210) #case 10

e = Button(root, state=DISABLED, text="←", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(2))
e.place(x=270, y=280) #case2
f = Button(root, state=DISABLED, text="→", bg="white", font="Times 16", width=2, height=1, command=lambda *args: switchVariable(1))
f.place(x=320, y=280) #case 1



Radiobutton(root, text="Manuell", font="Impact 14",  width = 15, variable=v, value=1, command=normal).place(x=430,y=83)   
Radiobutton(root, text="Automatisch", font="impact 14",  width = 15, variable=v, value=2, command=black).place(x=430, y=245) 

int(ser.write(switchVariable(python_button_var)))

root.mainloop()

