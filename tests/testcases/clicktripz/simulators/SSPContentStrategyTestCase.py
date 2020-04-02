import configparser
import os
import unittest
from pathlib import Path
from random import randint

from clicktripz.device.UserDeviceFactory import UserDeviceFactory
from clicktripz.openrtb.exchange.DemandSource import DemandSource
from clicktripz.simulators.SQLiteSSPEventListener import SQLiteSSPEventListener
from clicktripz.simulators.SSPContentStrategy import SSPContentStrategy


class SSPContentStrategyTestCase(unittest.TestCase):
    def setUp(self):
        ini = configparser.ConfigParser()
        ini.read(['.cpn.ini', os.path.expanduser('~/.cpn.ini')])

        data_dir = Path(os.path.dirname(__file__)) / '..' / '..' / '..' / '..' / 'data'

        self.demand_source = DemandSource(ini['dsp']['bidder_url'])
        self.device_factory = UserDeviceFactory(data_dir=data_dir)
        self.listener = SQLiteSSPEventListener(ini['databases']['output_db_dir'])
        self.simulator = SSPContentStrategy(self.device_factory, self.demand_source, self.listener)

    def tearDown(self):
        del self.simulator
        del self.device_factory
        del self.demand_source
        del self.listener

    def test_short_run(self):
        self.simulator.run(2, randint(500, 3000) / 1000, ['360', '2824', '2828', '1482'])
