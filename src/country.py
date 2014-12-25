from element import Element

class Country():
	def __init__(self):
		self.area = None
		self.element = None

	def add_area(self, list_of_points):
		if not self._check_inline(list_of_points):
			self.area = Area(list_of_points, self)

	def is_enemy(self, other):
		if not self.area or not other.area:
			return False
		for point in self.area.points:
			if other.area.point_inside(point):
				return True
		for point in other.area.points:
			if self.area.point_inside(point):
				return True
		return self.area.intersects(other.area)

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
	
	def strength(self):
		strength = 0
		for resident in self.area.residents:
			strength += resident.get_strength_to(self.element)
		return strength
	
	def change_element(self, new_element):
		self.element = Element.getId(new_element)

class Area():
	def __init__(self, points, country):
		self.points = points
		self.country = country
		self.residents = []

	def add_resident(self, resident):
		for r in self.residents:
			if r.element == resident.element:
				return
		self.residents.append(resident)
		resident.add_residence(self)

	def intersects(self, other):
		p1 = self.points
		p2 = other.points
		for i in xrange(len(p1)):
			for j in xrange(len(p2)):
				if p1[i-1] in [p2[j-1], p2[j]] or p1[i] in [p2[j-1], p2[j]]:
					continue
				if self._segment_intersect((p1[i-1], p1[i]), (p2[j-1], p2[j])):
					return True
		return False

	def population(self):
		return len(self.residents)
	
	def point_inside(self, point):
		intersections = 0
		prev_vertex = self.points[len(self.points)-1]
		for vertex in self.points:
			if vertex[0] == point[0] and vertex[1] == point[1]:
				return False
			if prev_vertex[1] == vertex[1] and prev_vertex[1] == point[1] and point[0] > min(prev_vertex[0], vertex[0]) and point[0] < max(prev_vertex[0], vertex[0]): #On a horizontal line
				return False
			if point[1] > min(prev_vertex[1], vertex[1]) and point[1] <= max(prev_vertex[1], vertex[1]) and point[0] < max(prev_vertex[0], vertex[0]) and prev_vertex[1] != vertex[1]:
				xinters = (point[1] - prev_vertex[1]) * (vertex[0] - prev_vertex[0]) / (vertex[1] - prev_vertex[1]) + prev_vertex[0];
				if xinters == point[0]: #On a line
					return False
				if prev_vertex[0] == vertex[0] or point[0] <= xinters:
					intersections += 1
			prev_vertex = vertex
		if intersections % 2 != 0:
			return True
		return False

	def _segment_intersect(self, s1, s2):
		# ccw = counter clock wise, aka magic
		# Check http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
		ccw = lambda p1, p2, p3: cmp((p3[1]-p1[1])*(p2[0]-p1[0]) - (p2[1]-p1[1])*(p3[0]-p1[0]), 0)
		return ccw(s1[0], s1[1], s2[0]) != ccw(s1[0], s1[1], s2[1]) and \
				ccw(s2[0], s2[1], s1[0]) != ccw(s2[0], s2[1], s1[1])

