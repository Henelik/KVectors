from Point3d import Point3d
from Vector3d import Vector3d
from VectorValueFunction import VectorValueFunction3d
from sympy.abc import x, y
from sympy import *

class QuadricSurface():
	def __init__(self, sym):
		self.sym = sym

	def __repr__(self):
		return("f(x, y) = " + str(self.sym))

	def gradient(self):
		return (diff(self.sym, x), diff(self.sym, y))

	def hessian(self):
		return self.fxx()*self.fyy()-self.fxy()**2

	def fx(self):
		return diff(self.sym, x)

	def fy(self):
		return diff(self.sym, y)

	def fxx(self):
		return diff(self.fx(), x)

	def fyy(self):
		return diff(self.fy(), y)

	def fxy(self):
		return diff(self.fx(), y)

	def fyx(self):
		return self.fxy()

	def directionalDerivative(self, xPos, yPos, direction):
		direction = Vector3d((0, 0, 0), (direction[0], direction[1], 0)).normalize()
		grad = self.gradient()
		grad = Vector3d((0, 0, 0), (grad[0].evalf(subs={x: xPos, y: yPos}), grad[1].evalf(subs={x: xPos, y: yPos}), 0))
		return grad*direction

if __name__ == "__main__":
	#sym = x**3 + 1/y
	sym = 3*y**2 - 2*y**3 - 3*x**2 + 6*x*y
	test = QuadricSurface(sym)
	print(test)
	print()
	print(test.gradient())
	print(test.hessian())
	print(test.directionalDerivative(1, 1, (1, 1)))