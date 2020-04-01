import unittest

from clicktripz.openrtb.exchange.DemandSource import DemandSource
from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.request.Device import Device
from clicktripz.openrtb.request.Impression import Impression
from clicktripz.openrtb.request.Site import Site
from clicktripz.openrtb.request.User import User


class DemandSourceTestCase(unittest.TestCase):
    def setUp(self):
        self.source = DemandSource('https://postman-echo.com/post')

    def tearDown(self):
        del self.source

    def test_simple_bid(self):
        req = BidRequest(
            id="reqid",
            imp=[
                Impression(
                    impid="impid",
                    instl=1
                )
            ],
            device=Device(
                ip="1.23,4.56",
                ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            ),
            site=Site(
                id="siteid",
                cat=[ "IAB12", "IAB12-5" ]
            ),
            user=User(
                id="user1"
            )
        )
        resp = self.source.send_bid_request(req)
        print(resp.content)
