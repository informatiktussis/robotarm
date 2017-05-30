//OHNE SOFT SERIAL
#define PIN 12 
char *startup[]={"ATE0","AT+CWMODE=2","AT+CIPMUX=1",
                 "AT+CIPSERVER=1","AT+CIPSTATUS"};
void setup()
{pinMode(PIN,OUTPUT); Serial.begin(9600); 
 if(analogRead(A0)==0)
 {Serial.println("AT+RST");delay(2000);espReadLine(1000);}
 for(int i=0;i<5;i++)
 {Serial.println(startup[i]);espReadLine(0);}
}
 
char *espReadLine(int ms)
{char s[80]=""; //buffer
 if(ms)delay(ms);
 int len=Serial.readBytesUntil('\n',s,sizeof(s)-4); s[len]=0;
 return s;
}  

void loop()
{int id,len;char s[80]; 
 if(3==sscanf(espReadLine(0),"+IPD,%d,%d:%s",&id,&len,s))
 {digitalWrite(PIN,s[0]== '1'? HIGH : LOW); // OUTPUT    
  sprintf(s,"AT+CIPSEND=%d,12",id);// Message to id
  Serial.println(s);espReadLine(0);// +\r\n
  if(digitalRead(PIN))Serial.println("LED is ON "); 
                 else Serial.println("LED is OFF");
 }
}
