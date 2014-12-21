import unittest

import country, creature

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
        self.c.add_area([(0,0), (100,0), (100,100)])
        self.assertIsNotNone(self.c.area)
        
    # One area can be populate to creatures
	def test_populate_area(self):
		self.c.add_area([(0,0), (100,0), (100, 100)])
		self.creature1 = creature.Creature()
		self.creature2 = creature.Creature()
		# Initially an area is empty
		assert self.c.area.population() == 0
        self.creature1 = creature.Creature()
        self.c.area.add_resident(creature1);
        assert self.c.area.population() == 1
        self.c.area.add_resident(creature2);
        assert self.c.area.population() == 1
		
		

