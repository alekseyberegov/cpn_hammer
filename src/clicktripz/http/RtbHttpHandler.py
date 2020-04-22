import json
import socketserver
import io
from http.server import SimpleHTTPRequestHandler
from random import random, randint

from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.response.Bid import Bid
from clicktripz.openrtb.response.BidResponse import BidResponse
from clicktripz.openrtb.response.SeatBid import SeatBid


class RtbHttpHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        output = io.BytesIO()
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        output.write(b"PLEASE USE POST METHOD")
        output.seek(0)
        self.wfile.write(output.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length).decode('utf-8')

        bid_req = BidRequest.deserialize(json.loads(content))
        bid_resp = BidResponse(
            id=bid_req.id,
            seatbid=[
                SeatBid(
                    bid=[
                       Bid(
                            id=bid_req.id,
                            impid=bid_req.imp[0].id,
                            adm='http://www.clicktripz.com',
                            price=0.6 * (1 + (randint(1, 100) - 50) / 100)
                       )
                    ],
                    seat='clicktripz'
                )
            ]

        )

        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(bytes(str(bid_resp.serialize()), 'utf-8'))
