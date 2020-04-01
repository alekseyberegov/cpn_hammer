import os
import unittest
from pathlib import Path

from clicktripz.device.UserDeviceFactory import UserDeviceFactory
from clicktripz.openrtb.exchange.DemandSource import DemandSource
from clicktripz.simulators.SSPContentStrategy import SSPContentStrategy
from clicktripz.simulators.SSPEventListener import SSPEventListener


class SSPContentStrategyTestCase(unittest.TestCase):
    def setUp(self):
        data_dir = Path(os.path.dirname(__file__)) / '..' / '..' / '..' / '..' / 'data'

        self.demand_source = DemandSource('https://engine.4dsply.com/openrtb.engine?id=4acdfb19-9abc-4f7b-b462-6db64da879b4&zoneId=60436')
        self.device_factory = UserDeviceFactory(data_dir=data_dir)
        self.listener = SSPEventListener()
        self.simulator = SSPContentStrategy(self.device_factory, self.demand_source, self.listener)

    def tearDown(self):
        del self.simulator
        del self.device_factory
        del self.demand_source
        del self.listener

    def test_short_run(self):
        self.simulator.run(5, 0.5, ['360', '2824'])
