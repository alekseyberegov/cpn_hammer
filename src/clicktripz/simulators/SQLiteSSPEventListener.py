import json
import sqlite3
import datetime
import logging

from decimal import Decimal
from json import JSONDecodeError
from pathlib import Path
from requests import Response

from clicktripz.openrtb.request.BidRequest import BidRequest
from clicktripz.openrtb.response.BidResponse import BidResponse
from clicktripz.simulators.SSPEventListener import SSPEventListener


class SQLiteSSPEventListener(SSPEventListener):
    def __init__(self, db_dir):
        db_file = '_'.join(['bids', datetime.datetime.now().strftime("%m_%d_%Y-%H_%M_%S"), '.db'])
        self.con = sqlite3.connect(Path(db_dir) / db_file)
        self.stmt = self.con.cursor()
        self.stmt.execute("""
            create table bid_log(ts timestamp, status_code int, price decimal(10,4), req_id text, msg_type text, msg text)
            """)
        self.req_id = None

        logging.basicConfig(level=logging.INFO)

    def before_request(self, req: BidRequest):
        self.req_id = req.id
        self.stmt.execute("insert into bid_log(ts, status_code, price, req_id, msg_type, msg) values (?, ?, ?, ?, ?, ?)"
                          , (datetime.datetime.now(), 0, 0, req.id, 'req', str(req.serialize())))

    def on_response(self, response: Response):
        status = response.status_code
        content = response.content.decode("utf-8")
        price = Decimal(0)
        msg_id = self.req_id

        if status == 200:
            try:
                bid_resp = BidResponse.deserialize(json.loads(content))
                msg_id = bid_resp.id
                price = bid_resp.seatbid[0].bid[0].price
            except JSONDecodeError:
                pass

        logging.info('[%s] %s', status, content)
        self.stmt.execute("insert into bid_log(ts, status_code, price, req_id, msg_type, msg) values (?, ?, ?, ?, ?, ?)"
                          , (datetime.datetime.now(), status, float(price), msg_id, 'resp', content))
        self.con.commit()

    def __del__(self):
        self.stmt.close()
        self.con.close()
