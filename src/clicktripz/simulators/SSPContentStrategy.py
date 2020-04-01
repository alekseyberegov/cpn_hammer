from random import randint
from time import sleep

from clicktripz.device.UserDeviceFactory import UserDeviceFactory
from clicktripz.iab.IABContentCategory import IABContentCategory
from clicktripz.openrtb.exchange.DemandSource import DemandSource
from clicktripz.openrtb.request.BidRequest import BidRequest

import uuid

from clicktripz.openrtb.request.Impression import Impression
from clicktripz.openrtb.request.Site import Site
from clicktripz.openrtb.request.User import User
from clicktripz.simulators.SSPEventListener import SSPEventListener


class SSPContentStrategy(object):
    def __init__(self, device_factory: UserDeviceFactory, demand_source: DemandSource, listener: SSPEventListener):
        self.device_factory = device_factory
        self.demand_source = demand_source
        self.listener = listener

    def run(self, runs, pause, sites):
        for i in range(runs):
            req = BidRequest(
                id=str(uuid.uuid1()),
                bcat=["IAB-23", "IAB-24", "IAB-25", "IAB-26"],
                imp=[Impression(id=str(uuid.uuid1()), instl=1)],
                device=self.device_factory.random_device(),
                site=Site(id=sites[randint(0, len(sites) - 1)], cat=IABContentCategory.get_random()),
                user=User(id=str(uuid.uuid1()))
            )
            self.listener.before_request(req)
            resp = self.demand_source.send_bid_request(req)
            self.listener.on_response(resp)
            sleep(pause)
