from os import path

from clicktripz.openrtb.request.Device import Device
from random import randint


class UserDeviceFactory(object):
    def __init__(self, data_dir='data'):
        self.ua_list = self.load_data(path.join(data_dir, 'browser_user_agents'))
        self.ip_list = self.load_data(path.join(data_dir, 'arin_us_ipv4'))

    @staticmethod
    def load_data(file):
        with open(file) as f:
            return [line.rstrip() for line in f]

    def random_device(self):
        return Device(ip=self.random_us_ipv4(), ua=self.random_ua())

    def random_ua(self):
        return self.random_get(self.ua_list)

    def random_us_ipv4(self):
        return self.random_get(self.ip_list)

    @staticmethod
    def random_get(data):
        return data[randint(0, len(data) - 1)]

    @staticmethod
    def random_ipv4():
        return '.'.join([str(randint(23, 216)) for x in range(4)])

    @staticmethod
    def random_ipv6():
        return ':'.join([hex(randint(2 ** 16, 2 ** 17))[-4:] for x in range(8)])


