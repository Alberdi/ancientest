from element import Element

class Creature():
	def __init__(self):
		self.element = None
		self.residence = None
		self.strength = 10
	
	def add_residence(self, area):
		self.residence = area

	def get_strength_to(self, country_element):
		if country_element == None:
			return self.strength
		if country_element == self.element:
			return self.strength * 1.5
		else:
			return self.strength * 0.7
		
	def change_element(self, new_element):
		self.element = Element.getId(new_element)
	
	def where_do_i_live(self):
		if self.residence:
			return self.residence.country
		return None

