import time, random
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()

def prezz(nappain):
    keyboard.press(nappain)
    keyboard.release(nappain)

def on_press(key):
    if (key == Key.enter):
        time.sleep(1)
        while 1:
            s = 0.1
            time.sleep(s)
                        
            prezz(Key.space)
            prezz('m')
            prezz('g')
            prezz('d')
            prezz('c')

            with keyboard.pressed(Key.shift):
                prezz('1')

with Listener(on_press=on_press) as listener:
    listener.join()
