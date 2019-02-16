from Point3d import Point3d
from Vector3d import Vector3d
import math

class Plane3d():
	def __init__(self, *args):
		# We can create a plane by only creating a normal vector
		# The tail of the vector is a point in the plane
		# The centered normal is what is regularly the normal vector (really a point)
		if len(args) == 0: # default plane is y/z axis
			self.normal = Vector3d((0, 0, 0), (1, 0, 0))
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

if __name__ == "__main__":
	test = Plane3d((0, 0, 0), (0, 0, 1), (0, 1, 0))
	print(Point3d(0, 69, 420) in test)
	print(Vector3d() in  Plane3d())