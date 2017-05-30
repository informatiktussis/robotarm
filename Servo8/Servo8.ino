#include <Servo.h>

Servo servo1;
Servo servo2;

int servo_1pin = 8;
int servo_2pin = 9;

int button1 = 3;
int button2 = 4;

//int var2 = 90;

void setup() {
  Serial.begin(9600);

  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  int angle = servo1.read();
  Serial.println(angle);
  //bservo1.write(angle);

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);


  
}
/*
struct servos {
char* servonamen
};

struct servos servodaten[4] = { 
  {.servonamen= "servo_1"}, 
  {.servonamen= "servo_2"},
  {.servonamen= "servo_3"},
  {.servonamen= "servo_4"},
}; */

//servos *Zeiger = &servonamen;
  
void arm_hoch(int maximalwinkel, char servoname ) { 
    int var = servoname.read();
    if (var < maximalwinkel) {
      myString.write(var + 1);
      //var2--;
   
     //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
     //Der "Gesamtwinkel" des Systems.
      delay(8); 
          
      Serial.print(" ");
      Serial.print(var + 1);
      Serial.print(" ");      
    }
    else {
      //var == 180;
    }
};
    
void arm_runter(int minimalwinkel, char dieser_servo){
     int var = dieser_servo.read();
    
      if (var > minimalwinkel) {
      dieser_servo2.write(var - 1);
      //var2++;
      delay(8);

      Serial.print(" ");
      Serial.print(var - 1);
      Serial.print(" ");
    } else {
      //var = 11;
    }
  
};

void loop()
{

  while (digitalRead(button1) == 0) {
    int var = servo1.read();
    int var2 =servo2.read();
    if (var < 180) {
      servo1.write(var + 1);
      //var2--;
     //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
     //Der "Gesamtwinkel" des Systems.
      delay(8);

      servo2.write(var2 -1);
      
      Serial.print(var2 -1);
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
      delay(8);

      servo2.write(var2 + 1);
      
      Serial.print(var2 + 1);
      Serial.print(" ");
      Serial.print(var - 1);
      Serial.print(" ");
      Serial.println(var+var2);
    } else {
      //var = 11;
    }

  }


switch(python_button_var) {
  case 1: arm_hoch(180, servo1); break;
  case 2: arm_runter(11, servo1); break;
  case 3: arm_runter(11); break;
  default: printf("a ist irgendwas\n"); break;
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
