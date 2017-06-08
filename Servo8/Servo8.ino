#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;


int servo_1pin = 8;
int servo_2pin = 9;
int servo_3pin = 10;
int servo_4pin = 11;

int button1 = 3;
int button2 = 4;


int python_button_var;

//int var2 = 90;

void setup() {
  Serial.begin(9600);

  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  servo3.attach(servo_3pin);
  servo4.attach(servo_4pin);
  
  int angle = servo1.read();
  Serial.println(angle);
  servo2.write(50);

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);

}


  
void arm_hoch(int maximalwinkel, Servo *servoname ) { 
    int var = servoname->read();
    if (var < maximalwinkel) {
      servoname->write(var + 1);
      //var2--;
   
     //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
     //Der "Gesamtwinkel" des Systems.
      delay(8); 
          
     
      Serial.println(var + 1);
     
    }
    else {
      //var == 180;
    }
};
    
void arm_runter(int minimalwinkel, Servo *servoname ){
     int var = servoname->read();
    
      if (var > minimalwinkel) {
      servoname->write(var - 1);
      //var2++;
      delay(8);

    
      Serial.println(var - 1);
    
    } else {
      //var = 11;
    }
  
};

void spezial_funktion_hoch (int maximalwinkel, Servo *servoname, Servo *servoname2) {
    int var = servoname->read();
    int var2 =servoname2->read();
    if (var < maximalwinkel) {
      servoname->write(var + 1);
      //var2--;
     //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
     //Der "Gesamtwinkel" des Systems.
      delay(15);

      servoname2->write(var2 +1);
      
      Serial.print(var2 +1);
      Serial.print(" ");
      Serial.print(var + 1);
      Serial.print(" ");
      Serial.println(var+var2); //Die Summe beider sollte stets umgefähr konstant sein bei 180°.
    }
    else {
      //var == 180;
    }
  }

void spezial_funktion_runter (int minimalwinkel, Servo *servoname, Servo *servoname2) {
    int var = servoname->read();
    int var2 = servoname2->read();

    if (var > minimalwinkel) {
      servoname->write(var - 1);
      //var2++;
      delay(15);

      servoname2->write(var2 - 1);
      
      Serial.print(var2 - 1);
      Serial.print(" ");
      Serial.print(var - 1);
      Serial.print(" ");
      Serial.println(var+var2);
    } else {
      //var = 11;
    }
  
}



void loop()
{
/*
  while (digitalRead(button1) == 0) {
    int var = servo1.read();
    int var2 =servo2.read();
    if (var < 180) {
      servo1.write(var + 1);
      //var2--;
     //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
     //Der "Gesamtwinkel" des Systems.
      delay(15);

      servo2.write(var2 +1);
      
      Serial.print(var2 +1);
      Serial.print(" ");
      Serial.print(var + 1);
      Serial.print(" ");
      Serial.println(var+var2); //Die Summe beider sollte stets umgefähr konstant sein bei 180°.
    }
    else {
      //var == 180;
    }
  }


  while (digitalRead(button2) == 0) {
    int var = servo1.read();
    int var2 = servo2.read();

    if (var > 11) {
      servo1.write(var - 1);
      //var2++;
      delay(15);

      servo2.write(var2 - 1);
      
      Serial.print(var2 - 1);
      Serial.print(" ");
      Serial.print(var - 1);
      Serial.print(" ");
      Serial.println(var+var2);
    } else {
      //var = 11;
    }

  }
*/

switch(python_button_var) {

case 1: arm_hoch(180, &servo1);   break;
case 2: arm_runter(11, &servo1);  break;

case 3: arm_hoch(180, &servo2);   break;
case 4: arm_runter(11, &servo2);  break;

case 5: arm_hoch(180, &servo3);   break;
case 6: arm_runter(11, &servo3);  break;

case 7: arm_hoch(180, &servo4);   break;
case 8: arm_runter(11, &servo4);  break;

case 9: spezial_funktion_hoch(180, &servo2, &servo3); break;
case 10: spezial_funktion_runter(11, &servo2, &servo3); break; 

}







while (digitalRead(button1) == 0) {
arm_hoch(180, &servo1);
  
}
while (digitalRead(button2) == 0) {

  arm_runter(110, &servo1);
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
