#include <Servo.h>

Servo servo1;
Servo servo2;


int angle = 20;

int servo_1pin = 8;
int servo_2pin = 9;

int button1 = 3;
int button2 = 4;

void setup() {
Serial.begin(9600);
  
  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  
  servo1.write(angle);

pinMode(button1, INPUT_PULLUP);
pinMode(button2, INPUT_PULLUP);
}

void loop() 
{ 



while(digitalRead(button1) == 0){
int var = servo1.read();

if (var < 180) {
  servo1.write(var+1);
 
delay(15);
Serial.println(var+1);}
else {
  var == 180;
}
}


while(digitalRead(button2) == 0){
  int var = servo1.read();



  if (var > 11){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}



  /*
 // scan from 0 to 180 degrees
  for(angle = 10; angle < 180; angle++)  
  {                                  
    servo.write(angle);               
    delay(15);                   
  } 
  // now scan back from 180 to 0 degrees
  for(angle = 180; angle > 10; angle--)    
  {                                
    servo.write(angle);           
    delay(15);       
  } */
} 
