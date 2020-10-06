import pygame
from time import sleep
from inputs import devices
import os
# 0 axis = aileron
# 1 axis = elevator
# 2 axis = throttle
# 3 axis = rudder
from Joystick import Joystick

if __name__ == '__main__':
    
    
    os.putenv('SDL_VIDEODRIVER', 'fbcon')
    
    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() != 1:
        print("No joystick detected...exiting")
        exit(0)
    joystick = Joystick(pygame.joystick.Joystick(0))

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print("joystick moved?: " + str(joystick.get_throttle()))
        clock.tick(30) # limit refresh rate to 30hz
