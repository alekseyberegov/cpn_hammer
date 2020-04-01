import json
import unittest
from decimal import Decimal

from clicktripz.serialize.Array import Array
from clicktripz.serialize.String import String


class ArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.array = None

    def tearDown(self):
        if self.array is not None:
            del self.array

    def test_array_str(self):
        self.array = Array(String)
        obj = self.array.deserialize(json.loads('["a","b","c"]'))
        self.assertListEqual(obj, ["a", "b", "c"])

    def test_array_decimal(self):
        self.array = Array(Decimal)
        obj = self.array.deserialize(json.loads('[1.1, 2.2, 3.3]'))
        self.assertListEqual(obj, [1.1, 2.2, 3.3])


