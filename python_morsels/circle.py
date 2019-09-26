#!/usr/bin/env python3
# by rog

import math


class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * float(radius) * float(radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = int(radius)
        self._diameter = self._radius * 2
        self._area = math.pi * (self._radius) * float(self._radius)

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter / 2

    @property
    def area(self):
        return self._area

    def __repr__(self):
        return "Circle(" + str(self._radius) + ")"


if __name__ == "__main__":
    c = Circle(5)
    print(c.radius)
