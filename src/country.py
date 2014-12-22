class Country():
	def __init__(self):
		self.area = None

	def add_area(self, list_of_points):
		if not self._check_inline(list_of_points):
			self.area = Area(list_of_points)

	def _check_inline(self, list_of_points):
		if len(list_of_points) > 2:
			before_point = None
			before_incline = None
			for point in list_of_points:
				if before_point:
					x = (before_point[0] - point[0])
					incline = (before_point[1] - point[1])/x if x else 999999999999999999
				if before_incline == None:
					before_incline = incline
				elif before_incline != incline:
					return False
				before_point = point
		return True

class Area():
	def __init__(self, points):
		self.points = points
		self.residents = []

	def add_resident(self, resident):
		for r in self.residents:
			if r.element == resident.element:
			return
		self.residents.append(resident)

	def population(self):
		return len(self.residents)
