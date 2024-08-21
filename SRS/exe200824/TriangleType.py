"""

WAP  classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""

side1 = int(input("Enter First side of triangle"))
side2 = int(input("Enter second side of triangle"))
side3 = int(input("Enter third side of triangle"))

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 and side1 != side3 and side2 != side3:
    print("issoceles")
else:
    print("Scalene")
