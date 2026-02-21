import serial
import pyautogui
import time

# Update the baud rate to match the Arduino (115200)
arduino = serial.Serial('COM9', 115200, timeout=0.01)

# PyAutoGUI has a default 0.1s delay after every action. 
# SET THIS TO ZERO to remove the built-in lag!
pyautogui.PAUSE = 0

print("System Active. Move the joystick")

while True:
    if arduino.in_waiting > 0:
        try:
            command = arduino.readline().decode("utf-8").strip()
            
            # Use 'press' but keep the logic fast
            if command == "LEFT":
                pyautogui.press('left')
            elif command == "RIGHT":
                pyautogui.press('right')
            elif command == "UP":
                pyautogui.press('up')
            elif command == "DOWN":
                pyautogui.press('down')
        except:
            continue # Ignore corrupted serial data
            
    # Keep this very small or remove it for maximum speed
    # time.sleep(0.001)