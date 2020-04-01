import unittest

from clicktripz.iab.IABContentCategory import IABContentCategory


class IABContentCategoryTestCase(unittest.TestCase):
    def setUp(self):
        self.category = IABContentCategory()

    def tearDown(self):
        del self.category

    def test_get_desc_top_level(self):
        desc = self.category.get_desc("IAB1")
        self.assertListEqual(desc, ['Arts & Entertainment'])

    def test_get_desc_second_level(self):
        desc = self.category.get_desc("IAB1-1")
        self.assertListEqual(desc, ['Books & Literature', 'Arts & Entertainment'])

    def test_get_desc_unknown(self):
        desc = self.category.get_desc("IAB40-1")
        self.assertListEqual(desc, ['IAB40-1'])

    def test_get_desc_malformed(self):
        desc = self.category.get_desc("XUI")
        self.assertListEqual(desc, ['XUI'])

    def test_get_random(self):
        cats = self.category.get_random()
        self.assertEqual(len(cats), 3)
        self.assertListEqual([cats[1],cats[2]], self.category.get_desc(cats[0]))


