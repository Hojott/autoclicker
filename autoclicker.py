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
    def __init__(self, startpause: tuple):
        self._start = startpause[0]
        self._pause = startpause[1]

        self._running: bool = False
        self.keyboard = Keyboard()
        self.mouse = Mouse()


    def press_key(self, controller, key):
        """ Takes in the controller (keyboard or mouse) and key to press
        """
        controller.press(key)
        controller.release(key)

    def autoclick(self, sleep: float, controller, keys: tuple, shift=False):
        """ Takes in controller: keyboard/mouse and a tuple of keys to press
        """
        while self.running:
            if shift:
                with self.keyboard.pressed(Key.shift):
                    for key in keys:
                        self.press_key(controller, key)
            
            else:
                for key in keys:
                    self.press_key(controller, key)

            time.sleep(sleep)

    def click_thread(self, sleep, controller, keys: list, shift=False):
        t = Thread(target=self.autoclick, args=[sleep, controller, keys, shift])
        t.start()

    def automove(self, sleep: float, amount: tuple):
        """ Moves cursor
        """
        while self.running:
            self.mouse.move(amount[0], amount[1])
            time.sleep(sleep)
    
    def move_thread(self, sleep, amount):
        t = Thread(target=self.automove, args=[sleep, amount])
        t.start()

    def listen(self, key):
        """ Listens to keyboard presses of self.start and -stop
        """
        if (key == self.start):
            self.running = True
            #self.move_thread(0.01, (0, -50))
            self.click_thread(0.05, self.mouse, (Button.left,))
            print("Started")

        if (key == self.pause):
            self.running = False
            print("Paused")

    def listen_keyboard(self):
        """ Listens to keyboard
        """
        with Listener(on_press=clicker.listen) as listener:
            listener.join()


    @property
    def start(self):
        return self._start

    @property
    def pause(self):
        return self._pause

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running: bool):
        self._running = running

if __name__ == '__main__':
    clicker = Clicker((Key.enter, Key.esc))
    clicker.listen_keyboard()
