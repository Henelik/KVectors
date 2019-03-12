from Point3d import Point3d
from Vector3d import Vector3d
from Plane3d import Plane3d
from VectorValueFunction import VectorValueFunction3d
from sympy.abc import t
from sympy import *

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
		testVec = None
		testPlane = None

		print("Main Menu")
		print()
		print("Choose an object to test:")
		print()
		print("	1. Point3d")
		print("	2. Vector3d")
		print("	3. Plane3d")
		print("	4. VectorValueFunction3d")
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
