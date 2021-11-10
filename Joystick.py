import evdev
from evdev import InputEvent

from Transmitter import Transmitter, Channel, TrimDirection





class Joystick:
    def __init__(self, joystick: evdev.InputDevice,
                 transmitter: Transmitter,
                 throttle_code: int = 6, throttle_type: int = 3,
                 elevator_code: int = 1, elevator_type: int = 3,
                 aileron_code: int = 0, aileron_type: int = 3,
                 rudder_code: int = 5, rudder_type: int = 3,
                 min_value=0, max_value=255):

        self.joystick = joystick
        self.transmitter = transmitter

        self.throttle_code = throttle_code
        self.throttle_type = throttle_type

        self.elevator_code = elevator_code
        self.elevator_type = elevator_type

        self.aileron_code = aileron_code
        self.aileron_type = aileron_type

        self.rudder_code = rudder_code
        self.rudder_type = rudder_type

        self.min_value = min_value
        self.max_value = max_value

    def handle_event(self, event: InputEvent):
        if event.code == 0 and event.type == 0:
            return  # no event actually took place so ignore it

        self.handle_analog_input(event)
        self.handle_trim_input(event)


    def handle_analog_input(self, event):
        channel = ""
        value = event.value
        if event.code == self.throttle_code and event.type == self.elevator_type:
            channel = "Throttle"
        elif event.code == self.elevator_code and event.type == self.elevator_type:
            channel = "Elevator"
        elif event.code == self.aileron_code and event.type == self.aileron_type:
            channel = "Aileron"
        elif event.code == self.rudder_code and event.type == self.rudder_type:
            channel = "Rudder"
        else:
            return
        self.transmitter.set_channel(channel, value, (self.min_value, self.max_value))

    def handle_trim_input(self, event):
        if event.code == 291 and event.type == 1 and event.value == 1:
            channel = Channel.ELEVATOR
            direction = TrimDirection.UP
        elif event.code == 290 and event.type == 1 and event.value == 1:
            channel = Channel.ELEVATOR
            direction = TrimDirection.DOWN
        elif event.code == 297 and event.type == 1 and event.value == 1:
            channel = Channel.RUDDER
            direction = TrimDirection.LEFT
        elif event.code == 296 and event.type == 1 and event.value == 1:
            channel = Channel.RUDDER
            direction = TrimDirection.RIGHT
        elif event.code == 16 and event.type == 3 and event.value == 1:
            channel = Channel.AILERON
            direction = TrimDirection.RIGHT
        elif event.code == 16 and event.type == 3 and event.value == -1:
            channel = Channel.AILERON
            direction = TrimDirection.LEFT
        else:
            return

        self.transmitter.trim(channel, direction)