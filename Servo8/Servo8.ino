#include <Servo.h>
#include <SoftwareSerial.h>

#define ESP_SUCESS_READY ((char *)"ready\r\n")
#define ESP_SUCESS_OK ((char *)"OK\r\n")
#define ESP_SUCESS_PKG ((char *)"+IPD,")
#define ESP_SUCESS_IPQ ((char *)"+CIPSTA_CUR:ip:\"")
#define ESP_SUCESS_SENT ((char *)"SEND OK\r\n")

class EspClient : public Stream
{
private:
	Stream *_esp_serial;
	int connection_id;
	int rem_msg_len;

	void flush_in_buff();
	void reset();
	void connect_wifi(const char *ssid, const char* pwd);
	void setup_client(const char *host, uint16_t port);

public:
	EspClient(void);

	void begin(Stream *esp_serial, const char* ssid, const char *pass, const char *host, uint16_t port);
	void my_ip(char *buf, size_t buflen);
	bool connected();

	virtual int available();
	virtual int peek();
	virtual int read();
	virtual void flush();
	virtual size_t write(const uint8_t *buffer, size_t size);

	inline size_t write(uint8_t n) { return write(&n, 1); }
	inline size_t write(unsigned long n) { return write((uint8_t)n); }
	inline size_t write(long n) { return write((uint8_t)n); }
	inline size_t write(unsigned int n) { return write((uint8_t)n); }
	inline size_t write(int n) { return write((uint8_t)n); }

	using Print::write;
};

EspClient::EspClient(void)
{
	_esp_serial = NULL;
	connection_id = -1;
	rem_msg_len = 0;
}

void EspClient::begin(Stream *esp_serial, const char* ssid, const char *pass, const char *host, uint16_t port)
{
	_esp_serial = esp_serial;
	_esp_serial->setTimeout(60000);

	reset();
	connect_wifi(ssid, pass);
	setup_client(host, port);
}

void EspClient::flush_in_buff()
{
	while (_esp_serial->available()) {
		_esp_serial->read();
	}
}
void EspClient::reset()
{
	flush_in_buff();

	// Reset ESP
	_esp_serial->println("AT+RST");
	_esp_serial->find(ESP_SUCESS_READY);

	delay(500);

	// Disable command echo
	_esp_serial->println("ATE0");
	_esp_serial->find(ESP_SUCESS_OK);
}

void EspClient::connect_wifi(const char *ssid, const char* pwd)
{
	// Set station mode
	_esp_serial->println("AT+CWMODE_CUR=1");
	_esp_serial->find(ESP_SUCESS_OK);

	// Connect to AP
	_esp_serial->print("AT+CWJAP_CUR=\"");
	_esp_serial->print(ssid);
	_esp_serial->print("\",\"");
	_esp_serial->print(pwd);
	_esp_serial->println("\"");
	_esp_serial->find(ESP_SUCESS_OK);

	// Get an IP using DHCP
	_esp_serial->println("AT+CIFSR");
	_esp_serial->find(ESP_SUCESS_OK);
}

void EspClient::setup_client(const char *host, uint16_t port)
{
	/* Configure for multiple connections
	* (necessary to run as server) */
	_esp_serial->println("AT+CIPMUX=1");
	_esp_serial->find(ESP_SUCESS_OK);

	// Start listening for connections
	_esp_serial->print("AT+CIPSTART=0,\"TCP\",\"");
	_esp_serial->print(host);
	_esp_serial->print("\",");
	_esp_serial->println(port);

	connection_id = 0;

	_esp_serial->find(ESP_SUCESS_OK);
}

void EspClient::my_ip(char *buf, size_t buflen)
{
	_esp_serial->println("AT+CIPSTA_CUR?");
	_esp_serial->find(ESP_SUCESS_IPQ);

	memset(buf, 0, buflen);
	_esp_serial->readBytesUntil('"', buf, buflen - 1);

	_esp_serial->find(ESP_SUCESS_OK);
}

bool EspClient::connected()
{
	/* available() will, as a side-effect check if
	* the connection status changed */
	available();

	/* Return true if there is currently a
	* client connected */
	return(connection_id >= 0);
}

int EspClient::available()
{
	int ser_available = _esp_serial->available();

	if (rem_msg_len) {
		// There is a message in transit

		return(min(rem_msg_len, ser_available));
	}

	if (ser_available) {
		char bte = _esp_serial->peek();

		if (bte == '+') {
			char cmd[4];
			_esp_serial->readBytes(cmd, 4);

			int id = _esp_serial->parseInt();
			int len = _esp_serial->parseInt();

			_esp_serial->find((char *)":");

			if (id == connection_id) {
				rem_msg_len = len;
			}
		}
		else {
			_esp_serial->read();
		}
	}


	return(0);
}

int EspClient::peek()
{
	if (available()) {
		return(_esp_serial->peek());
	}
	else {
		return(-1);
	}
}

int EspClient::read()
{
	if (available()) {
		rem_msg_len -= 1;

		return(_esp_serial->read());
	}
	else {
		return(-1);
	}
}

