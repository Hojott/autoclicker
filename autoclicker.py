#!/usr/bin/env python3
# Autoclicker that can use keyboard and mouse

import time
from threading import Thread

from pynput.keyboard import Controller as Keyboard
from pynput.mouse import Controller as Mouse

from pynput.keyboard import Key, Listener
from pynput.mouse import Button


class Clicker:
    """ Automatic clicker, starts with Enter and pauses with Esc
    """
    def __init__(self):
        self.running: bool = False
        self.keyboard = Keyboard()
        self.mouse = Mouse()

    def press_key(self, controller, key):
        """ Takes in the controller (keyboard or mouse) and key to press
        """
        controller.press(key)
        controller.release(key)

    def click_combo(self):
        """ Edit to change keys to press and sleep time
        """
        while self.running:
            sleep = 1

            self.press_key(self.mouse, Button.left)

            time.sleep(sleep)

    def listen(self, key):
        """ Listens to keyboard presses
        """
        if (key == Key.enter):
            self.running = True
            t = Thread(target=self.click_combo, name=clicker)
            t.start()
            print("Started")

    
        if (key == Key.esc):
            self.running = False
            print("Paused")

if __name__ == '__main__':
    clicker = Clicker()
    with Listener(on_press=clicker.listen) as listener:
        listener.join()
