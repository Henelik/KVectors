from Point3d import Point3d
from Vector3d import Vector3d
from Plane3d import Plane3d
from VectorValueFunction import VectorValueFunction3d
from QuadricSurface import QuadricSurface
from VectorField3d import VectorField3d
from PotentialFunction3d import PotentialFunction3d

from sympy.abc import t, x, y, z
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication

def getPointsInput():
	print("Enter the coordinates for a point (x, y, z):")
	coords1 = eval(input())
	print()
	print("Enter the coordinates for a second point (x, y, z):")
	coords2 = eval(input())
	print()
	return(list(coords1), list(coords2))

if __name__ == "__main__":
	print()
	print()
	print("Welcome to the KVectors module test menu!")
	print()
	while(True):
		choice = 0
		subchoice = 0
		transformations = standard_transformations + (implicit_multiplication,)
		testVec = None
		testPlane = None
		testVVF = None
		testSurf = None
		testPot = None
		testField = None

		print("Main Menu")
		print()
		print("Choose an object to test:")
		print()
		print("	1. Point3d")
		print("	2. Vector3d")
		print("	3. Plane3d")
		print("	4. VectorValueFunction3d")
		print("	5. Quadric Surface")
		print("	6. Potential Funtion")
		print("	7. Vector Field")
		choice = eval(input())
		print()
		print()
		while(choice == 1):
			print("Testing Point3d")
			print()
			print("	1. Add 2 points")
			print("	2. Subtract 2 points")
			print("	3. Find the distance between 2 points")
			print("	4. Return to main menu")
			subchoice = eval(input())
			print()
			print()
			if subchoice == 1:
				coords = getPointsInput()
				p1 = Point3d(coords[0])
				p2 = Point3d(coords[1])
				print(str(p1) + " + " + str(p2) + " = " + str(p1+p2))
				print()
			elif subchoice == 2:
				coords = getPointsInput()
				p1 = Point3d(coords[0])
				p2 = Point3d(coords[1])
				print(str(p1) + " - " + str(p2) + " = " + str(p1-p2))
				print()
			elif subchoice == 3:
				coords = getPointsInput()
				p1 = Point3d(coords[0])
				p2 = Point3d(coords[1])
				print("The distance between " + str(p1) + " and " + str(p2) + " is " + str(p1.distance(p2)))
				print()
			elif subchoice == 4:
				choice = 0
		while(choice == 2):
			print("Testing Vector3d")
			print("Stored vector is " + str(testVec))
			print()
			print("	1. Create a vector to test")
			print("	2. Get the magnitude of the stored vector")
			print("	3. Normalize the stored vector")
			print("	4. Find the angle between the stored vector and another vector")
			print("	5. Offset the vector")
			print("	6. Scale the vector")
			print("	7. Get a point on the vector")
			print("	8. Dot product with another vector")
			print("	9. Cross product with another vector")
			print("	10. Return to main menu")
			subchoice = eval(input())
			print()
			print()
			if subchoice == 1: # Create a vector to test
				coords = getPointsInput()
				p1 = Point3d(coords[0])
				p2 = Point3d(coords[1])
				testVec = Vector3d(p1, p2)
				print("The stored vector is now " + str(testVec))
				print()
			elif subchoice == 2: # Get the magnitude of the stored vector
				if testVec:
					print(testVec.magnitude())
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 3: # Normalize the stored vector
				if testVec:
					testVec = testVec.normalize()
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 4: # Find the angle between the stored vector and another vector
				if testVec:
					coords = getPointsInput()
					p1 = Point3d(coords[0])
					p2 = Point3d(coords[1])
					testVec2 = Vector3d(p1, p2)
					print("The angle between the vectors is " + str(testVec.angleBetween(testVec2)) + " radians.")
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 5: # Offset the vector
				if testVec:
					print("Enter the amount to offset the vector by (x, y, z)")
					p1 = Point3d(eval(input()))
					testVec = testVec+p1
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 6: # Scale the vector
				if testVec:
					print("Enter the amount to scale the vector by")
					testVec = testVec*eval(input())
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 7: # Index the vector
				if testVec:
					print("Enter a ratio to get the point that far along the vector")
					print("0 for the head, 1 for the tail, .5 for the midpoint, larger than 1 to extrapolate")
					print(testVec[eval(input())])
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 8: # Dot product
				if testVec:
					coords = getPointsInput()
					p1 = Point3d(coords[0])
					p2 = Point3d(coords[1])
					testVec2 = Vector3d(p1, p2)
					print("The dot product of the vectors is " + str(testVec*testVec2))
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 9: # Cross product
				if testVec:
					coords = getPointsInput()
					p1 = Point3d(coords[0])
					p2 = Point3d(coords[1])
					testVec2 = Vector3d(p1, p2)
					print("The cross product of the vectors is " + str(testVec**testVec2))
					print()
				else:
					print("No stored vector!  Create a vector first.")
			elif subchoice == 10:
				choice = 0
		while(choice == 3):
			print("Testing Plane3d")
			print("Stored plane is " + str(testPlane))
			print()
			print("	1. Construct a plane with a normal vector")
			print("	2. Construct a plane with 3 points")
			print("	3. Test if a point is on the stored plane")
			print("	4. Return to main menu")
			subchoice = eval(input())
			print()
			print()
			if subchoice == 1:
				coords = getPointsInput()
				p1 = Point3d(coords[0])
				p2 = Point3d(coords[1])
				testPlane = Plane3d(p1, p2)
				print()
			elif subchoice == 2:
				coords = getPointsInput()
				p1 = Point3d(coords[0])
				p2 = Point3d(coords[1])
				print("Enter the coordinates for a third point (x, y, z):")
				p3 = Point3d(input())
				testPlane = Plane3d(p1, p2, p3)
				print()
			elif subchoice == 3:
				if testPlane:
					print("Enter the coordinates for a point (x, y, z):")
					p1 = Point3d(input())
					if p1 in testPlane:
						print("The entered point is in the plane.")
					else:
						print("The entered point is not in the plane.")
					print()
				else:
					print("No stored plane!  Create a plane first.")
			elif subchoice == 4:
				choice = 0
		while(choice == 4):
			print("Testing Vector Valued Function")
			print("Stored VVF is " + str(testVVF))
			print()
			print("	1. Create Vector Value Function")
			print("	2. Print derivative of VVF")
			print("	3. Print integral of VVF")
			print("	4. Evaluate at a given t")
			print("	5. Get unit tangent vector at a given t")
			print("	6. Get unit normal vector at a given t")
			print("	7. Get velocity vector at a given t")
			print("	8. Get acceleration vector at a given t")
			print("	9. Return to main menu")
			subchoice = eval(input())
			print()
			print()
			if subchoice == 1:
				xSym = parse_expr(input("x(t) = "), transformations=transformations)
				ySym = parse_expr(input("y(t) = "), transformations=transformations)
				zSym = parse_expr(input("z(t) = "), transformations=transformations)
				testVVF = VectorValueFunction3d(xSym, ySym, zSym)
			elif subchoice == 2:
				print(testVVF.derivative())
			elif subchoice == 3:
				print(testVVF.integral())
			elif subchoice == 4:
				v1 = Point3d(eval(input("Enter a value for t: ")))
				print()
				print(testVVF.evaluate(v1))
			elif subchoice == 5:
				v1 = Point3d(eval(input("Enter a value for t: ")))
				print()
				print(testVVF.tangentVector(v1).normalize())
			elif subchoice == 6:
				v1 = Point3d(eval(input("Enter a value for t: ")))
				print()
				print(testVVF.normalVector(v1).normalize())
			elif subchoice == 7:
				v1 = Point3d(eval(input("Enter a value for t: ")))
				print()
				print(testVVF.tangentVector(v1))
			elif subchoice == 8:
				v1 = Point3d(eval(input("Enter a value for t: ")))
				print()
				print(testVVF.accelerationVector(v1))
			elif subchoice == 9:
				choice = 0
		while(choice == 5):
			print("Testing QuadricSurface")
			print("Stored surface is " + str(testSurf))
			print()
			print("	1. Create a quadric surface to test")
			print("	2. Print all first and second derivatives of surface")
			print("	3. Print gradient of surface")
			print("	4. Print Hessian of surface")
			print("	5. Get rate of increase at a specified point and direction")
			print("	6. Return to main menu")
			subchoice = eval(input())
			print()
			print()
			if subchoice == 1:
				sym = parse_expr(input("f(x, y) = "), transformations=transformations)
				testSurf = QuadricSurface(sym)
			elif subchoice == 2:
				print("fx(x, y) = " + str(testSurf.fx()))
				print("fy(x, y) = " + str(testSurf.fy()))
				print("fxx(x, y) = " + str(testSurf.fxx()))
				print("fyy(x, y) = " + str(testSurf.fyy()))
				print("fxy(x, y) = " + str(testSurf.fxy()))
				print("fyx(x, y) = " + str(testSurf.fyx()))
			elif subchoice == 3:
				print(str(testSurf.gradient()))
			elif subchoice == 4:
				print(str(testSurf.hessian()))
			elif subchoice == 5:
				pos = eval(input("Enter a 2d position (x, y): "))
				direction = eval(input("Enter a 2d direction (x, y): "))
				print(testSurf.directionalDerivative(pos[0], pos[1], direction))
			elif subchoice == 6:
				choice = 0
		while(choice==6):
			print("Testing PotentialFunction3d")
			print("Stored function is " + str(testPot))
			print()
			print("	1. Create a potential function to test")
			print("	2. Print all partial derivatives of potential function")
			print("	3. Evaluate the potential function at a point")
			print("	4. Return to main menu")
			subchoice = eval(input())
			if subchoice == 1:
				sym = parse_expr(input("f(x, y, z) = "), transformations=transformations)
				testPot = PotentialFunction3d(sym)
			elif subchoice == 2:
				if testPot:
					print("Partial x derivative: " + str(testPot.partialDerivative(x)))
					print("Partial y derivative: " + str(testPot.partialDerivative(y)))
					print("Partial z derivative: " + str(testPot.partialDerivative(z)))
			elif subchoice == 3:
				if testPot:
					print("Enter the coordinates for a point (x, y, z):")
					coords = eval(input())
					print(testPot.evaluate(coords[0], coords[1], coords[2]))
			elif subchoice == 4:
				choice = 0
		while(choice==7):
			print("Testing VectorField3d")
			print("Stored field is " + str(testField))
			print()
			print("	1. Create a vector field to test")
			print("	2. Print gradient of field")
			print("	3. Print anti-gradient of field")
			print("	4. Evaluate the field at a point")
			print("	5. Print the curl function of the field")
			print("	6. Evaluate the curl at a point")
			print("	7. Print the divergence function of the field")
			print("	8. Evaluate the divergence at a point")
			print("	9. Return to main menu")
			subchoice = eval(input())
			if subchoice == 1:
				xSym = parse_expr(input("m(x, y, z) = "), transformations=transformations)
				ySym = parse_expr(input("N(x, y, z) = "), transformations=transformations)
				zSym = parse_expr(input("P(x, y, z) = "), transformations=transformations)
				testField = VectorField3d(xSym, ySym, zSym)
			elif subchoice == 2:
				if testField:
					print(testField.gradient())
			elif subchoice == 3:
				if testField:
					print(testField.antiGradient())
			elif subchoice == 4:
				if testField:
					print("Enter the coordinates for a point (x, y, z):")
					coords = eval(input())
					print(testField.evaluate(coords[0], coords[1], coords[2]))
			elif subchoice == 5:
				if testField:
					print(testField.curlFunc())
			elif subchoice == 6:
				if testField:
					print("Enter the coordinates for a point (x, y, z):")
					coords = eval(input())
					print(testField.curlValue(coords[0], coords[1], coords[2]))
			elif subchoice == 7:
				if testField:
					print(testField.divergenceFunc())
			elif subchoice == 8:
				if testField:
					print("Enter the coordinates for a point (x, y, z):")
					coords = eval(input())
					print(testField.divergenceValue(coords[0], coords[1], coords[2]))
			elif subchoice == 9:
				choice = 0
