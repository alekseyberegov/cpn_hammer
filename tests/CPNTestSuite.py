import unittest

from testcases.clicktripz.device.UserDeviceFactoryTestCase import UserDeviceFactoryTestCase
from testcases.clicktripz.iab.IABContentCategoryTestCase import IABContentCategoryTestCase
from testcases.clicktripz.serialize.ArrayTestCase import ArrayTestCase
from testcases.clicktripz.serialize.FieldTestCase import FieldTestCase

test_cases = [
    FieldTestCase,
    ArrayTestCase,
    UserDeviceFactoryTestCase,
    IABContentCategoryTestCase
]


def get_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(get_suite())
