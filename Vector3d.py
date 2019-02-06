import Point3d
import math

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
		return(math.sqrt(sum(comp**2 for comp in self.head-self.tail)))

	def normalize(self):
		return(self.divide(self.magnitude()))

	def multiply(self, num):
		return Vector3d(self.tail, Point3d(tuple(comp*num for comp in self.head-self.tail))+self.tail)

	def divide(self, num):
		return Vector3d(self.tail, Point3d(tuple(comp/num for comp in self.head-self.tail))+self.tail)

	def __mul__(self, other): # dot product
		pass

	def __repr__(self):
		return "Vector3d object: "+str(self.tail)+" to "+str(self.head)


if __name__ == "__main__":
	tail = Point3d(5, 2, 6)
	head = Point3d(3, 4, 7)
	test = Vector3d(tail, head)
	#test = Vector3d()
	print("Created " + str(test))
	print("The magnitude is " + str(test.magnitude())) # This should return sqrt(3), or 1.7320508075688772
	print("The normalized vector is: " + str(test.normalize())) # should return a unit vector
	print("The normalized vector's magnitude is " + str(test.normalize().magnitude())) # should return 1.0, the magnitude of a unit vector
	print("Double the original vector is " + str(test.multiply(2)))
	print("The double vector's magnitude is " + str(test.multiply(2).magnitude()))
	
# Sample run:
#
#Created Vector3d object: (5, 2, 6) to (3, 4, 7)
#The magnitude is 3.0
#The normalized vector is: Vector3d object: (5, 2, 6) to (4.333333333333333, 2.6666666666666665, 6.333333333333333)
#The normalized vector's magnitude is 1.0
#Double the original vector is Vector3d object: (5, 2, 6) to (1, 6, 8)
#The double vector's magnitude is 6.0
#[Finished in 0.1s]