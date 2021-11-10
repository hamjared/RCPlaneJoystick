import RPi.GPIO as GPIO
import spidev


class Potentiometer:
    def __init__(self, chip_select: int, spi_bus: spidev.SpiDev, address: int, num_steps: int = 128):
        self.chip_select = chip_select
        self.spi_bus = spi_bus
        self.address = address
        self.num_steps = num_steps

        GPIO.setup(self.chip_select, GPIO.OUT)

    def write_pot(self, value: int):
        GPIO.output(self.chip_select, 0)
        self.spi_bus.xfer([self.address << 4, value])
        GPIO.output(self.chip_select, 1)
