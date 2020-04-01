import unittest

from clicktripz.openrtb.exchange.DemandSource import DemandSource
from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.request.Device import Device
from clicktripz.openrtb.request.Impression import Impression
from clicktripz.openrtb.request.Site import Site
from clicktripz.openrtb.request.User import User


class DemandSourceTestCase(unittest.TestCase):
    def setUp(self):
        self.source = DemandSource('https://engine.4dsply.com/openrtb.engine?id=4acdfb19-9abc-4f7b-b462-6db64da879b4&zoneId=60436')

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
