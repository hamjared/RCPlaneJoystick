import RPi.GPIO as GPIO


class Multiplexer:
    def __init__(self, channel_a_pin: int, channel_b_pin: int, channel_c_pin: int, inhibit_pin: int):
        self.channel_a_pin = channel_a_pin
        self.channel_b_pin = channel_b_pin
        self.channel_c_pin = channel_c_pin
        self.inhibit_pin = inhibit_pin
        GPIO.setup(self.channel_a_pin, GPIO.OUT)
        GPIO.setup(self.channel_b_pin, GPIO.OUT)
        GPIO.setup(self.channel_c_pin, GPIO.OUT)
        GPIO.setup(self.inhibit_pin, GPIO.OUT)
        self.inhibit()

    def set(self, value: int):
        GPIO.output(self.channel_a_pin, value & 0b001)
        GPIO.output(self.channel_b_pin, value & 0b010)
        GPIO.output(self.channel_c_pin, value & 0b100)

    def inhibit(self):
        GPIO.output(self.inhibit_pin, GPIO.HIGH)

    def enable(self):
        GPIO.output(self.inhibit_pin, GPIO.LOW)
