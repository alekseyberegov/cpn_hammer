from os import path

from clicktripz.openrtb.request.Device import Device
from random import randint


class UserDeviceFactory(object):
    def __init__(self, data_dir='data'):
        self.user_agents = self.load_data(path.join(data_dir, 'browser_user_agents'))
        self.us_ipv4 = self.load_data(path.join(data_dir, 'arin_us_ipv4'))

    @staticmethod
    def load_data(file):
        with open(file) as f:
            return [line.rstrip() for line in f]

    def random_device(self):
        return Device(ip=self.random_ipv4(), ua=self.random_ua())

    def random_ua(self):
        return self.random_peek(self.user_agents)

    def random_us_ipv4(self):
        return self.random_peek(self.us_ipv4)

    @staticmethod
    def random_peek(data):
        return data[randint(0, len(data) - 1)]

    @staticmethod
    def random_ipv4():
        return '.'.join([str(randint(23, 216)) for x in range(4)])

