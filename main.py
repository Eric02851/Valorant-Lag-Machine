#By Eric Still 7/15/2021

import pyautogui
from global_hotkeys import *
import time

resolution = pyautogui.size()
print(resolution)

is_alive = True

action = None

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1E-20

def loop():
    global action
    while action == True:
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.press('g')
        time.sleep(0.1)
    while action == False:
        pyautogui.press('f')

def buy():
    global action
    pyautogui.press('b')

    if resolution == (1920, 1080):
        pyautogui.moveTo(479, 314)
    if resolution == (2560, 1440):
        pyautogui.moveTo(639, 419)

    action = True

def pickup():
    global action
    action = False

def stop():
    global action
    action = None

def exit_application():
    global is_alive
    stop_checking_hotkeys()
    is_alive = False

bindings = [
    [["alt", "shift", "7"], None, buy],
    [["alt", "shift", "8"], None, pickup],
    [["alt", "shift", "9"], None, stop]
]

register_hotkeys(bindings)
start_checking_hotkeys()
while is_alive:
    loop()
    #time.sleep(0.001)

