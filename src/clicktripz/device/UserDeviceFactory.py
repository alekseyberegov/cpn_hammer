from os import path

from clicktripz.openrtb.request.Device import Device
from random import randint


class UserDeviceFactory(object):
    def __init__(self, data_dir='data'):
        # load user agents from the data file
        with open(path.join(data_dir, 'browser_user_agents')) as f:
            self.user_agents = [line.rstrip() for line in f]

        # load US IPv4 from the data file
        with open(path.join(data_dir, 'arin_us_ipv4')) as f:
            self.us_ipv4 = [line.rstrip() for line in f]

    def random_device(self):
        pass

    def random_ua(self):
        return self.user_agents[randint(0, len(self.user_agents) - 1)]

    @staticmethod
    def random_ip():
        return '.'.join([str(randint(23, 216)) for x in range(4)])

