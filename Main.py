import time

import evdev
import spidev
from RPi import GPIO

from DX5e import DX5e
from Joystick import Joystick
from Potentiometer import Potentiometer
from Multiplexer import Multiplexer

if __name__ == '__main__':
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    joystick = evdev.InputDevice(devices[0].path)

    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 976000
    GPIO.setmode(GPIO.BCM)

    throttle_pot = Potentiometer(2, spi, 1)
    elevator_pot = Potentiometer(3, spi, 1)
    aileron_pot = Potentiometer(2, spi, 0)
    rudder_pot = Potentiometer(3, spi, 0)
    trim_mux = Multiplexer(channel_a_pin=21, channel_b_pin=20, channel_c_pin=19, inhibit_pin=25)

    transmitter = DX5e(throttle_pot, elevator_pot, aileron_pot, rudder_pot, trim_mux)
    transmitter.add_channel("Rudder Trim", Potentiometer(15,spi, 0))

    joystick = Joystick(joystick, transmitter)
    while True:
        for event in joystick.joystick.read_loop():
            print(event)
            joystick.handle_event(event)
            time.sleep(0.01)
