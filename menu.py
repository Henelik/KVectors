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
		choice = "0"
		subchoice = "0"

		print("Main Menu")
		print()
		print("Choose an object to test:")
		print()
		print("	1. Point3d")
		print("	2. Vector3d")
		print("	3. Plande3d")
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
				pass
			elif subchoice == 4:
				choice = 0
