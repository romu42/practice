#!/usr/bin/env python3
# by rog


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def radius(self):
        return self.radius

    def area(self):
        return self.radius * self.radius * 3.14

    def diameter(self):
        return self.radius * 4

