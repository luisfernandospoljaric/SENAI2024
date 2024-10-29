import pyautogui
import time

print("Tecla enter será acionada")
time.sleep(1)

try:
    while True:
        pyautogui.press('enter')
        time.sleep(0.00000000001)
except KeyboardInterrupt:
    print("Deu excessão")