int led_high = 0 ;
int b = 0;
int blink = 0;

void setup(){
  pinMode(LED_BUILTIN,OUTPUT);
  digitalWrite(LED_BUILTIN,LOW);
  Serial.begin(9600);//set baud rate 

}

void loop(){
  if(Serial.available() > 0){// check for available data
   blink= Serial.parseInt(); // read the blinking time from the python code
   for (int i = 0; i< blink ; i++){
    digitalWrite(LED_BUILTIN,HIGH);//turn the LED on
    delay(1000);// wait for 1 second
    digitalWrite(LED_BUILTIN,LOW);// tirn the LED off
    delay(1000);// wait for 1 second
   }
   b = random(1, 10);
   Serial.println(b);

  }
  } 


