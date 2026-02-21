void setup() {
  Serial.begin(115200); // one of the fastest baud rate(to minimize the lag)
}

void loop() {
  int xVal = analogRead(A0); // Reads 0 to 1023
  int yVal = analogRead(A1);

  
  if (xVal < 300) Serial.println("LEFT");
  else if (xVal > 700) Serial.println("RIGHT");

  if (yVal < 300) Serial.println("UP");
  else if (yVal > 700) Serial.println("DOWN");

 
  delay(10); // this decide lag
}
