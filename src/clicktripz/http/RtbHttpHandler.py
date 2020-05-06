import json
import io
import sys
import traceback
import urllib
from http.server import SimpleHTTPRequestHandler

from clicktripz.openrtb.exchange.BidManager import BidManager
from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.response.Bid import Bid
from clicktripz.openrtb.response.BidResponse import BidResponse
from clicktripz.openrtb.response.SeatBid import SeatBid
from clicktripz.http.ResponseFactory import ResponseFactory
from clicktripz.serialize.ValidationError import ValidationError


class RtbHttpHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.bid_manager = BidManager()
        self.resp_factory = ResponseFactory()
        super().__init__(*args, **kwargs)

    def handle_bid(self, bid_req: BidRequest) -> BidRequest:
        url = self.resp_factory.get_adm_url(auction_uuid=bid_req.id)
        bid_resp = BidResponse(
            id=bid_req.id,
            cur="USD",
            seatbid=[
                SeatBid(
                    bid=[
                        Bid(
                            id=bid_req.id,
                            impid=bid_req.imp[0].id,
                            adm=url,
                            nurl=url,
                            price=self.bid_manager.generate_bid(),
                            w=1024,
                            x=768
                        )
                    ],
                )
            ]
        )
        return bid_resp

    def send_unsupported(self, capability):
        output = io.BytesIO()
        self.send_response(400)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        resp_body = '{"error": "%s is not supported"}' % capability
        output.write(bytes(resp_body, 'utf-8'))
        output.seek(0)
        self.wfile.write(output.read())

    def do_GET(self):
        self.send_unsupported('GET')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length).decode('utf-8')

        try:
            bid_req = BidRequest.deserialize(json.loads(content))
            bid_resp = self.handle_bid(bid_req)
            resp_body = str(bid_resp.serialize())
            resp_code = 200
        except (ValidationError, ValueError) as err:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            resp_body = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
            resp_body = '{"error": "malformed request", "stacktrace" : "%s"}' % urllib.parse.quote(resp_body)
            resp_code = 400

        self.send_response(resp_code)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(bytes(resp_body, 'utf-8'))

