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

void loop()
{



  while (digitalRead(button1) == 0) {
    int var = servo1.read();
    int var2 =servo2.read();
    if (var < 180) {
      servo1.write(var + 1);
      var2--;
     //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
     //Der "Gesamtwinkel" des Systems.
      delay(8);

      servo2.write(var2);
      
      Serial.print(var2);
      Serial.print(" ");
      Serial.print(var + 1);
      Serial.print(" ");
      Serial.println(var+var2);
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
      var2++;
      delay(8);

      servo2.write(var2);
      
      Serial.print(var2);
      Serial.print(" ");
      Serial.print(var - 1);
      Serial.print(" ");
      Serial.println(var+var2);
    } else {
      //var = 11;
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
