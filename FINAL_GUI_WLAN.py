#!/usr/bin/env python3
import tkinter as tk
import socket as so




class Arduino(object):
    def __init__(self, window, host, port, on_received):
        '''An abstraction for a network-connected Arduino.

        'window' is an instance of a TK root object,
        'host' and 'port' are the TCP network address of an Arduino,
        'on_received' is a function that is called whenever a line is
        received from the Arduino.
        '''
        
        self.window= window
        self.on_received= on_received

        # Open socket and connect to the Arduino
        self.socket= so.socket()
        self.socket.connect(('170.20.10.5', 30304))
        self.socket.setblocking(False)

        self.rd_buff= bytes()

        self._periodic_socket_check()

    def send_command(self, command):
        'Send a message to the Arduino'

        self.socket.send(command.encode('utf-8') + b'\n')

    def close(self):
        'Cleanly close the connection'

        self.socket.close()
        self.window.after_cancel(self.after_event)

    def _periodic_socket_check(self):
        try:
            msg= self.socket.recv(1024)

            if not msg:
                raise(IOError('Connection closed'))

            self.rd_buff+= msg

        except so.error:
            # In non-blocking mode an exception is thrown
            # whenever no data is available.
            # Which error is OS-dependant so we have to catch
            # the generic socket.error exception.

            pass

        while b'\n' in self.rd_buff:
            line, self.rd_buff= self.rd_buff.split(b'\n')

            line= line.decode('utf-8').strip()
            self.on_received(line)

        # Tell tkinter to call this function again
        # in 100ms
        self.after_event= self.window.after(
            100, self._periodic_socket_check
        )



class Bla(object):
    def __init__(self):
        self.setup_window()
        host= "170.20.10.5"
        port= 30304

        self.arduino= Arduino(
            self.window,
            host, int(port),
            self.on_received
        )

        self.setup_content()

        #self.a =tk.Button(window, text="Open", bg="green", width=5, height=1, font="10", fg="white", command= senden)
        #self.a.place(x=370, y=225)
    
    
    
    def setup_window(self):
        self.window=tk.Tk()
        self.window.title("Roboterarm")
        self.window.geometry("680x360")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.p=tk.IntVar()
        self.p.set(1)

    def on_close(self):
        self.arduino.close()
        self.window.destroy()
    
    def setup_content(self):

        
        self.h = tk.Button(self.window, text="Open", bg="green", width=5, height=1, font="10", fg="white")
        self.h.place(x=370, y=57)
        self.h.bind("<ButtonPress>", self.case_7)
        self.h.bind("<ButtonRelease>", self.case_standard) #case 7

        self.i =tk.Button(self.window, text="Close", bg="red", width=5, height=1, font="10", fg="black")
        self.i.place(x=370,y=98) 
        self.i.bind("<ButtonPress>", self.case_8)
        self.i.bind("<ButtonRelease>", self.case_standard)#self.case 8

        self.j =tk.Button(self.window, text="↑", bg="white", font="Times 16", width=2, height=1)
        self.j.place(x=270,y=10) 
        self.j.bind("<ButtonPress>", self.case_6)
        self.j.bind("<ButtonRelease>", self.case_standard)#self.case 5
        self.k =tk.Button(self.window, text="↓", bg="white", font="Times 16", width=2, height=1)
        self.k.place(x=320, y=10)
        self.k.bind("<ButtonPress>", self.case_5)
        self.k.bind("<ButtonRelease>", self.case_standard) #self.case 6

        self.l =tk.Button(self.window, text="↑", bg="White", font="Times 16", width=2, height=1)
        self.l.place(x=270, y=73)
        self.l.bind("<ButtonPress>", self.case_3)
        self.l.bind("<ButtonRelease>", self.case_standard) #self.case 3
        self.m =tk.Button(self.window, text="↓", bg="white", font="Times 16", width=2, height=1)
        self.m.place(x=320, y=73)
        self.m.bind("<ButtonPress>", self.case_4)
        self.m.bind("<ButtonRelease>", self.case_standard) #self.case4

        self.n =tk.Button(self.window, text="←", bg="white", font="Times 16", width=2, height=1)
        self.n.place(x=270, y=135)
        self.n.bind("<ButtonPress>", self.case_2)
        self.n.bind("<ButtonRelease>", self.case_standard) #self.case 2
        self.o =tk.Button(self.window, text="→", bg="white", font="Times 16", width=2, height=1)
        self.o.place(x=320, y=135)
        self.o.bind("<ButtonPress>", self.case_1)
        self.o.bind("<ButtonRelease>", self.case_standard) #self.case 1
