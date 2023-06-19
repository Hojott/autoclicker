from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()

def on_press(key):
    if key == 'a':
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    if key == 'd':
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        keyboard.press(Key.right)
        keyboard.release(Key.right)

with Listener(on_press=on_press) as listener:
    listener.join()
