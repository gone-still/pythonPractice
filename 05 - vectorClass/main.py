# File        :   vectorClass.py
# Version     :   1.0.0
# Description :   Implementing a basic Vector(x,y) class
#
# Date:       :   Jan 15, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

import math


class Vector:

    # Object initialization
    # Default values for x, y components is "0.0, 0.0"
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    # The add method returns a new object that represents
    # the sum of two objects
    def __add__(self, v: "Vector") -> "Vector":
        # Add individual vector components:
        a = self.x + v.x
        b = self.y + v.y

        # Return the addition in vector form:
        return Vector(a, b)

    # The repr method returns the string representation
    # of the object or class
    def __repr__(self) -> str:
        # Return the string representation of a Vector
        # object
        return "Vector(" + str(self.x) + ", " + str(self.y) + ")"

    # Return the norm/magnitude of the vector:
    def __abs__(self) -> float:
        # Calculate products:
        a = self.x * self.x
        b = self.y * self.y
        n = math.sqrt(a + b)

        # Return the norm:
        return n

    # Return the scalar product between a constant
    # and the vector:
    def __mul__(self, c: float) -> "Vector":
        # Multiply constant by each component:
        a = c * self.x
        b = c * self.y

        # Return the scalar product in vector form:
        return Vector(a, b)


# Create two vector objects:
v1 = Vector(2, 4)
v2 = Vector(2, 1)

# Add the two vectors:
s = v1 + v2
# Display the resulting vector:
print(s)

# Create a third vector object:
v3 = Vector(3, 4)
# Get its norm:
v3Norm = abs(v3)
print(v3Norm)

# Perform scalar product:
v4 = v3 * 3
print(v4)
print(abs(v3 * 3))

