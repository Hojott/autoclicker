import time, random
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()

def prezz(nappain):
    for i in range(20):
        keyboard.press(nappain)
        keyboard.release(nappain)

def on_press(key):
    if (key == Key.enter):
        time.sleep(1)
        while 1:
            s = 0.001
            time.sleep(s)
                        
            #prezz(Key.space)
            #prezz('m')
            prezz('8')
            prezz('7')
            prezz('6')
            prezz('5')
            prezz('4')
            prezz('3')
            prezz('2')
            prezz('1')
            prezz('t')
            #prezz('g')
            #prezz('d')
            ##prezz('c')

            #with keyboard.pressed(Key.shift):
            #    prezz('8')
                #prezz('1')

with Listener(on_press=on_press) as listener:
    listener.join()
