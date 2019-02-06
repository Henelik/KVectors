import Point3d
import math
from random import randrange
import time

Point3d = Point3d.Point3d

class Vector3d():
	def __init__(self, *args):
		if len(args) == 0:
			self.tail = Point3d(0, 0, 0)
			self.head = Point3d(1, 1, 1)
		elif len(args) == 2:
			if type(args[0]) == Point3d and type(args[1]) == Point3d:
				self.tail = args[0]
				self.head = args[1]
		else: raise(TypeError)

	def magnitude(self):
		return self.tail.distance(self.head)

	def normalize(self):
		return(self//self.magnitude())

	def __floordiv__(self, num): # Floor division operator is used because of a 3.x Python "feature" that prevents divisions between objects and ints
		return Vector3d(self.tail, Point3d(tuple(comp/num for comp in self.head-self.tail))+self.tail)

	def __div__(self, num):
		return Vector3d(self.tail, Point3d(tuple(comp/num for comp in self.head-self.tail))+self.tail)

	def __mul__(self, other): # dot product
		if type(other) in (int, float):
			return Vector3d(self.tail, Point3d(tuple(comp*other for comp in self.head-self.tail))+self.tail)
		return sum(x*y for y in self.head-self.tail for x in other.head-other.tail)

	def __pow__(self, other): # cross product
		a = self.head-self.tail
		b = other.head-other.tail
		return Vector3d(Point3d(0, 0, 0), Point3d([a[1]*b[2]-a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]))

	def __repr__(self):
		return "Vector3d object: "+str(self.tail)+" to "+str(self.head)


if __name__ == "__main__":
	tail = Point3d(5, 2, 6)
	head = Point3d(3, 4, 7)
	test = Vector3d(tail, head)
	test2 = Vector3d()
	print("Created " + str(test))
	print("The magnitude is " + str(test.magnitude())) # This should return sqrt(3), or 1.7320508075688772
	print("The normalized vector is: " + str(test.normalize())) # should return a unit vector
	print("The normalized vector's magnitude is " + str(test.normalize().magnitude())) # should return 1.0, the magnitude of a unit vector
	print("Double the original vector is " + str(test*2))
	print("The double vector's magnitude is " + str((test*2).magnitude()))
	print("Test dot product: " + str(test*test2))

	t = time.time()
	for i in range(1000): # for performance test purposes.  Set range to 0 to disable.
		tail = Point3d(randrange(-1000, 1000), randrange(-1000, 1000), randrange(-1000, 1000))
		head = Point3d(randrange(-1000, 1000), randrange(-1000, 1000), randrange(-1000, 1000))
		test = Vector3d(tail, head)
		str(test) # representation test
		test.magnitude() # This should return sqrt(3), or 1.7320508075688772
		test.normalize() # should return a unit vector
		test.normalize().magnitude() # should return 1.0, the magnitude of a unit vector
		test*2 # lengthen
		test//2 # shorten
		(test*2).magnitude()
		test*test2 # dot product
		test**test2 # cross product
	print("Test time was " + str(time.time()-t) + " seconds.")
	
# Sample run:
#
#Created Vector3d object: (5, 2, 6) to (3, 4, 7)
#The magnitude is 3.0
#The normalized vector is: Vector3d object: (5, 2, 6) to (4.333333333333333, 2.6666666666666665, 6.333333333333333)
#The normalized vector's magnitude is 1.0
#Double the original vector is Vector3d object: (5, 2, 6) to (1, 6, 8)
#The double vector's magnitude is 6.0
#[Finished in 0.1s]