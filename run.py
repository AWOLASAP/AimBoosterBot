from PIL import ImageGrab
import keyboard
import pynput
import time


# Function to quit in case of emergency
def quit():
    global run
    run = False

# Add hotkey for emergency quiting
keyboard.add_hotkey(' ', quit)

# Set up variables
run = True



while run:
    screen_shot = ImageGrab.grab(bbox=(840, 730, 2040, 1570))
    pixs = screen_shot.load()
    size = screen_shot.size
    target_color = (255, 106, 0, 255)
    targets = []
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = pixs[x, y]
            if pixel == target_color:
                targets.append((x, y))
    
    # For debugging
    break

# For debugging
print(targets)
