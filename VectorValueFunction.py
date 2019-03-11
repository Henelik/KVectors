from Point3d import Point3d
from Vector3d import Vector3d
from sympy.abc import t
from sympy import *

class VectorValueFunction3d(): # A function which takes a scalar and returns a vector
	def __init__(self, xSymbol, ySymbol, zSymbol):
		self.xSymbol = xSymbol
		self.ySymbol = ySymbol
		self.zSymbol = zSymbol

	def derivative(self, n = 1): # return the nth derivative
		if n == 0: return self
		elif n < 0: raise(Exception)
		else:
			xTemp = diff(self.xSymbol, t)
			yTemp = diff(self.ySymbol, t)
			zTemp = diff(self.zSymbol, t)
			for i in range(n-1):
				xTemp = diff(xTemp, t)
				yTemp = diff(yTemp, t)
				zTemp = diff(zTemp, t)
			return VectorValueFunction3d(xTemp, yTemp, zTemp)

	def integral(self, n = 1): # return the nth integral
		if n == 0: return self
		elif n < 0: raise(Exception)
		else:
			xTemp = integrate(self.xSymbol, t)
			yTemp = integrate(self.ySymbol, t)
			zTemp = integrate(self.zSymbol, t)
			for i in range(n-1):
				xTemp = integrate(xTemp, t)
				yTemp = integrate(yTemp, t)
				zTemp = integrate(zTemp, t)
			return VectorValueFunction3d(xTemp, yTemp, zTemp)

	def evaluate(self, value):
		if type(self.xSymbol) == int or type(self.xSymbol) == float:
			xTemp = self.xSymbol
		else:
			xTemp = self.xSymbol.evalf(5, subs={t: value})

		if type(self.ySymbol) == int or type(self.ySymbol) == float:
			yTemp = self.ySymbol
		else:
			yTemp = self.ySymbol.evalf(5, subs={t: value})

		if type(self.zSymbol) == int or type(self.zSymbol) == float:
			zTemp = self.zSymbol
		else:
			zTemp = self.zSymbol.evalf(5, subs={t: value})

		return Point3d(xTemp, yTemp, zTemp)

	def tangentVector(self, value): # find the non-unit tangent vector at the given value
		if type(self.xSymbol) == int or type(self.xSymbol) == float:
			xTail = self.xSymbol
			xHead = 0
		else:
			xTail = self.xSymbol.evalf(5, subs={t: value})
			xHead = diff(self.xSymbol, t).evalf(5, subs={t: value})

		if type(self.ySymbol) == int or type(self.ySymbol) == float:
			yTail = self.ySymbol
			yHead = 0
		else:
			yTail = self.ySymbol.evalf(5, subs={t: value})
			yHead = diff(self.ySymbol, t).evalf(5, subs={t: value})

		if type(self.zSymbol) == int or type(self.zSymbol) == float:
			zTail = self.zSymbol
			zHead = 0
		else:
			zTail = self.zSymbol.evalf(5, subs={t: value})
			zHead = diff(self.zSymbol, t).evalf(5, subs={t: value})

		return Vector3d(Point3d(xTail, yTail, zTail), Point3d(xHead+xTail, yHead+yTail, zHead+zTail))

	def normalVector(self, value): # not unit length
		dx = diff(self.xSymbol, t)
		dy = diff(self.ySymbol, t)
		dz = diff(self.zSymbol, t)
		tanMagnitude = sqrt(dx**2 + dy**2 + dz**2)

		dx2 = diff(dx/tanMagnitude, t)
		dy2 = diff(dy/tanMagnitude, t)
		dz2 = diff(dz/tanMagnitude, t)

		if type(self.xSymbol) == int or type(self.xSymbol) == float:
			xTail = self.xSymbol
		else:
			xTail = self.xSymbol.evalf(subs={t: value})
		if type(self.ySymbol) == int or type(self.ySymbol) == float:
			yTail = self.ySymbol
		else:
			yTail = self.ySymbol.evalf(subs={t: value})
		if type(self.zSymbol) == int or type(self.zSymbol) == float:
			zTail = self.zSymbol
		else:
			zTail = self.zSymbol.evalf(subs={t: value})

		if type(dx2) == int or type(dx2) == float:
			xHead = dx2
		else:
			xHead = dx2.evalf(subs={t: value})
		if type(dy2) == int or type(dy2) == float:
			yHead = dy2
		else:
			yHead = dy2.evalf(subs={t: value})
		if type(dz2) == int or type(dz2) == float:
			zHead = dz2
		else:
			zHead = dz2.evalf(subs={t: value})

		return Vector3d(Point3d(xTail, yTail, zTail), Point3d(xHead+xTail, yHead+yTail, zHead+zTail))

	def accelerationVector(self, value):
		if type(self.xSymbol) == int or type(self.xSymbol) == float:
			xTail = self.xSymbol
			xHead = 0
		else:
			xTail = self.xSymbol.evalf(subs={t: value})
			xHead = diff(diff(self.xSymbol, t)).evalf(subs={t: value})

		if type(self.ySymbol) == int or type(self.ySymbol) == float:
			yTail = self.ySymbol
			yHead = 0
		else:
			yTail = self.ySymbol.evalf(subs={t: value})
			yHead = diff(diff(self.ySymbol, t)).evalf(subs={t: value})

		if type(self.zSymbol) == int or type(self.zSymbol) == float:
			zTail = self.zSymbol
			zHead = 0
		else:
			zTail = self.zSymbol.evalf(subs={t: value})
			zHead = diff(diff(self.zSymbol, t)).evalf(subs={t: value})

		return Vector3d(Point3d(xTail, yTail, zTail), Point3d(xHead+xTail, yHead+yTail, zHead+zTail))

	def tangentialAcceleration(self, value):
		dx = diff(self.xSymbol, t)
		dy = diff(self.ySymbol, t)
		dz = diff(self.zSymbol, t)
		tanMagnitude = sqrt(dx**2 + dy**2 + dz**2)

		return diff(tanMagnitude, t).evalf(subs={t: value})

	def normalAcceleration(self, value):
		return sqrt(self.accelerationVector(value).magnitude()**2 - self.tangentialAcceleration(value)**2).evalf(subs={t: value})

	def __repr__(self):
		return "<" + str(self.xSymbol) + ", " + str(self.ySymbol) + ", " + str(self.zSymbol) + ">"

if __name__ == "__main__":
	xSym = t**3
	ySym = 5*t
	zSym = 20
	test = VectorValueFunction3d(xSym, ySym, zSym)
	print(test)
	print()
	print("Derivatives:")
	print(test.derivative(1))
	print(test.derivative(2))
	print()
	print("Integrals:")
	print(test.integral(1))
	print(test.integral(2))
	print()
	print("Tangent vector:")
	print(test.tangentVector(5))
	print()
	print("Normal vector:")
	print(test.normalVector(5))
	print()
	print("Acceleration:")
	print(test.accelerationVector(5))
	print("Tangential acceleration:")
	print(test.tangentialAcceleration(5))
	print("Normal acceleration:")
	print(test.normalAcceleration(5))
	#for i in range(0, 10):
	#	print(test.evaluate(i))
