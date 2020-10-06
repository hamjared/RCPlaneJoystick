from time import sleep

import pyglet

# 0 axis = aileron
# 1 axis = elevator
# 2 axis = throttle
# 3 axis = rudder
from Joystick import Joystick

def poll_joystick(dt):
    print(joystick.x)


if __name__ == '__main__':

    joystick = pyglet.input.get_joysticks()[0]
    joystick.open()
    pyglet.clock.schedule_interval(poll_joystick, 0.1)
    pyglet.app.run()



