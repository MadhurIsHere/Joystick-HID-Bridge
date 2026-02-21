import serial
import pyautogui
import time


arduino = serial.Serial('COM9', 115200, timeout=0.01)

pyautogui.PAUSE = 0

print("System Active. Move the joystick")

while True:
    if arduino.in_waiting > 0:
        try:
            command = arduino.readline().decode("utf-8").strip()
            
            
            if command == "LEFT":
                pyautogui.press('left')
            elif command == "RIGHT":
                pyautogui.press('right')
            elif command == "UP":
                pyautogui.press('up')
            elif command == "DOWN":
                pyautogui.press('down')
        except:
            continue 
            
