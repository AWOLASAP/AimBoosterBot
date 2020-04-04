from PIL import ImageGrab
import keyboard
import time
from pynput.mouse import Button, Controller


# Define mouse as something
# that can be controlled
mouse = Controller()


# Function to quit in case of emergency
def quit():
    global run
    run = False

# Function to check to see if two locations 
# are too close to each other (30px x and y)
def notClose(loc1, loc2):
    if abs(loc1[0] - loc2[0]) > 30:
        if abs(loc1[1] - loc2[1]) > 30:
            return True
    return False

# Add hotkey for emergency quiting
keyboard.add_hotkey(' ', quit)

# Set up variables
run = True

# Main loop
while run:
    # Get a screen shot of the field, load the pixel values,
    # and get the size of the image (last part is probably 
    # not needed but eh)
    screen_shot = ImageGrab.grab(bbox=(840, 730, 2040, 1570))
    pixs = screen_shot.load()
    size = screen_shot.size
    
    # Go through the image looking for targets
    # Does this by finding the color of the target

    # Correct target color v 
    target_color = (255, 255, 255, 255)
    # Testing color v
    # target_color = (255, 96, 0, 255)
    targets = [(0, 0)]
    for x in range(0, size[0], 2):
        for y in range(0, size[1], 2):
            if pixs[x, y] == target_color and notClose((x+840, y+730), (targets[-1][0], targets[-1][1])):
                if (x, y) != mouse.position:
                    # Add coords to target list, adjusting 
                    # them for the fullscreen screenshot
                    targets.append((x+840, y+730))

    # Go through each target in the gathered list
    # and click in that location
    for t in targets[1:]:
        # Move the mouse over the target
        mouse.position = ((t[0]/3840) * 1920, (t[1]/2400) * 1200)
        time.sleep(0.01)

        # Click on the target
        mouse.press(Button.left)
        mouse.release(Button.left)
    
