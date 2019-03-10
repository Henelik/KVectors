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

	def Evaluate(self, t):
		return Point3d(self.xSymbol, self.ySymbol, self.zSymbol)

	def TangentVector(self, t):
		pass

	def NormalVector(self, t):
		pass

	def AccelerationVector(self, t):
		pass

	def TangentAccelerationVector(self, t):
		pass

	def NormalAccelerationVector(self, t):
		pass

	def __repr__(self):
		return "<" + str(self.xSymbol) + ", " + str(self.ySymbol) + ", " + str(self.zSymbol) + ">"

if __name__ == "__main__":
	xSym = t**3
	ySym = 5*t
	zSym = 20
	test = VectorValueFunction3d(xSym, ySym, zSym)
	print(test)
	print("Derivatives:")
	print(test.derivative(1))
	print(test.derivative(2))
	print("Integrals:")
	print(test.integral(1))
	print(test.integral(2))
