void setup() {
  // Starts serial communication. 9600 is the "speed" (baud rate).
  Serial.begin(115200); 
}

void loop() {
  int xVal = analogRead(A0); // Reads 0 to 1023
  int yVal = analogRead(A1);

  // LOGIC: We only send data if the stick moves past the "Deadzone"
  if (xVal < 300) Serial.println("LEFT");
  else if (xVal > 700) Serial.println("RIGHT");

  if (yVal < 300) Serial.println("UP");
  else if (yVal > 700) Serial.println("DOWN");

  // THE "TIME" FACTOR: 
  // Without this, the Arduino sends data too fast for Python to process.
  // 50ms is the "sweet spot" for responsiveness without lag.
  delay(10); 
}