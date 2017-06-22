import tkinter as tk     """GUI erstellt mit Tkinter"""
import socket as so      """Für eine WLAN Verbidung"""
   



class Arduino(object):
    def __init__(self, window, host, port, on_received):
        self.window= window
        self.on_received= on_received

        self.socket= so.socket()
        self.socket.connect(('170.20.10.5', 30304))    """Für die Verbindung mit dem WLAN Shield"""
        self.socket.setblocking(False)

        self.rd_buff= bytes()

        self._periodic_socket_check()

    def send_command(self, command):


        self.socket.send(command.encode('utf-8') + b'\n')

    def close(self):

        self.socket.close()                            """Damit die GUI geschlossen werden kann"""
        self.window.after_cancel(self.after_event)

    def _periodic_socket_check(self):
        try:
            msg= self.socket.recv(1024)

            if not msg:
                raise(IOError('Connection closed'))

            self.rd_buff+= msg

        except so.error:
            pass

        while b'\n' in self.rd_buff:
            line, self.rd_buff= self.rd_buff.split(b'\n')

            line= line.decode('utf-8').strip()
            self.on_received(line)

        self.after_event= self.window.after(
            100, self._periodic_socket_check
        )



class WLAN(object):
    def __init__(self):
        self.setup_window()
        #host= "170.20.10.5"
        #port= 30304

        self.arduino= Arduino(
            self.window,
            host, int(port),
            self.on_received
        )

        self.setup_content()

    
    
    
    def setup_window(self):
        self.window=tk.Tk()
        self.window.title("Roboterarm")
        self.window.geometry("680x360")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.p=tk.IntVar() 														"""RadioButton Variable"""
        self.p.set(1)

    def on_close(self):
        self.arduino.close()
        self.window.destroy()
    
    def setup_content(self):
