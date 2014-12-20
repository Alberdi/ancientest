import unittest

import country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.c = country.Country()

    # Countries have an area defined by a list of points
    def test_add_area(self):
        # Two points don't make a valid area
        self.c.add_area([(0,0), (100,100)])
        self.assertIsNone(self.c.area)
        # Three points in a line isn't a valid area either
        self.c.add_area([(0,0), (100,100), (200,200)])
        self.assertIsNone(self.c.area)
        # A triangle is a valid area
        self.c_add_area([(0,0), (100,0), (100,100)])
        self.assertIsNotNone(self.c.area)

