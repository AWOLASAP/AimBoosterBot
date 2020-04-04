from PIL import ImageGrab
import keyboard
import pynput
import time


# Function to quit in case of emergency
def quit():
    global run
    run = False

# Function to check to see if two locations 
# are too close to each other (50px x and y)
def notClose(loc1, loc2):
    if abs(loc1[0] - loc2[0]) > 50:
        if abs(loc1[1] - loc2[1]) > 50:
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

    # Correct target color: target_color = (255, 106, 0, 255)
    # Testing color v
    target_color = (255, 96, 0, 255)
    targets = [(0, 0)]
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = pixs[x, y]
            if pixel == target_color and notClose((x, y), (targets[-1][0], targets[-1][1])):
                targets.append((x, y))
    
    # For debugging
    break

# For debugging
print(targets)
