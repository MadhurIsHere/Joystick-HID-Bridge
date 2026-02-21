# Arduino Joystick Keyboard Bridge 🕹️⌨️

This project converts analog movements from an **Arduino Uno** joystick into digital keyboard keystrokes on a PC. Since standard Arduino Uno clones (CH340) do not support native HID (Human Interface Device) emulation, this project utilizes a **Python Bridge** to listen to high-speed serial data and trigger OS-level keyboard events.

---

## 🎓 Learning Objectives
This project is an excellent entry point for B.Tech students interested in **AIML** and **DevOps** because it touches on:
* **Embedded Logic:** Handling analog sensor data and signal thresholds.
* **Serial Communication:** Optimizing baud rates for real-time data transfer.
* **Automation:** Using Python to interface with the Operating System's input layer.

---

## 🛠️ Hardware Setup

### Components
* **Arduino Uno** (Official or CH340 Clone)
* **2-Axis Joystick Module** (KY-023)
* **Jumper Wires** (Female-to-Male)

### Wiring Diagram
| Joystick Pin | Arduino Pin | Purpose |
| :--- | :--- | :--- |
| **GND** | **GND** | Electrical Ground |
| **+5V** | **5V** | 5V Power Supply |
| **VRx** | **A0** | Horizontal Movement (Left/Right) |
| **VRy** | **A1** | Vertical Movement (Up/Down) |
| **SW** | **D2** | Optional Click Button |

---

## 🚀 Step-by-Step Implementation

### 1. Upload the Firmware
The Arduino reads the joystick's position and sends string commands over the USB cable. We use a baud rate of **115200** to eliminate input lag.

**File:** `firmware/joystick_firmware.ino`
```cpp
void setup() {
  Serial.begin(115200); 
}

void loop() {
  int xVal = analogRead(A0);
  int yVal = analogRead(A1);

  // Deadzone Logic: prevents "ghost" presses when the stick is centered
  if (xVal < 300) Serial.println("LEFT");
  else if (xVal > 700) Serial.println("RIGHT");

  if (yVal < 300) Serial.println("UP");
  else if (yVal > 700) Serial.println("DOWN");

  delay(10); // High polling rate for smooth gaming
}
```

2. Set Up the Python Bridge
The Python script listens to the serial port and "presses" the keys on your behalf.

Prerequisites:

```Bash
pip install pyserial pyautogui
```
Bridge Script (main.py):
```Python

import serial
import pyautogui
import time

# Optimization: Removes the default 0.1s delay in PyAutoGUI
pyautogui.PAUSE = 0

# Match your Arduino's COM port
try:
    ser = serial.Serial('COM9', 115200, timeout=0.01)
    print("Bridge is active!")
except:
    print("Error: Port busy or not found. Ensure Serial Monitor is closed.")

while True:
    if ser.in_waiting > 0:
        command = ser.readline().decode('utf-8').strip()
        if command in ["UP", "DOWN", "LEFT", "RIGHT"]:
            pyautogui.press(command.lower())
    time.sleep(0.001)
```
🚦 Troubleshooting
Access is denied: Ensure the Serial Monitor in the Arduino IDE is closed before running the Python script. Only one program can use the COM port at a time.

Laggy Movement: Verify that the baud rate in both the C++ code and Python script is set to 115200.

Python not responding: Ensure the window you want to control (like a game or browser) is the active window on your screen.

📁 Repository Structure<br>
Plaintext<br>
├── firmware/<br>
│   └── joystick_firmware.ino    # Arduino C++ Code<br>
│── main.py              # Python Bridge Script<br>
└── README.md                    # Project Documentation<br>
## Developed by: Madhur Rastogi<br>
