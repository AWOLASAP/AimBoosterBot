from PIL import ImageGrab
import pynput
import time


# The first step is 









screen_shot = ImageGrab.grab(bbox=(840, 730, 2040, 1570))
pix = screen_shot.load()
size = screen_shot.size
print("The image size is:", size)
print("The pixel at 100, 100 is:", pix[100, 100])
target = (37, 37, 37, 255)
for x in range(size[0]):
    for y in range(size[1]):
        if pix[x, y] == target:
            print("Found target at:", x, y)
