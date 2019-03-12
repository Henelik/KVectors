from Point3d import Point3d
from Vector3d import Vector3d
import math

class Plane3d():
	def __init__(self, *args):
		# We can create a plane by only creating a normal vector
		# The tail of the vector is a point in the plane
		# The centered normal is what is regularly the normal vector (really a point)
		if len(args) == 0: # default plane is y/z axis
			self.normal = Vector3d((-2, 7, 11), (7, 4, -5))
		elif len(args) == 2: # If we were given 2 points (for a normal vector)
			self.normal = Vector3d(args[0], args[1])
		elif len(args) == 3: # If we were given 3 coplanar points
			self.normal = Vector3d(args[0], ((Vector3d(args[0], args[1])**Vector3d(args[0], args[2]))+args[0]).head)

	def __contains__(self, item):
		if type(item) == Point3d:
			# Use a dot product to determine if the point is in the plane
			return Vector3d(self.normal.tail, item)*self.normal == 0
		elif type(item) == Vector3d:
			return Vector3d(self.normal.tail, item.head)*self.normal == 0 and Vector3d(self.normal.tail, item.tail)*self.normal == 0
		else: raise(TypeError)

	def __repr__(self):
		n = self.normal.center()

		equation = ''

		if n[0] != 0:
			equation += str(n[0])
			if self.normal.tail[0] < 0:
				equation += "(x+" + str(abs(self.normal.tail[0])) + ")"
			elif self.normal.tail[0] > 0:
				equation += "(x-" + str(self.normal.tail[0]) + ")"
			else:
				equation += "x"

		if n[1] > 0:
			if equation:
				equation += " + "
		elif n[1] < 0:
			if equation:
				equation += " - "
		if n[1] != 0:
			equation += str(abs(n[1]))
			if self.normal.tail[1] < 0:
				equation += "(y+" + str(abs(self.normal.tail[1])) + ")"
			elif self.normal.tail[1] > 0:
				equation += "(y-" + str(self.normal.tail[1]) + ")"
			else:
				equation += "y"

		if n[2] > 0:
			if equation:
				equation += " + "
		elif n[2] < 0:
			if equation:
				equation += " - "
		if n[2] != 0:
			equation += str(abs(n[2]))
			if self.normal.tail[2] < 0:
				equation += "(z+" + str(abs(self.normal.tail[2])) + ")"
			elif self.normal.tail[2] > 0:
				equation += "(z-" + str(self.normal.tail[2]) + ")"
			else:
				equation += "z"

		equation += " = 0"

		return "A plane with the equation " + equation

if __name__ == "__main__":
	test = Plane3d((0, 0, 0), (0, 0, 1), (0, 1, 0))
	print(Point3d(0, 69, 420) in test)
	print(Vector3d() in  Plane3d())
	print(Plane3d())