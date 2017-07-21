import random
import time

from arduino import Arduino


ard = Arduino('COM4', 9600)
print('Connected', flush=True)

while True:
    angle = random.randint(0, 180)
    print(angle, flush=True)
    ard.write_ints(angle)
    time.sleep(3)
