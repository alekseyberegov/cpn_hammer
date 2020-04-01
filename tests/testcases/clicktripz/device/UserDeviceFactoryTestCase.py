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

    def test_generate_ua(self):
        self.assertIsNotNone(self.factory.random_ua())
