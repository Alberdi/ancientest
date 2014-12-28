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
		creature1 = creature.Creature()
		creature2 = creature.Creature()
		# Initially an area is empty
		self.assertEqual(self.c.area.population(), 0)
		self.c.area.add_resident(creature1);
		self.assertEqual(self.c.area.population(), 1)
		self.c.area.add_resident(creature2)
		self.assertEqual(self.c.area.population(), 1)

	def test_point_inside(self):
		self.c.add_area([(0,0), (100,0), (100, 100)])
		self.assertTrue(self.c.area.point_inside((80,20)))
		self.assertFalse(self.c.area.point_inside((20,80)))
		self.assertFalse(self.c.area.point_inside((100,100)))
		
	#Two countries are enemies if they claim the same place
	def test_is_enemy(self):
		c2 = country.Country()
		c3 = country.Country()
		self.c.add_area([(0,0), (100, 0), (100,100)])
		self.assertFalse(self.c.is_enemy(c2))
		c2.add_area([(0,0), (100, 0), (100, -100)])
		self.assertFalse(self.c.is_enemy(c2))
		c3.add_area([(20,50), (70, 30), (60, 100)])
		self.assertTrue(self.c.is_enemy(c3))

	# Creatures on a country give it strength
	def test_strength(self):
		self.c.add_area([(0,0), (100,0), (100,100)])
		self.assertEqual(self.c.strength(), 0)
		creature1 = creature.Creature()
		self.c.area.add_resident(creature1)
		normal_creature_strength = self.c.strength()
		self.assertTrue(normal_creature_strength > 0)
		# A creature gives less strength if the country element doesn't match
		self.c.change_element("FIRE")
		self.assertTrue(normal_creature_strength > self.c.strength() > 0)
		# But gives more if the element does match
		creature1.change_element("FIRE")
		self.assertTrue(normal_creature_strength < self.c.strength())

	# Countries can fight enemy countries
	def test_fight(self):
		self.c.add_area([(0,0), (100, 0), (100, 100)])
		friendly_creature = creature.Creature()
		self.c.area.add_resident(friendly_creature)

		non_enemy_country = country.Country()
		non_enemy_country.add_area([(0,0), (100, 0), (100, -100)])
		non_enemy_creature = creature.Creature()
		non_enemy_country.area.add_resident(non_enemy_creature)
		# Can't fight non-enemy countries
		self.assertIsNone(self.c.fight(non_enemy_country))

		enemy_country = country.Country()
		enemy_country.add_area([(20,50), (70, 30), (60, 100)])
		enemy_creature = creature.Creature()
		enemy_creature.strength -= 2
		enemy_country.area.add_resident(enemy_creature)
		self.assertEqual(self.c.fight(enemy_country), self.c)
		self.assertEqual(self.c.strength(), 2)

	# Creatures on a country get paid to defend it
	def test_pay_upkeep(self):
		self.c.add_area([(0,0), (100, 0), (100, 100)])
		starting_coins = self.c.current_coins()
		creature = creature.Creature()
		self.c.area.add_resident(creature)
		self.c.pay_upkeep()
		first_payment = starting_coins - self.c.current_coins()
		self.assertTrue(payment > 0)

		# Matching creatures are free
		self.c.change_element("FIRE")
		creature.change_element("FIRE")
		self.c.pay_upkeep()
		matching_payment = starting_coins - first_payment - self.c.current_coins()
		self.assertTrue(matching_payment == 0)

		# Opposite creatures pay more
		creature.change_element("WATER")
		self.c.pay_upkeep()
		opposite_payment = starting_coins - first_payment - self.c.current_coins()
		self.assertTrue(opposite_payment > first_payment)

		# Creatures will leave if they can't be paid
		while creature.where_do_i_live() == self.c:
			self.c.pay_upkeep()
		self.assertNotEqual(creature.where_do_i_live(), self.c)

