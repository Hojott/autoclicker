from time import sleep
from pynput.keyboard import Key, Listener, Controller
from PIL import Image, ImageGrab

keyboard = Controller()

def getHex(rgb):
    return '%02X%02X%02X'%rgb

def check_color(x,y):
    bounding_box = (x,y,x+1,y+1)
    image = ImageGrab.grab(bbox=bounding_box)
    rgb_image = image.convert('RGB')
    r,g,b = rgb_image.getpixel((0,0))
    hex_color = getHex((r,g,b))
    return hex_color

def on_press(key):
    if key == Key.enter:
        while 1:
            color = check_color(898, 634)
            print(color)
            if color == 'A17438' or color == '886332' or color == '99CC66':
                     keyboard.press(Key.right)
                     keyboard.release(Key.right)
            else:
                     keyboard.press(Key.left)
                     keyboard.release(Key.left)
            sleep(0.5)

with Listener(on_press=on_press) as listener:
    listener.join()
