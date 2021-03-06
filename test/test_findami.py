__author__ = 'stormacq'

import unittest
import logging

from findAMI import AMIFinder


class AMIFinderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig()
        cls.logger = logging.getLogger(__name__)
        cls.logger.setLevel(logging.INFO)
        cls.finder = AMIFinder(cls.logger)

    def test_FindAMI_BasicVersion_eu_west_1(self):
        image = self.finder.findWindowsAMIInRegion('eu-west-1', '2012', 'en')
        self.assertIsNotNone(image, 'Did not find a Windows 2012 AMI in eu-west-1 for English locale')

    def test_FindAMI_ComplexVersion_eu_west_1(self):
        image = self.finder.findWindowsAMIInRegion('eu-west-1', '2008 R2 SP1', 'en')
        self.assertIsNotNone(image, 'Did not find a Windows 2008 AMI in eu-west-1 for English locale')

    def test_FindAMI_BasicVersion_us_east_1(self):
        image = self.finder.findWindowsAMIInRegion('us-east-1', '2012', 'en')
        self.assertIsNotNone(image, 'Did not find a Windows 2012 AMI in us-east-1 for English locale')

    def test_FindAMI_ComplexVersion__us_east_1(self):
        image = self.finder.findWindowsAMIInRegion('us-east-1', '2008 R2 SP1', 'en')
        self.assertIsNotNone(image, 'Did not find a Windows 2008 AMI in us-east-1 for English locale')

    def test_FindAMI_BasicVersion__DifferentLocale(self):
        image = self.finder.findWindowsAMIInRegion('us-east-1', '2012', 'fr')
        self.assertIsNotNone(image, 'Did not find a Windows 2012 AMI in us-east-1 for French locale')

    def test_FindAMI_invalid_locale(self):
        image = self.finder.findWindowsAMIInRegion('us-east-1', '2012', 'xx')
        self.assertIsNone(image, 'xx locale does not exist')

    def test_FindAMI_invalid_region(self):
        image = self.finder.findWindowsAMIInRegion('xx-east-1', '2012', 'en')
        self.assertIsNone(image, 'xx-east-1 region does not exist')

if __name__ == '__main__':
    unittest.main()