'''
UL: 840 730
UR: 2040 730
DL: 840 1570
DR: 2040 1570
'''
from PIL import ImageGrab
import time

start = time.time() 
ss = ImageGrab.grab(bbox=(840, 730, 2040, 1570))
grabbed = time.time()
ss.show()
shown = time.time()
print(grabbed - start)
print(shown - start)
