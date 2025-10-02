# Finger Tracking Servo Control

Control a servo motor with just your fingers! ✋➡️⚙️  
This project uses Python (with OpenCV and MediaPipe) to track the distance between your fingers in real-time.  
The measured distance (in pixels) is sent over serial to an Arduino, which converts it into a PWM signal to control a servo motor.

---

## 🔧 Features
- Real-time hand/finger tracking using Python + OpenCV + MediaPipe.
- Serial communication between PC and Arduino.
- Maps finger distance to servo position (0°–180°).
- Demonstrates cross-platform integration of computer vision + embedded systems.

## 🚀 Getting Started

### 1. Requirements (Python)
- Python 3.8+
- Install dependencies:
  ```bash
  pip install opencv-python mediapipe pyserial

### 2. Run the python script
    cd python
    python hand_tracking.py

### 3. Upload Arduino code

- Open arduino/hand_servo.ino in Arduino IDE.
- Select your board (e.g., Arduino Uno).
- Upload the sketch.

### 4. Connect and test

- Python will send the finger distance (in pixels) over Serial.
- Arduino reads this distance and maps it to a PWM duty cycle.
- Servo rotates according to your finger distance.