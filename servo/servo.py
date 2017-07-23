import random
import time

from arduino import Arduino


ard = Arduino('/dev/ttyACM0', 9600)
print('Connected', flush=True)

def randomize():
    while True:
        angle = random.randint(0, 180)
        print(angle, flush=True)
        ard.write_ints(angle)
        time.sleep(3)


def roll_bones():
    ard.write_ints(36)
