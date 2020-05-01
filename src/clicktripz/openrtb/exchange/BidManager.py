from random import randint


class BidManager(object):
    def __init__(self):
        self.bid_mean = 2.5
        self.bid_sigma = 0.5

    def generate_bid(self):
        r = 1000
        return self.bid_mean * (1 + (randint(1, r) - self.bid_sigma * r) / r)