#untere Buttons
        self.a =tk.Button(self.window, text="Open", bg="green", width=5, height=1, font="10", fg="white")
        self.a.place(x=370, y=225)
        self.a.bind("<ButtonPress>", self.case_7)
        self.a.bind("<ButtonRelease>", self.case_standard) #self.case 7
        self.b =tk.Button(self.window, text="Close", bg="red", width=5, height=1, font="10", fg="black")
        self.b.place(x=370,y=265)
        self.b.bind("<ButtonPress>", self.case_8)
        self.b.bind("<ButtonRelease>", self.case_standard) #self.case 8


        self.c =tk.Button(self.window, text="↑", bg="White", font="Times 16", width=2, height=1)
        self.c.place(x=270, y=210)
        self.c.bind("<ButtonPress>", self.case_9)
        self.c.bind("<ButtonRelease>", self.case_standard) #self.case 9
        self.d =tk.Button(self.window, text="↓", bg="white", font="Times 16", width=2, height=1)
        self.d.place(x=320, y=210)
        self.d.bind("<ButtonPress>", self.case_10)
        self.d.bind("<ButtonRelease>", self.case_standard) #self.case 10

        self.e =tk.Button(self.window, text="←", bg="white", font="Times 16", width=2, height=1)
        self.e.place(x=270, y=280) 
        self.e.bind("<ButtonPress>", self.case_2)
        self.e.bind("<ButtonRelease>", self.case_standard)#self.case2
        self.f =tk.Button(self.window, text="→", bg="white", font="Times 16", width=2, height=1)
        self.f.place(x=320, y=280)
        self.f.bind("<ButtonPress>", self.case_1)
        self.f.bind("<ButtonRelease>", self.case_standard) #self.case 1    
  
  
  
        self.x=tk.Radiobutton(self.window, text="Snail", font="Fixedsys 12", variable=self.p, value=1, command= lambda : self.case_langsam(None))
        self.x.place(x=520,y=70)
        self.q=tk.Radiobutton(self.window, text="SuperSlow", font="Fixedsys 12", variable=self.p, value=2, command= lambda : self.case_langsamer(None)) 
        self.q.place(x=520, y=110)
        self.r=tk.Radiobutton(self.window, text="Normal", font="Fixedsys 12", variable=self.p, value=4, command= lambda : self.case_mittel(None))  
        self.r.place(x=520,y=150)
        self.s=tk.Radiobutton(self.window, text="SuperNormal", font="Fixedsys 12", variable=self.p, value=5, command= lambda : self.case_mittelaf(None))
        self.s.place(x=520, y=190) 
        self.t=tk.Radiobutton(self.window, text="SuperSpeed", font="Fixedsys 12", variable=self.p, value=6, command= lambda : self.case_schnell(None))
        self.t.place(x=520,y=230)
        self.u=tk.Radiobutton(self.window, text="Hyperspeed", font="Fixedsys 12", variable=self.p, value=7, command= lambda : self.case_schneller(None)) 
        self.u.place(x=520, y=270)
        
        self.skizze= tk.PhotoImage(file="skizze_neu.gif")
        self.skizze2 = tk.PhotoImage(file="skizze2_neu.gif")
        
        self.w = tk.Label(self.window, image=self.skizze).grid(row=0,column=0)
        self.w = tk.Label(self.window, image=self.skizze2).grid(row=4,column=0)

        self.w = tk.Label(self.window, text="Top", font = "Impact 18").place(x=170, y=10)
        self.w = tk.Label(self.window, text="Middle", font = "Impact 18").place(x=170, y=73)
        self.w = tk.Label(self.window, text="Bottom", font = "Impact 18").place(x=170, y=135)


        self.w = tk.Label(self.window, text="Middle", font = "Impact 18").place(x=170, y=210)
        self.w = tk.Label(self.window, text="Bottom", font = "Impact 18").place(x=170, y=280)

        self.tempo = tk.Label(self.window, text="Speed", font="Impact 15").place(x=520, y= 25)
    
    
    
    
    
    
    
    
    
    
    
    
    
    def on_received(self):
        pass
    def senden(self):
        self.arduino.send_command('on')

    
    def case_1(self,event):
        self.arduino.send_command('a')
	
    def case_2(self,event):
        self.arduino.send_command('b')

    def case_3(self,event):
        self.arduino.send_command('c')
	
    def case_4(self,event):
        self.arduino.send_command('d')

    def case_5(self,event):
        self.arduino.send_command('e')

    def case_6(self,event):
        self.arduino.send_command('f')
    
    
    def case_7(self,event):
        self.arduino.send_command('g')
    def case_8(self,event):
        self.arduino.send_command('h')

    def case_9(self,event):
        self.arduino.send_command('i')
	
    def case_10(self,event):
        self.arduino.send_command('j')
    
    def case_standard(self,event):
        self.arduino.send_command('k')
    
    def case_schneller(self,event):
        self.arduino.send_command('1')

    def case_schnell(self,event):
        self.arduino.send_command('2')

    def case_mittelaf(self,event):
        self.arduino.send_command('3')
	
    def case_mittel(self,event):
        self.arduino.send_command('4')
 
    def case_langsamer(self,event):
        self.arduino.send_command('5')
	
    def case_langsam(self,event):
        self.arduino.send_command('6')
    def run(self):
        self.window.mainloop()
        
   

if __name__ == '__main__':
    window= Bla()
    window.run()