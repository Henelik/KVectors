from Point3d import Point3d
from Vector3d import Vector3d
from Plane3d import Plane3d
from VectorValueFunction import VectorValueFunction3d

from sympy.abc import x, y, z
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication

class PotentialFunction3d():
	def __init__(self, symbol):
		self.symbol = symbol

	def partialDerivative(self, glyph):
		return PotentialFunction3d(diff(self.symbol, glyph))

	def evaluate(self, xValue, yValue, zValue):
		return self.symbol.evalf(5, subs={x: xValue, y: yValue, z: zValue})

	def __repr__(self):
		return "Potential Function: " + str(self.symbol)

if __name__ == "__main__":
	print(PotentialFunction3d(x**2+2*y*z).partialDerivative(x))
