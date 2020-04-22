import configparser
import os
import unittest
from pathlib import Path

from clicktripz.openrtb.exchange.DemandSource import DemandSource
from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.request.Device import Device
from clicktripz.openrtb.request.Impression import Impression
from clicktripz.openrtb.request.Site import Site
from clicktripz.openrtb.request.User import User


class DemandSourceTestCase(unittest.TestCase):
    def setUp(self):
        ini = configparser.ConfigParser()
        ini.read(['.cpn.ini', os.path.expanduser('~/.cpn.ini')])

        self.source = DemandSource(ini['dsp']['bidder_url'])

    def tearDown(self):
        del self.source

    def test_sample_bid_request(self):
        req = BidRequest(
            id="fffd894f-c33c-4c08-b826-4448fcaecc85",
            bcat=["CTX-1", "CTX-3", "CTX-4"],
            imp=[
                Impression(
                    id="aaad894f-c33c-4c08-b826-4448fcaecc899",
                    instl=1
                )
            ],
            device=Device(
                ip="47.144.160.0",
                ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            ),
            site=Site(
                id="19283",
                cat=["IAB12", "IAB12-5"]
            ),
            user=User(
                id="08057c4b-4cb3-4e65-8a9b-b6db49d921a7"
            )
        )
        resp = self.source.send_bid_request(req)
        print(resp.content)
