import unittest
import os
from pathlib import Path

from clicktripz.device.UserDeviceFactory import UserDeviceFactory


class UserDeviceFactoryTestCase(unittest.TestCase):
    def setUp(self):
        data_dir = Path(os.path.dirname(__file__)) / '..' / '..' / '..' / '..' / 'data'
        self.factory = UserDeviceFactory(data_dir=data_dir)

    def tearDown(self):
        del self.factory

    def test_random_ua(self):
        self.assertIsNotNone(self.factory.random_ua())

    def test_random_us_ipv4(self):
        self.assertIsNotNone(self.factory.random_us_ipv4())

    def test_random_device(self):
        device = self.factory.random_device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.ip)
        self.assertIsNotNone(device.ua)

