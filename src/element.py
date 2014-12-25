class Element():
	element_types = ["FIRE"]
	
	@classmethod
	def getId(cls, element):
		for i, j in enumerate(cls.element_types):
			if j == element: return i