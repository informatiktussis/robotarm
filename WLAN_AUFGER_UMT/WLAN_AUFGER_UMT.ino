#include <Servo.h>
#include <SoftwareSerial.h>
#include "DumbServer.h"

SoftwareSerial esp_serial(3, 2);
EspServer esp_server;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

int servo_1pin = 8;
int servo_2pin = 9;
int servo_3pin = 10;
int servo_4pin = 11;

int python_button_var;
int speed_var_check;
int speed_var = 15;

void setup() {
  Serial.begin(9600);
  esp_serial.begin(9600);

  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  servo3.attach(servo_3pin);
  servo4.attach(servo_4pin);

  Serial.println("Starting server...");
  esp_server.begin(&esp_serial, "GDI", "password", 30303);
  Serial.println("...server is running");


  /* Get and print the IP-Address the python program
     should connect to */
  char ip[16];
  esp_server.my_ip(ip, 16);

  Serial.print("My ip: ");
  Serial.println(ip);

}

void arm_hoch(int maximalwinkel, Servo *servoname ) {
  int var = servoname->read();
  
  if (var < maximalwinkel) {
    servoname->write(var + 1);
    delay(speed_var);

  }
};

void arm_runter(int minimalwinkel, Servo *servoname ) {
  int var = servoname->read();
  
  if (var > minimalwinkel) {
    servoname->write(var - 1);
    delay(speed_var);

   }  
};

void spezial_funktion_hoch (int maximalwinkel, Servo *servoname, Servo *servoname2) {
  int var = servoname->read();
  int var2 = servoname2->read();
  
  if (var < maximalwinkel) {
    servoname->write(var + 1);
    servoname2->write(var2 + 1);
    delay(speed_var);
  }
 
}

void spezial_funktion_runter (int minimalwinkel, Servo *servoname, Servo *servoname2) {
  int var = servoname->read();
  int var2 = servoname2->read();

  if (var > minimalwinkel) {
    servoname->write(var - 1);
    servoname2->write(var2 - 1);
    delay(speed_var);
  }

}

void loop()
{ 
  // Check if the python program sent commands
  if (esp_server.available()) {
    // Read one line of commands
    String command = esp_server.readStringUntil('\n');
    Serial.println(command);

    if (command == "a") {
      python_button_var = 97;
    }
    else if (command == "b") {
      python_button_var = 98;
    }
    else if (command == "c") {
      python_button_var = 99;
    }
    else if (command == "d") {
      python_button_var = 100;
    }
    else if (command == "e") {
      python_button_var = 101;
    }
    else if (command == "f") {
      python_button_var = 102;
    }
    else if (command == "g") {
      python_button_var = 103;
    }
    else if (command == "h") {
      python_button_var = 104;
    }
    else if (command == "i") {
      python_button_var = 105;
    }
    else if (command == "j") {
      python_button_var = 106;
    }
    else if (command == "k") {
      python_button_var = 107;
    }
    else if (command == "1") {
      python_button_var = 49;
    }
    else if (command == "2") {
      python_button_var = 50;
    }
    else if (command == "3") {
      python_button_var = 51;
    }
    else if (command == "4") {
      python_button_var = 52;
    }
    else if (command == "5") {
      python_button_var = 53;
    }
    else if (command == "6") {
      python_button_var = 54;
    }
}

   switch (python_button_var) {

      case 97: arm_hoch(180, &servo1);   break; //a
      case 98: arm_runter(11, &servo1);  break; //b

      case 99: arm_hoch(180, &servo2);   break; //c
      case 100: arm_runter(11, &servo2);  break; //d

      case 101: arm_hoch(180, &servo3);   break; //e
      case 102: arm_runter(11, &servo3);  break; //f

      case 103: arm_hoch(180, &servo4);   break; //g
      case 104: arm_runter(11, &servo4);  break; //h

      case 105: spezial_funktion_hoch(180, &servo2, &servo3); break; //i
      case 106: spezial_funktion_runter(11, &servo2, &servo3); break; //j

      case 107: break; //default case //k

      case 49: speed_var = 5; break;
      case 50: speed_var = 8;  break;
      case 51: speed_var = 11; break;
      case 52: speed_var = 14; break;
      case 53: speed_var = 17; break;
      case 54: speed_var = 20; break;
    }

}
