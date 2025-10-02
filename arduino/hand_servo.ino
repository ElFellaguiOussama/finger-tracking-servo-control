#include <Servo.h>

Servo myServo;
String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  myServo.attach(11);
}

void loop() {
  if (stringComplete) {
    int angle = inputString.toInt();
    angle = constrain(angle, 0, 180);
    myServo.write(angle);
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}