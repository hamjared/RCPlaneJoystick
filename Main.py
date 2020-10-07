from time import sleep

import pyglet
import evdev

# 0 axis = aileron
# 1 axis = elevator
# 2 axis = throttle
# 3 axis = rudder
from Joystick import Joystick



if __name__ == '__main__':
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    joystick = evdev.InputDevice(devices[0].path)
    print (joystick)
    while True:
        for event in joystick.read_loop():
            print(event)


