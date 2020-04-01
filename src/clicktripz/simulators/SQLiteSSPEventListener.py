import json
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
        self.stmt.execute("create table bid_log(ts timestamp, req_id text, msg_type text, msg text)")

    def before_request(self, req: BidRequest):
        self.stmt.execute("insert into bid_log(ts, req_id, msg_type, msg) values (?, ?, ?, ?)"
                          , (datetime.datetime.now(), req.id, 'req', str(req.serialize())))

    def on_response(self, response: Response):
        print(response.content)
        bid_resp = BidResponse.deserialize(json.loads(response.content))
        self.stmt.execute("insert into bid_log(ts, req_id, msg_type, msg) values (?, ?, ?, ?)"
                          , (datetime.datetime.now(), bid_resp.id, 'resp', response.content))
        self.con.commit()

    def __del__(self):
        self.stmt.close()
        self.con.close()
