#include <SoftwareSerial.h>

#define SSID "iPhone von Jisoo" // wifi name, test
#define PASS "1029384756" // wifi password
#define DST_IP "143.248.5.153" // destination_IP

SoftwareSerial Serial2(2,3); // make RX Arduino line is pin 2, make TX Arduino line is pin 3.
                             // This means that you need to connect the TX line from the esp to the Arduino's pin 2
                             // and the RX line from the esp to the Arduino's pin 3
                             // ESP8266 (rxPin, txPin)
 

void setup()
{
  // Open Serial1 communications and wait for port to open:

  Serial2.begin(9600);
  Serial2.setTimeout(5000);
  Serial.begin(9600); //can't be faster than 19200 for softSerial1
  Serial.println("ESP8266 Demo");
  
  //test if the module is ready
  Serial2.println("AT+RST");
  delay(2000);
  if(Serial2.find("ready")){
    Serial.println("Module is ready");
    }
  else{
    Serial.println("Module has no response.");
    while(1);
  }

  delay(1000);


  //connect to the wifi
  boolean connected=false;
  for(int i=0;i<5;i++){
    if(connectWiFi()){
      connected = true;
      break;
    }
  }
  
  if (!connected){  // if the internet isn't connected, repeat it.
    while(1);
    }
  
  delay(5000);
  
  //set the single connection mode
  Serial2.println("AT+CIPMUX=0");  // Set multiple connection =0
}

 
void loop()
{
  String cmd = "AT+CIPSTART=\"TCP\",\"*server IP Adress*";  // TCP connection
  cmd += DST_IP;
  cmd += "\",80";
  
  Serial2.println(cmd);
  Serial.println(cmd);
  
  if(Serial2.find("Error")) return;
  
  cmd = "GET / HTTP/1.0\r\n\r\n";
  Serial2.print("AT+CIPSEND=");   // length of the HTTP request messege
  Serial2.println(cmd.length());
  
  if(Serial2.find(">")) {
    Serial.print(">");}
  else {
    Serial2.println("AT+CIPCLOSE"); // Close TCP or UDP connection
    Serial.println("connect timeout");
    delay(1000);
    
    return;
   }
    
  Serial2.print(cmd);
  delay(2000);

  //Serial1.find("+IPD"); // Serial finds received data 
  while (Serial2.available()) {
    char c = Serial2.read();
    Serial.write(c);
    
    if(c=='\r') Serial.print('\n');
  }
  
  delay(1000);
  
  while (Serial2.available()) {
    char c = Serial2.read();
    Serial.write(c);
    
    if(c=='\r') Serial2.print('\n');
    }
    
  Serial.println("====");
  delay(1000);
}

boolean connectWiFi() {
  Serial2.println("AT+CWMODE=1"); // wifi mode = STA
  String cmd="AT+CWJAP=\""; // join the AP = <ssid>, <pwd>
  
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  
  Serial.println(cmd);
  Serial2.println(cmd);
  delay(2000);
  
  if(Serial2.find("OK")){
    Serial.println("OK, Connected to WiFi.");
    
    return true;
    } 
  else{
    Serial.println("Cannot connect to the WiFi.");
    return false;
    }
}
