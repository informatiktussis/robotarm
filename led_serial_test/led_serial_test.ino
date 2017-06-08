int test;
int led = 13;
int led_2 = 12;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(led_2, OUTPUT);
  //Serial.write(1);

}

void loop(){
  if (Serial.available() > 0) {
    test = Serial.read();
    Serial.println(test);}
     
    if (test == 97) {
      digitalWrite(led, HIGH);
        } else{digitalWrite(led, LOW);}
  
    
 if (test == 98) {
      digitalWrite(led_2, HIGH);
    } else {digitalWrite(led_2, LOW);}
    

 }