void EspClient::flush()
{
	_esp_serial->flush();
}

size_t EspClient::write(const uint8_t *buffer, size_t size)
{
	while (!connected());

	_esp_serial->print("AT+CIPSEND=");
	_esp_serial->print(connection_id);
	_esp_serial->print(",");
	_esp_serial->println(size);

	_esp_serial->find((char *)">");

	_esp_serial->write(buffer, size);
	_esp_serial->find((char *)ESP_SUCESS_SENT);

	return(size);
}

/* The WiFi shield is connected to
* the Arduino pins 3 and 2, as the
* Arduino has only one hardware serial
* port (pins 0 and 1) we are using a
* serial port emulated in software. */
SoftwareSerial esp_serial(3, 2);
EspClient esp_client;

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
int speed_var_check;
int speed_var = 15;

//int var2 = 90;

void setup() {
	Serial.begin(9600);
	esp_serial.begin(9600);

  servo1.attach(servo_1pin);
  servo2.attach(servo_2pin);
  servo3.attach(servo_3pin);
  servo4.attach(servo_4pin);

  int angle = servo1.read();
  Serial.println(angle);
  servo2.write(50);

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);

  /* Connect to the wireless network with the name "GDI"
    and password "password", change these to match
    your wifi settings.

    If anything fails begin() will not return.

    To debug possible problems you can flash a second
    Arduino with the "Bare Minimum" example,
    connect the GNDs of the two Arduinos,
    connect pin 3 or 2 of the Arduino with the Wifi-shield
    to pin 1(TX) of the other Arduino and use the Serial monitor
    to see the Wifi commands and error-messages. */
  
  Serial.println("Starting client...");
  esp_client.begin(&esp_serial, "CJS", "Jinnyisthebest", "134.102.30.165", 30303);
  Serial.println("...client is running");

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
    //var2--;

    //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
    //Der "Gesamtwinkel" des Systems.
    delay(speed_var);


   // Serial.println(var + 1);

  }
  else {
    //var == 180;
  }
};

void arm_runter(int minimalwinkel, Servo *servoname ) {
  int var = servoname->read();

  if (var > minimalwinkel) {
    servoname->write(var - 1);
    //var2++;
    delay(speed_var);


   // Serial.println(var - 1);

  } else {
    //var = 11;
  }

};

void spezial_funktion_hoch (int maximalwinkel, Servo *servoname, Servo *servoname2) {
  int var = servoname->read();
  int var2 = servoname2->read();
  if (var < maximalwinkel) {
    servoname->write(var + 1);
    //var2--;
    //Alternativ: var2=180-var1; 180 kann auch eine Variable sein die man festlegen kann, das ist dann ja
    //Der "Gesamtwinkel" des Systems.
    delay(speed_var);

    servoname2->write(var2 + 1);

   // Serial.print(var2 + 1);
   // Serial.print(" ");
   // Serial.print(var + 1);
    //Serial.print(" ");
   // Serial.println(var + var2); //Die Summe beider sollte stets umgefähr konstant sein bei 180°.
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
    delay(speed_var);

    servoname2->write(var2 - 1);

   // Serial.print(var2 - 1);
   // Serial.print(" ");
   // Serial.print(var - 1);
   // Serial.print(" ");
   // Serial.println(var + var2);
  } else {
    //var = 11;
  }

}



void loop()
{ 
	/* Check if the python program
	* sent a new information - bearbeiten
	if (esp_client.available()) {
		int hue = esp_client.parseInt();

		int16_t intens_r = 255 - abs(hue - 255);
		int16_t intens_g = 255 - abs(hue - 511);
		int16_t intens_b = (hue > 300) ? (hue - 511) : (255 - hue);

		analogWrite(9, (intens_r > 0) ? intens_r : 0);
		analogWrite(10, (intens_g > 0) ? intens_g : 0);
		analogWrite(11, (intens_b > 0) ? intens_b : 0);
	}*/

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
/*
  if (Serial.available() > 0 ) {
    speed_var_check = Serial.read();
    Serial.println(speed_var_check);
  }

  switch (speed_var_check) {
    case 49: speed_var = 5;
    case 50: speed_var = 6;
    case 51: speed_var = 7;
    case 52: speed_var = 8;
    case 53: speed_var = 9;
    case 54: speed_var = 10;
    case 55: speed_var = 11;
    case 56: speed_var = 12;
    case 57: speed_var = 13;
    case 58: speed_var = 14;
    case 59: speed_var = 15;
    case 60: speed_var = 16;
    case 61: speed_var = 17;
    case 62: speed_var = 18;
    case 63: speed_var = 19;
    case 64: speed_var = 20;
  }
  */


  if (Serial.available() > 0) {
    python_button_var = Serial.read();
//Serial.println(python_button_var);
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



    case 49: speed_var = 5;
    case 50: speed_var = 8;
    case 51: speed_var = 11;
    case 52: speed_var = 14;
    case 53: speed_var = 17;
    case 54: speed_var = 20;
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
