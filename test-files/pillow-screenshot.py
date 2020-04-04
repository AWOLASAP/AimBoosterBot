from PIL import ImageGrab
import time

start = time.time() 
ss = ImageGrab.grab()
grabbed = time.time()
ss.show()
shown = time.time()
print(grabbed - start)
print(shown - start)
