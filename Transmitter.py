import string
from abc import ABC, abstractmethod
from enum import Enum

from Potentiometer import Potentiometer


def scale(val, src, dst) -> int:
    return ((val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


class Channel(Enum):
    THROTTLE = 1
    ELEVATOR = 2
    AILERON = 3
    RUDDER = 4
    GEAR = 5


class TrimDirection(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 0
    LEFT = 1


class Transmitter(ABC):

    def __init__(self):
        self.channels = []
        self.channel_mapping = {}

    def add_channel(self, channel_name: string, potentiometer: Potentiometer):
        self.channels.append(potentiometer)
        self.channel_mapping[channel_name] = len(self.channels) - 1

    def get_channel(self, channel_name: string) -> Potentiometer:
        index = self.channel_mapping[channel_name]
        return self.channels[index]

    @abstractmethod
    def set_channel(self, channel_name: string, value: int, value_range):
        pass

    @abstractmethod
    def trim(self, channel: Channel, direction: TrimDirection):
        pass


if __name__ == '__main__':
    print("Hello")
    print(TrimDirection.UP)
