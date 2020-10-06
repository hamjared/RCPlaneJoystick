import pygame


class Joystick:
    def __init__(self, joystick: pygame.joystick.Joystick,
                 throttle_axis: int = 2,
                 elevator_axis: int = 1,
                 aileron_axis: int = 0,
                 rudder_axis: int = 3):
        self.joystick = joystick
        self.joystick.init()
        self.throttle_axis = throttle_axis
        self.elevator_axis = elevator_axis
        self.aileron_axis = aileron_axis
        self.rudder_axis = rudder_axis

    def get_throttle(self) -> float:
        print("From Joystick: " + str(self.joystick.get_axis(2)))
        return self.joystick.get_axis(self.throttle_axis)

    def get_elevator(self) -> float:
        pass

    def get_aileron(self) -> float:
        pass

    def get_rudder(self) -> float:
        pass
