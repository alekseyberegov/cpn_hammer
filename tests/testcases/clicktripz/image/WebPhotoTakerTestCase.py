import configparser
import os
import unittest

from clicktripz.image.WebPhotoTaker import WebPhotoTaker


class WebPhotoTakerTestCase(unittest.TestCase):
    taker: WebPhotoTaker

    def setUp(self) -> None:
        ini = configparser.ConfigParser()
        ini.read(['.cpn.ini', os.path.expanduser('~/.cpn.ini')])
        self.taker = WebPhotoTaker(ini['image']['output_image_dir'])

    def tearDown(self) -> None:
        del self.taker

    def test_take_photo(self):
        self.taker.take_photo('https://www.fightful.com/wrestling/?utm_source=AdSupply&utm_campaign=AS-Desktop&utm_medium=&utm_content=15458')

