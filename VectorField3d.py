from Point3d import Point3d
from Vector3d import Vector3d
from Plane3d import Plane3d
from VectorValueFunction import VectorValueFunction3d

from sympy.abc import x, y, z
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication

class VectorField3d():
	def __init__(self, xSymbol, ySymbol, zSymbol):
		self.xSymbol = xSymbol
		self.ySymbol = ySymbol
		self.zSymbol = zSymbol

	def gradient(self, n=1):
		if n == 0: return self
		elif n < 0: raise(Exception)
		else:
			xTemp = diff(self.xSymbol, x)
			yTemp = diff(self.ySymbol, y)
			zTemp = diff(self.zSymbol, z)
			for i in range(n-1):
				xTemp = diff(xTemp, x)
				yTemp = diff(yTemp, y)
				zTemp = diff(zTemp, z)
			return VectorField3d(xTemp, yTemp, zTemp)

	def antiGradient(self, n=1):
		if n == 0: return self
		elif n < 0: raise(Exception)
		else:
			xTemp = integrate(self.xSymbol, x)
			yTemp = integrate(self.ySymbol, y)
			zTemp = integrate(self.zSymbol, z)
			for i in range(n-1):
				xTemp = integrate(xTemp, x)
				yTemp = integrate(yTemp, y)
				zTemp = integrate(zTemp, z)
			return VectorField3d(xTemp, yTemp, zTemp)

	def evaluate(self, xValue, yValue, zValue):
		if type(self.xSymbol) == int or type(self.xSymbol) == float:
			xTemp = self.xSymbol
		else:
			xTemp = self.xSymbol.evalf(5, subs={x: value})

		if type(self.ySymbol) == int or type(self.ySymbol) == float:
			yTemp = self.ySymbol
		else:
			yTemp = self.ySymbol.evalf(5, subs={y: value})

		if type(self.zSymbol) == int or type(self.zSymbol) == float:
			zTemp = self.zSymbol
		else:
			zTemp = self.zSymbol.evalf(5, subs={z: value})
		h = Point3d(xValue, yValue, zValue)
		p = Point3d(xTemp, yTemp, zTemp)
		return Vector3d(h, h+p)

	def curlFunc(self):
		pass

	def curlValue(self, xValue, yValue, zValue):
		pass

	def divergenceFunc(self):
		pass

	def divergenceValue(self, xValue, yValue, zValue):
		pass
