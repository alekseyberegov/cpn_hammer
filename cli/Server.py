import logging
from http.server import HTTPServer
import fire

from clicktripz.http.RtbHttpHandler import RtbHttpHandler


class Server(object):
    def __init__(self, handler_class):
        self.handler_class = handler_class

    def run(self, port=9000):
        server_address = ('', port)
        httpd = HTTPServer(server_address, self.handler_class)
        httpd.serve_forever()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Server(handler_class=RtbHttpHandler))
