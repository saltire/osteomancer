import time

from serial import Serial


class Arduino:
    def __init__(self, port, baud):
        self.serial = Serial(port, baud)
        time.sleep(2)

    def write_ints(self, *ints):
        bytestr = b''.join(i.to_bytes(1, byteorder='little') for i in ints)
        self.serial.write(bytestr)