""" Obere Buttons"""
        
        self.h = tk.Button(self.window, text="Open", bg="green", width=5, height=1, font="10", fg="white")
        self.h.place(x=370, y=57)                                                                              """Alle einzelnen Buttons werden mit einem genauen Ort zugeordnet"""
        self.h.bind("<ButtonPress>", self.case_7)                                                              """Der Button bekommt die Funktion case_7"""
        self.h.bind("<ButtonRelease>", self.case_standard)                                                     """Wenn der Button aufgehört wird zu druücken, soll die Funktion case_standard aktiviert werden, soddass beim Arduino Programm nichts mehr ausgeführt werden kann"""
        self.i =tk.Button(self.window, text="Close", bg="red", width=5, height=1, font="10", fg="black")
        self.i.place(x=370,y=98) 
        self.i.bind("<ButtonPress>", self.case_8)
        self.i.bind("<ButtonRelease>", self.case_standard)

        self.j =tk.Button(self.window, text="↑", bg="white", font="Times 16", width=2, height=1)
        self.j.place(x=270,y=10) 
        self.j.bind("<ButtonPress>", self.case_6)
        self.j.bind("<ButtonRelease>", self.case_standard)
        self.k =tk.Button(self.window, text="↓", bg="white", font="Times 16", width=2, height=1)
        self.k.place(x=320, y=10)
        self.k.bind("<ButtonPress>", self.case_5)
        self.k.bind("<ButtonRelease>", self.case_standard

        self.l =tk.Button(self.window, text="↑", bg="White", font="Times 16", width=2, height=1)
        self.l.place(x=270, y=73)
        self.l.bind("<ButtonPress>", self.case_3)
        self.l.bind("<ButtonRelease>", self.case_standard)
        self.m =tk.Button(self.window, text="↓", bg="white", font="Times 16", width=2, height=1)
        self.m.place(x=320, y=73)
        self.m.bind("<ButtonPress>", self.case_4)
        self.m.bind("<ButtonRelease>", self.case_standard) 

        self.n =tk.Button(self.window, text="←", bg="white", font="Times 16", width=2, height=1)
        self.n.place(x=270, y=135)
        self.n.bind("<ButtonPress>", self.case_2)
        self.n.bind("<ButtonRelease>", self.case_standard)
        self.o =tk.Button(self.window, text="→", bg="white", font="Times 16", width=2, height=1)
        self.o.place(x=320, y=135)
        self.o.bind("<ButtonPress>", self.case_1)
        self.o.bind("<ButtonRelease>", self.case_standard)

		"""untere Buttons"""
		
        self.a =tk.Button(self.window, text="Open", bg="green", width=5, height=1, font="10", fg="white")
        self.a.place(x=370, y=225)
        self.a.bind("<ButtonPress>", self.case_7)
        self.a.bind("<ButtonRelease>", self.case_standard)
        self.b =tk.Button(self.window, text="Close", bg="red", width=5, height=1, font="10", fg="black")
        self.b.place(x=370,y=265)
        self.b.bind("<ButtonPress>", self.case_8)
        self.b.bind("<ButtonRelease>", self.case_standard)

        self.c =tk.Button(self.window, text="↑", bg="White", font="Times 16", width=2, height=1)
        self.c.place(x=270, y=210)
        self.c.bind("<ButtonPress>", self.case_9)
        self.c.bind("<ButtonRelease>", self.case_standard)
        self.d =tk.Button(self.window, text="↓", bg="white", font="Times 16", width=2, height=1)
        self.d.place(x=320, y=210)
        self.d.bind("<ButtonPress>", self.case_10)
        self.d.bind("<ButtonRelease>", self.case_standard)

        self.e =tk.Button(self.window, text="←", bg="white", font="Times 16", width=2, height=1)
        self.e.place(x=270, y=280) 
        self.e.bind("<ButtonPress>", self.case_2)
        self.e.bind("<ButtonRelease>", self.case_standard)
        self.f =tk.Button(self.window, text="→", bg="white", font="Times 16", width=2, height=1)
        self.f.place(x=320, y=280)
        self.f.bind("<ButtonPress>", self.case_1)
        self.f.bind("<ButtonRelease>", self.case_standard)     
  
  """Radiobuttons für die Geschwindigkeit"""
  
        self.x=tk.Radiobutton(self.window, text="Snail", font="Fixedsys 12", variable=self.p, value=1, command= lambda : self.case_langsam(None))      """Variable P, damit wird deklariert das die Radiobuttons zusammen gehören."""
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
        
        self.w = tk.Label(self.window, image=self.skizze).grid(row=0,column=0)                      """Die Bilder wurden in einer Matrix angeordnet, damit man sich danach richten kann."""
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
        self.arduino.send_command('a')  """Hier werden die einzelnen Cases aus dem Arduino ausgeführt.
										   Das ist Case 97."""
    def case_2(self,event):
        self.arduino.send_command('b')  """Case 98"""

    def case_3(self,event):
        self.arduino.send_command('c')  """Case 99"""
	
    def case_4(self,event):
        self.arduino.send_command('d')  """Case 100"""

    def case_5(self,event):
        self.arduino.send_command('e')  """Case 101"""

    def case_6(self,event):
        self.arduino.send_command('f')  """Case 102"""
    
    def case_7(self,event):
        self.arduino.send_command('g')  """Case 103"""
		
    def case_8(self,event):
        self.arduino.send_command('h')  """Case 104"""

    def case_9(self,event):
        self.arduino.send_command('i')  """Case 105"""
	
    def case_10(self,event):
        self.arduino.send_command('j')  """Case 106"""
    
    def case_standard(self,event):
        self.arduino.send_command('k')  """Case 107 - Default Case"""
    
    def case_schneller(self,event):
        self.arduino.send_command('1')  """RadioButton Funktionen, welche die Geschwindigkeit rüber senden. Case 49"""

    def case_schnell(self,event):
        self.arduino.send_command('2')  """Case 50"""

    def case_mittelaf(self,event):
        self.arduino.send_command('3')  """Case 51"""
	
    def case_mittel(self,event):
        self.arduino.send_command('4')  """Case 52"""
 
    def case_langsamer(self,event):
        self.arduino.send_command('5')  """Case 53"""
	
    def case_langsam(self,event):
        self.arduino.send_command('6')  """Case 54"""
		
    def run(self):
        self.window.mainloop()          """Dafür das die GUI die ganze Zeit geöffnet bleibt und sich nicht einfach schließt."""
        
   

if __name__ == '__main__':
    window= WLAN()
    window.run()