#By Eric Still 7/15/2021

import pyautogui
from global_hotkeys import *
import time

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1E-20

instructions = """

 /$$    /$$          /$$                                          /$$           /$$                                 /$$      /$$                     /$$       /$$                    
| $$   | $$         | $$                                         | $$          | $$                                | $$$    /$$$                    | $$      |__/                    
| $$   | $$ /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$        | $$        /$$$$$$   /$$$$$$       | $$$$  /$$$$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
|  $$ / $$/|____  $$| $$ /$$__  $$ /$$__  $$|____  $$| $$__  $$|_  $$_/        | $$       |____  $$ /$$__  $$      | $$ $$/$$ $$ |____  $$ /$$_____/| $$__  $$| $$| $$__  $$ /$$__  $$
 \  $$ $$/  /$$$$$$$| $$| $$  \ $$| $$  \__/ /$$$$$$$| $$  \ $$  | $$          | $$        /$$$$$$$| $$  \ $$      | $$  $$$| $$  /$$$$$$$| $$      | $$  \ $$| $$| $$  \ $$| $$$$$$$$
  \  $$$/  /$$__  $$| $$| $$  | $$| $$      /$$__  $$| $$  | $$  | $$ /$$      | $$       /$$__  $$| $$  | $$      | $$\  $ | $$ /$$__  $$| $$      | $$  | $$| $$| $$  | $$| $$_____/
   \  $/  |  $$$$$$$| $$|  $$$$$$/| $$     |  $$$$$$$| $$  | $$  |  $$$$/      | $$$$$$$$|  $$$$$$$|  $$$$$$$      | $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$  | $$| $$| $$  | $$|  $$$$$$$
    \_/    \_______/|__/ \______/ |__/      \_______/|__/  |__/   \___/        |________/ \_______/ \____  $$      |__/     |__/ \_______/ \_______/|__/  |__/|__/|__/  |__/ \_______/
                                                                                                    /$$  \ $$                                                                         
                                                                                                   |  $$$$$$/                                                                         
                                                                                                    \______/                                                                          

Usage and Keybinds:
1. alt + shift + 7
    Opens buy menue, then buys and drops shorties.

2. alt + shift + 8
    Spam clicks f to rapidly pick up shorties lagging the server.

3. alt + shift + 8
    Stops running action.
"""

resolution = pyautogui.size()
print(instructions)
print(resolution)

is_alive = True

action = None

def loop():
    global action
    while action == True:
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.press('g')
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

bindings = [
    [["alt", "shift", "7"], None, buy],
    [["alt", "shift", "8"], None, pickup],
    [["alt", "shift", "9"], None, stop]
]

register_hotkeys(bindings)
start_checking_hotkeys()
while is_alive:
    loop()