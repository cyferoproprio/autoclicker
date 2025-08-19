import pyautogui
import time
import keyboard

time.sleep(5)
while True:
    if keyboard.is_pressed('q'):  # pressione 'q' para parar
        break
    pyautogui.click()
    time.sleep(1)
