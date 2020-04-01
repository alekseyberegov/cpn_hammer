from requests import Request, Session


class DemandSource(object):
    def __init__(self, url):
        self.headers = {'x-openrtb-version': '2.5', 'Content-Type': 'application/json'}
        self.url = url

    def send_bid_request(self, request):
        data = str(request.serialize())
        session = Session()

        req = Request('POST', self.url, data=data, headers=self.headers)
        prepped = req.prepare()
        response = session.send(prepped)
        session.close()

        return response
