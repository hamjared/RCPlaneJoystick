import string
from time import sleep

from Potentiometer import Potentiometer
from Transmitter import Transmitter, scale, TrimDirection, Channel
from Multiplexer import Multiplexer


class DX5e(Transmitter):

    def __init__(self, throttle_pot: Potentiometer,
                 elevator_pot: Potentiometer,
                 aileron_pot: Potentiometer,
                 rudder_pot: Potentiometer,
                 trim_mux: Multiplexer):
        super().__init__()
        self.add_channel('Throttle', throttle_pot)
        self.add_channel('Elevator', elevator_pot)
        self.add_channel('Aileron', aileron_pot)
        self.add_channel('Rudder', rudder_pot)
        self.trim_mux = trim_mux

    def set_channel(self, channel_name: string, value: int, value_range):
        pot = self.get_channel(channel_name)
        mapped_value = scale(value, value_range, (0, pot.num_steps - 1))
        print("Setting " + channel_name + " to " + str(int(mapped_value)))
        pot.write_pot(int(mapped_value))

    def trim(self, channel: Channel, direction: TrimDirection):
        # multiplexer channel will be determined by 2*channel - 1 - direction
        print("Trimming " + str(channel) + " " + str(direction))
        mux_channel = 2*channel.value - 1 - direction.value
        self.trim_mux.set(mux_channel)
        self.trim_mux.enable()
        sleep(0.025)
        self.trim_mux.inhibit()





