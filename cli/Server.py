import logging
import os
import sys
from http.server import HTTPServer
from pathlib import Path

import fire


class Server(object):
    def __init__(self, handler_class):
        self.handler_class = handler_class

    def run(self, port=9000):
        server_address = ('', port)
        httpd = HTTPServer(server_address, self.handler_class)
        httpd.serve_forever()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    src_path = Path(os.path.dirname(__file__)) / '..' / 'src'
    sys.path.append(os.path.abspath(src_path))
    logging.info(sys.path)
    mod = __import__('clicktripz.http.RtbHttpHandler', fromlist=['RtbHttpHandler'])
    klass = getattr(mod, 'RtbHttpHandler')
    fire.Fire(Server(handler_class=klass))
