import keyboard
import sys

def quit():
    print("Ded")
    global x
    x = 2

#keyboard.add_hotkey(57, quit)
keyboard.add_hotkey(' ', quit, suppress=True)
x = 1
while x == 1:
    pass
