import unittest

import country, creature

class TestCreature(unittest.TestCase):
	def setUp(self):
		self.c = creature.Creature()
		
	def test_where_do_i_live(self):
		country1 = country.Country()
		country1.add_area([(0,0), (100,0), (100, 100)])
		country2 = country.Country()
		country2.add_area([(0,0), (100, 0), (100, -100)])
		self.assertIsNone(self.c.where_do_i_live())
		country1.area.add_resident(self.c)
		self.assertEqual(self.c.where_do_i_live(), country1)
		country2.area.add_resident(self.c)
		self.assertEqual(self.c.where_do_i_live(), country2)
		
	#A criature can only travel to adjacent country
	def test_travel(self):
		country1 = country.Country()
		country1.add_area([(0,0), (100,0), (100, 100)])
		country2 = country.Country()
		country2.add_area([(0,0), (100, 0), (100, -100)])
		country3 = country.Country()
		country3.add_area([(200,0), (500, 0), (200, 200)])
		country1.area.add_resident(self.c)
		self.c.travel(country2)
		self.assertEqual(self.c.where_do_i_live(), c2)
		self.c.travel(country3)
		self.assertEqual(self.c.where_do_i_live(), c2)