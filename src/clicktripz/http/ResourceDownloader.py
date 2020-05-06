from lxml import html
import requests


class ResourceDownloader(object):
    def __init__(self):
        self.tree = None

    def download(self, url):
        page = requests.get(url)
        self.tree = html.fromstring(page.content)

    def __str__(self):
        return str(self.tree)

    def xpath(self, path):
        return self.tree.xpath(path)
