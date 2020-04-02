import json
from decimal import Decimal
from json import JSONDecodeError
from pathlib import Path

from requests import Response

from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.response.BidResponse import BidResponse
from clicktripz.simulators.SSPEventListener import SSPEventListener

import sqlite3
import datetime


class SQLiteSSPEventListener(SSPEventListener):
    def __init__(self, db_name):
        db_file = '_'.join([db_name, datetime.datetime.now().strftime("%m_%d_%Y-%H_%M_%S"), '.db'])
        self.con = sqlite3.connect(Path.home() / db_file)
        self.stmt = self.con.cursor()
        self.stmt.execute("""
            create table bid_log(ts timestamp, status_code int, price decimal(10,4), req_id text, msg_type text, msg text)
            """)
        self.req_id = None

    def before_request(self, req: BidRequest):
        self.req_id = req.id
        self.stmt.execute("insert into bid_log(ts, status_code, price, req_id, msg_type, msg) values (?, ?, ?, ?, ?, ?)"
                          , (datetime.datetime.now(), 0, 0, req.id, 'req', str(req.serialize())))

    def on_response(self, response: Response):
        status = response.status_code
        price = Decimal(0)

        print(str(status) + ":" + str(response.content))

        if status == 200:
            try:
                bid_resp = BidResponse.deserialize(json.loads(response.content))
                self.req_id = bid_resp.id
                price = bid_resp.seatbid[0].bid[0].price
            except JSONDecodeError:
                pass
        self.stmt.execute("insert into bid_log(ts, status_code, price, req_id, msg_type, msg) values (?, ?, ?, ?, ?, ?)"
                          , (datetime.datetime.now(), status, float(price), self.req_id, 'resp', response.content))
        self.con.commit()

    def __del__(self):
        self.stmt.close()
        self.con.close()
