from tkinter import *
root = Tk()

#root.title("Roboterarm")

from serial import*

serialPort = "COM6"
baudRate=9600
ser = Serial(timeout=1, writeTimeout=0)
ser.port = serialPort
ser.baudrate = baudRate
ser.open()

connected = False






#while not connected:
 #   serin = ser.read()
#    connected = True

counter=3

#if ser.read() ==  0:
 #   ser.read()

def change_text():
    global counter
    counter -=1
    button.config(text="Click "+str(counter))
    if counter==0:
        root.destroy()
    root.after(1000,change_text)

def led_1():
    ser.write("a".encode("utf-8"))
  # ser.write(51)
  # print(ser.write("3".encode("utf-8")))
##
def led_2():
    ser.write("b".encode("utf-8"))

def led_3():
    ser.write("c".encode("utf-8"))
    
#ser.write(52)
    #print(ser.write(4))

zangelabel = Label(root, text="Zange:")
zangelabel.grid(row=0,column=0)

zange= Button(root, text="led_1", command=led_1)
zange.grid(row=0,column=1)

zange2 = Button(root, text="led_2", command=led_2)
zange2.grid(row=0,column=2)

obenlabel = Label(root, text="Oben:")
obenlabel.grid(row=1,column=0)

oben = Button(root, text='Up', command=root.destroy)
oben.grid(row=1,column=1)

oben2 = Button(root, text='Down', command=root.destroy)
oben2.grid(row=1,column=2)

mittelabel = Label(root, text="Mitte:")
mittelabel.grid(row=2,column=0)

mitte = Button(root, text='Up', command=root.destroy)
mitte.grid(row=2,column=1)

mitte2 = Button(root, text='Down', command=root.destroy)
mitte2.grid(row=2,column=2)

untenlabel = Label(root, text="Unten:")
untenlabel.grid(row=3,column=0)

unten = Button(root, text='Up', command=root.destroy)
unten.grid(row=3,column=1)

unten2 = Button(root, text='Down', command=root.destroy)
unten2.grid(row=3,column=2)



root.mainloop()