import pyscreenshot as ImageGrab
import time

s = time.time()
ss = ImageGrab.grab()
print(time.time() - s)
ss.show()
print(time.time() - s)
