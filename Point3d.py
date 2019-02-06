import math

class Point3d():
	def __init__(self, *args):
		if len(args) == 0:
			self.values = [0, 0, 0]
		elif len(args) == 1:
			self.values = list(args[0]) # convert to list to support assignment
		elif len(args) == 3:
			self.values = list(args) # convert to list to support assignment
		else: raise(TypeError)

	def distance(self, other):
		if type(other) != Point3d:
			raise(TypeError)
		return math.sqrt(sum(comp**2 for comp in self-other))

	def __add__(self, other):
		return Point3d(self.values[0] + other.values[0], self.values[1] + other.values[1], self.values[2] + other.values[2])

	def __sub__(self, other):
		return Point3d(self.values[0] - other.values[0], self.values[1] - other.values[1], self.values[2] - other.values[2])

	def __repr__(self):
		return str(tuple(self.values)) # cast to tuple before string so parenthesis are used

	def __getitem__(self, key):
		return self.values[key]

	def __iter__(self):
		return self.values.__iter__()


if __name__ == "__main__":
	test = Point3d(3, 4, 7)
	print(test) # prints the point's representation: "(3, 4, 7)"
