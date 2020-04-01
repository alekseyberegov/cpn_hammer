
from requests import Response
from clicktripz.openrtb.request.BidRequest import BidRequest


class SSPEventListener(object):
    def before_request(self, request: BidRequest):
        print(request)

    def on_response(self, response: Response):
        print(response.content)
