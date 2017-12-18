"""
Python review of Classes
"""

import math

class MyFirstClass:
    pass


class Point:
    # Add som instance methods: Do something
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def reset(self):
        self._x = 0
        self._y = 0

    def get_point(self):
        """
        method to get the ponit
        :return: tupple in form: (x, y)
        """
        return(self._x, self._y)

    def calculate_distance(self, dist_point):
        return math.sqrt(
            (self._y - dist_point._y)**2 +
            (self._x - dist_point._x)**2)


def main():
    """
    Test Function
    """
    p1 = Point()
    p2 = Point(2, 5)

    print(type(p1))
    print(p1._x, p1._y)
    print(p2._x, p2._y)

    p1.reset()
    print(p1._x, p1._y)
    print('distance = ')
    print(p1.calculate_distance(p2))

if __name__ == '__main__':
    main()
    exit(0)