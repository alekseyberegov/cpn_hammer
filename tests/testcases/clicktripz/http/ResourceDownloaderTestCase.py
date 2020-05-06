import unittest

from clicktripz.http.ResourceDownloader import ResourceDownloader


class ResourceDownloaderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.downloader = ResourceDownloader()

    def tearDown(self) -> None:
        del self.downloader

    def test_simple_xpath(self):
        self.downloader.download('http://www.clicktripz.com')
        div_arr: list = self.downloader.xpath('//div')
        self.assertGreater(len(div_arr), 0)

