#By Eric Still 7/15/2021

import pyautogui
from global_hotkeys import *
import time

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1E-30

resolution = pyautogui.size()

valorant = """
 /$$    /$$          /$$                                          /$$    
| $$   | $$         | $$                                         | $$    
| $$   | $$ /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$  
|  $$ / $$/|____  $$| $$ /$$__  $$ /$$__  $$|____  $$| $$__  $$|_  $$_/  
 \  $$ $$/  /$$$$$$$| $$| $$  \ $$| $$  \__/ /$$$$$$$| $$  \ $$  | $$    
  \  $$$/  /$$__  $$| $$| $$  | $$| $$      /$$__  $$| $$  | $$  | $$ /$$
   \  $/  |  $$$$$$$| $$|  $$$$$$/| $$     |  $$$$$$$| $$  | $$  |  $$$$/
    \_/    \_______/|__/ \______/ |__/      \_______/|__/  |__/   \___/  
"""
lag = """
 /$$                          
| $$                          
| $$        /$$$$$$   /$$$$$$ 
| $$       |____  $$ /$$__  $$
| $$        /$$$$$$$| $$  \ $$
| $$       /$$__  $$| $$  | $$
| $$$$$$$$|  $$$$$$$|  $$$$$$$
|________/ \_______/ \____  $$
                     /$$  \ $$
                    |  $$$$$$/
                     \______/ 
"""
machine = """
 /$$      /$$                     /$$       /$$                    
| $$$    /$$$                    | $$      |__/                    
| $$$$  /$$$$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ |____  $$ /$$_____/| $$__  $$| $$| $$__  $$ /$$__  $$
| $$  $$$| $$  /$$$$$$$| $$      | $$  \ $$| $$| $$  \ $$| $$$$$$$$
| $$\  $ | $$ /$$__  $$| $$      | $$  | $$| $$| $$  | $$| $$_____/
| $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$  | $$| $$| $$  | $$|  $$$$$$$
|__/     |__/ \_______/ \_______/|__/  |__/|__/|__/  |__/ \_______/                                                            
"""
instructions = """                                                                 
Usage and Keybinds:
alt + shift + 1
    Opens buy menue, then buys and drops shorties.

alt + shift + 2
    Spam clicks f to rapidly pick up shorties lagging the server.

alt + shift + 3
    Stops running action.
"""
print(valorant)
time.sleep(0.2)
print(lag)
time.sleep(0.2)
print(machine)
time.sleep(0.2)
print(instructions)
print(resolution)

is_alive = True

action = None

def loop():
    global action
    while action == True:
        pyautogui.click()
        pyautogui.press('g')
        time.sleep(0.15)
    while action == False:
        pyautogui.press('f')

def buy():
    global action
    pyautogui.press('b')
    time.sleep(0.1)

    if resolution == (1920, 1080):
        pyautogui.moveTo(479, 314)
    if resolution == (2560, 1440):
        pyautogui.moveTo(639, 419)

    time.sleep(0.1)
    action = True

def pickup():
    global action
    action = False

def stop():
    global action
    action = None

bindings = [
    [["alt", "shift", "1"], None, buy],
    [["alt", "shift", "2"], None, pickup],
    [["alt", "shift", "3"], None, stop]
]

register_hotkeys(bindings)
start_checking_hotkeys()
while is_alive:
    loop()
    if action == None:
        time.sleep(0.5)