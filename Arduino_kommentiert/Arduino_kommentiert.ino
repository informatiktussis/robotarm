#include <Servo.h>
/** Servo.h ist eine Bibliothek, die benötigt wird,
   um die Servos zu steuern.
*/

#include <SoftwareSerial.h>
/** SoftwareSerial-Bibliothek*/
#include "DumbServer.h"
/** Verknüfung mit DumbServer.h*/

SoftwareSerial esp_serial(3, 2);
/** Das WLAN-Shield ist an Pin 2 und 3
 * Seriell mit dem Arduino verbunden
*/
EspServer esp_server;

/** servo1,2,3... als
 * Servo geklarieren. Später
 * werden die servos auch so angesprochen.
*/

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

/** Die Pins der Servos
*/

int servo_1pin = 8;
int servo_2pin = 9;
int servo_3pin = 10;
int servo_4pin = 11;

/** Geklaration mehrer Variablen*/

int python_button_var;
int speed_var = 15;

void setup() {
  Serial.begin(9600);
  esp_serial.begin(9600);

  /** Die Pins werden
   * dann mit dem servo1.attach(servo_pin)
   * Befehl als servo-pin geklariert.
   * Dies ist sehr ähnlich wie wenn eine
   * LED-pin gedefiniert mit pinMode(...,OUTPUT).
  */

  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  servo3.attach(servo_3pin);
  servo4.attach(servo_4pin);

  Serial.println("Starting server...");
  esp_server.begin(&esp_serial, "GDI", "password", 30303);
  Serial.println("...server is running");


  
  char ip[16];
  esp_server.my_ip(ip, 16);

  Serial.print("My ip: ");
  Serial.println(ip);

  /** Die IP-Adresse des WLAN-Shields wird seriell ausgegeben.*/

}

/** Ab hier beginnen die 4 Funktionen die später den Arm gewegen
   Führt man den Befehl servoname.write(winkel) bewegt man den servo auf
   einen bestimmten Winkel.
   Mit .read() liest man den Winkel aus in dem sich der jeweilige
   Servo gerade befindet.
   Als Parameter sind immer der Maximalwinkel und der Servoname, also welcher
   Servo angesprochen werden soll, angegeben. Dies erspart eine Menge schreibarbeit.
*/

void arm_hoch(int maximalwinkel, Servo *servoname ) {

  int var = servoname->read(); /** Der jeweilige Winkel des Servos wird in der Variable var gespeichert. */

  /** Da die servos auf 180° Grad mechanisch begrenzt sind kann ist hier
     eine if-Abfrage nötig, da sonst der Servomotor anfangen würde
     zu Brummen. Er darf also nicht weiter als 180° drehen.
  */
  if (var < maximalwinkel) {
    servoname->write(var + 1);
    delay(speed_var);
    /** Wenn der Winkel 180° noch nicht erreicht ist
       wird der Winkel mit write(nächster Winkel), also
       der Winkel+1 gesetzt.
       Der  Delay ist dazu da die Geschwindigkeit des Servos
       zu steuern. Wird die variable speed_var größer gewählt
       wird die Drehgeschwindigkeit langer, wird sie kleiner
       gewählt wird sie schneller, da die Funktion öfter pro
       Sekunde aufgerufen wird.
    */

  }
};

/** Für die Funktion arm_runter ist es genau das gleiche
   Prinzip wie für arm_hoch, nur dass der Winkel
   immer um -1 nach unten gesetzt wird, der Arm bewegt
   sich also in die andere Richtung.
*/

void arm_runter(int minimalwinkel, Servo *servoname ) {
  int var = servoname->read();

  /** Auch hier gibt es eine if-Abfrage ob diesesmal der Minimalwinkel
     erreicht wurde. In der Theorie dürfte der Servo bei 0° aufhören, jedoch
     hat es sich gezeigt dass bereits bei 11° die Begrezung auftritt, dies
     muss an  einer schlechten Qualität der Servos liegen.
  */

  if (var > minimalwinkel) {
    servoname->write(var - 1);
    delay(speed_var);

  }
};


/** Für die Spezialfunktionen werden zwei servos angesprochen.
   Dabei ist eigentlich nur die untige if-Abfrage in der Funktion
   selbst interessant, da der eine Winkel des Servos addiert wird,
   und der des anderen Subtrahiert.
*/

void spezial_funktion_hoch (int maximalwinkel, Servo *servoname, Servo *servoname2) {
  int var = servoname->read();
  int var2 = servoname2->read();

  if (var < maximalwinkel) {
    servoname->write(var + 1);
    servoname2->write(var2 + 1);
    delay(speed_var);
  }

}

/** Bei der untigen anderen spezial_funktion ist es der gegenteilige Fall */

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
  /** mit dieser if-Bedingung wird überprüft, ob
     eineneuer String durch die serielle
     Verbindung mit dem WLAN-Shield verfügbar ist.
  */
  if (esp_server.available()) {

    String command = esp_server.readStringUntil('\n');

    /** Ist eine neue verfügbar, wird der string in command
       gespeichert.
       Ab hier beginnt dann die umwandlung in einen Integer.
       Dies nötig da später cases Benutzt werden, wobei nur
       Integer als Vergleich benutzt werden können und keine Strings.

       Jeder gesendete String wird nun durch eine sehr lange if-Schleife
       einer passenden Zahl zugewiesen.
       Ist das Empfangene beispielsweise ein "a", so wird die Variable
       python_button_var auf 97 gesetzt, usw.
    */

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

  /** Da jetzt der gesendete String einem Integer zugewiesen worden ist
     kann einfach mit dem untenstehenden switch, der nur von der einen
     Variable python_button_var abgängig ist, der gesamte Arm gesteuert werden.

     Zur Wiederholung: Wenn ein "a" gesendet wurde, wird daraus eine 97 gemacht,
     und in der case 97 wird die Funktion arm_hoch(180, &servo1) aufgerufen.
     Dies bedeutet, dass sich servo1 nun nach oben bewegen würde und das gegen
     den Maximalwinkel 180°.
  */

  switch (python_button_var) {

    case 97: arm_hoch(180, &servo1);   break; //a
    case 98: arm_runter(11, &servo1);  break; //b

    case 99: arm_hoch(180, &servo2);   break; //c
    case 100: arm_runter(20, &servo2);  break; //d

    case 101: arm_hoch(180, &servo3);   break; //e
    case 102: arm_runter(11, &servo3);  break; //f

    case 103: arm_hoch(180, &servo4);   break; //g
    case 104: arm_runter(45, &servo4);  break; //h

    case 105: spezial_funktion_hoch(180, &servo2, &servo3); break; //i
    case 106: spezial_funktion_runter(20, &servo2, &servo3); break; //j

    /** Des weiten gibt es eine default-Case, die immer dann gesendet wird,
       wenn ein Button in der GUI losgelassen wird. Wird also ein "k" gesendet, dann
       ist das ein einfach der Befehl zum nichts tun.
    */

    case 107: break; /** default case :k */

    /** Für die cases 49 bis 54 wird die Geschwindigkeit der servos geändert.
       Dazu wird die variable speed_var einfach einen neuen Wert zugewiesen.
    */

    case 49: speed_var = 5; break;
    case 50: speed_var = 8;  break;
    case 51: speed_var = 11; break;
    case 52: speed_var = 14; break;
    case 53: speed_var = 17; break;
    case 54: speed_var = 20; break;
  }

}
