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
	
'''test'''
def black():
 a.config(state=NORMAL) #funktioniert noch nciht 
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
 a.config(state='disabled') #funktioniert noch nciht 
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
 
skizze= PhotoImage(file="C:/Users/Waleriya/Desktop/skizze.gif")
skizze2 = PhotoImage(file="C:/Users/Waleriya/Desktop/skizze2.gif")

w = Label(root, compound = CENTER, image=skizze).grid(row=0,column=0)
w = Label(root, compound = CENTER, image=skizze2).grid(row=4,column=0)

w = Label(root, text="Top", font = "Impact 18").place(x=170, y=10)
w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=73)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=135)


w = Label(root, text="Middle", font = "Impact 18").place(x=170, y=210)
w = Label(root, text="Bottom", font = "Impact 18").place(x=170, y=280)



h = Button(root, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=fuck)
h.place(x=370, y=57) #case 7
i = Button(root, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=fuck)
i.place(x=370,y=98) #case 8

j = Button(root, text="←", bg="white", font="Times 16", width=2, height=1, command=callback)
j.place(x=270,y=10) #case 5
k = Button(root, text="→", bg="white", font="Times 16", width=2, height=1, command=callback)
k.place(x=320, y=10) #case 6

l = Button(root, text="↑", bg="White", font="Times 16", width=2, height=1, command=callback)
l.place(x=270, y=73) #case 3
m = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1, command=callback)
m.place(x=320, y=73) #case4

n = Button(root, text="←", bg="white", font="Times 16", width=2, height=1, command=callback)
n.place(x=270, y=135) #case 2
o = Button(root, text="→", bg="white", font="Times 16", width=2, height=1, command=callback)
o.place(x=320, y=135) #case 1

'''untere Buttons'''
a = Button(root, text="Open", bg="green", width=5, height=1, font="10", fg="white", command=fuck)
a.place(x=370, y=225) #case 7
b = Button(root, text="Close", bg="red", width=5, height=1, font="10", fg="black", command=fuck)
b.place(x=370,y=265) #case 8


c = Button(root, text="↑", bg="White", font="Times 16", width=2, height=1, command=callback)
c.place(x=270, y=210) #case 9
d = Button(root, text="↓", bg="white", font="Times 16", width=2, height=1, command=callback)
d.place(x=320, y=210) #case 10

e = Button(root, text="←", bg="white", font="Times 16", width=2, height=1, command=callback)
e.place(x=270, y=280) #case2
f = Button(root, text="→", bg="white", font="Times 16", width=2, height=1, command=callback)
f.place(x=320, y=280) #case 1


Radiobutton(root, text="Manuell", font="Impact 14",  width = 15, variable=v, value=1, command=normal).place(x=430,y=83)    #wenn diese aktiviert ist, dann sollen die unteren buttons nicht mehr gehen
Radiobutton(root, text="Automatisch", font="impact 14",  width = 15, variable=v, value=2, command=black).place(x=430, y=245) #wenn dieses aktiviert ist sollen oberen buttons nicht mehr gehen
# mit command state=disable
root.mainloop()

