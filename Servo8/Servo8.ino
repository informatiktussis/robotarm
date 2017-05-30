#include <Servo.h>

Servo servo1; //Servo numero uno
Servo servo2; // "    numero dos
Servo servo3; // "    nummeo tres
Servo servo4; // "    numero quadro

int test;

int angle = 20;

int servo_1pin = 8;
int servo_2pin = 9;

int button1 = 3;
int button2 = 4;
int button3 = 5;
int button4 = 6;
int button5 = 7;
int button6 = 10;
int button7 = 11;
int button8 = 12;

int grenze = 102; //Grenze

void setup() {
Serial.begin(9600);  
  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  servo1.write(angle);
pinMode(button1, INPUT_PULLUP);
pinMode(button2, INPUT_PULLUP);
}

void loop() { 
  
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
if (var > grenze){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}

while(digitalRead(button3) == 0){
int var = servo1.read();

if (var < 180) {
  servo1.write(var+1);
 
delay(15);
Serial.println(var+1);}
else {
  var == 180;
}

}
while(digitalRead(button4) == 0){
  int var = servo1.read();
if (var > grenze){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}
while(digitalRead(button5) == 0){
  int var = servo1.read();
if (var > grenze){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}

while(digitalRead(button6) == 0){
  int var = servo1.read();
if (var > grenze){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}

while(digitalRead(button7) == 0){
  int var = servo1.read();
if (var > grenze){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}

while(digitalRead(button8) == 0){
  int var = servo1.read();
if (var > grenze){
  servo1.write(var-1);
 delay(15);
  
 Serial.println(var-1);
  }else{
    var = 11;
   }

}





} 
