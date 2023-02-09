import time
from threading import Thread

from pynput.keyboard import Controller as Keyboard
from pynput.mouse import Controller as Mouse

from pynput.keyboard import Key, Listener
from pynput.mouse import Button

keyboard = Keyboard()
mouse = Mouse()

def press(controller, key):
    controller.press(key)
    controller.release(key)

def click_combo():
    running: bool = True
    while running:
        s = 1
        press(mouse, Button.left)
        
        time.sleep(s)

def on_press(key):
    if (key == Key.enter):
        print("enter")
        clicker = Thread(target=click_combo)
        clicker.start()

    
    if (key == Key.esc):
        running: bool = False
        print("esc")

with Listener(on_press=on_press) as listener:
    listener.join()
