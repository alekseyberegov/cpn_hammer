from clicktripz.http.utils import make_url


class ResponseFactory(object):
    def __init__(self):
        self.adm_url = make_url('https://staycation.tiki.com'
                                , 'cant-travel-turn-your-quarantine-into-a-staycation'
                                , utm_source=2949
                                , utm_campaign='staycation'
                                , utm_medium='fslb-20'
                                , bid='${AUCTION_PRICE}')

    def get_adm_url(self):
        return self.adm_url
