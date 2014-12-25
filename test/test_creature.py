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
