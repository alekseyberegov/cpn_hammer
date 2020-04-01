import requests


class DemandSource(object):
    def __init__(self, url):
        self.headers = {'x-openrtb-version': '2.5'}
        self.url = url

    def send_bid_request(self, request):
        payload = str(request.serialize())
        r = requests.post(self.url, json=payload)
