import time, random
from pynput.keyboard import Key, Controller, Listener

def prezz(nappain):
    Controller().press(nappain)
    Controller().release(nappain)

def on_press(key):
    if (key == Key.enter):
        while 1:
            #s = random.randrange(1,33,1)/random.randrange(10,70,1)
            s = 0.1
            time.sleep(s)
                        
            prezz(Key.space)
            prezz('m')
            prezz('g')
            prezz('d')
            prezz('c')

            Controller().press(Key.shift)
            prezz('1')
            Controller().release(Key.shift)


with Listener(on_press=on_press) as listener:
    listener.join()