import serial
ser = serial.Serial()
ser.port = 'COM33' #serial port auswählen
ser.baudrate = 9600 #Geschwindigkeit
ser.open() #serial port öffnen
while(True): #loop
    if(ser.inWaiting() > 0): #wenn Datai nicht gleich wie null ist
        ser.write(ser.read())#print it out