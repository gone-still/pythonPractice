# File        :   basicInheritance.py
# Version     :   1.0.0
# Description :   Implementing a series of classes via inheritance
#
# Date:       :   Jan 27, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

class Rectangle:
    def __init__(self, length, width):
        # Init parameters
        self.length = length
        self.width = width

    def area(self):
        # Calculate area:
        return self.length * self.width

    def perimeter(self):
        # Calculate perimeter:
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        # Calls Rectangle's init
        # Set Rectangle's length and width:
        super().__init__(length, length)

        # Not written, but Square has
        # access to Rectangle's methods:
        # area() and perimeter()


# Multiple inheritance:
class Cube(Square):
    def __init__(self, name, *args):
        # Class unique attribute:
        self._name = name
        # Calls Square's init:
        # Set Square's length:
        super().__init__(*args)

    def surface_area(self):
        # Call Square's area,
        # (Actually Rectangle's):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        # Call Square's area,
        # (Actually Rectangle's):
        face_area = super().area()
        return face_area * self.length

    # Access "name" via a read-only property:
    @property
    def name(self):
        return self._name


# Some objects and operations:
mySquare = Square(4)
squareArea = mySquare.area()
print(squareArea)

myCube = Cube("mrCube", 3)
cubeVolume = myCube.volume()

print(cubeVolume)
print(myCube.name)
