import configparser
import logging
import os
import sqlite3
from pathlib import Path
from time import sleep

import fire

from clicktripz.image.WebPhotoTaker import WebPhotoTaker


class Creative(object):
    def __init__(self):
        self.ini = configparser.ConfigParser()
        self.ini.read(['.cpn.ini', os.path.expanduser('~/.cpn.ini')])
        self.taker = WebPhotoTaker(self.ini['image']['output_image_dir'])

    def images_from_db(self, db_file):
        con = sqlite3.connect(Path(self.ini['databases']['output_db_dir']) / db_file)
        stmt = con.cursor()
        for row in stmt.execute("""
             select replace(url, '$'||'{AUCTION_PRICE}'
                        , cast(price * (1 - abs(random() % 500) / 10000.0) as text)) as adm
                from (
                    select json_extract(msg, '$.seatbid[0].bid[0].adm') as url
                        ,  cast(json_extract(msg, '$.seatbid[0].bid[0].price') as decimal(8,4)) as price
                    from (
                        select  * 
                        from bid_log 
                        where msg_type = 'resp' 
                            and status_code = 200
                    )
                )
                """):
            self.photo(row[0])
            sleep(1)

        stmt.close()
        con.close()

    def photo(self, url):
        logging.info(url)
        self.taker.take_photo(url)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Creative)
