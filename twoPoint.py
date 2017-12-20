class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '({}, {})'.format(str(self._x), str(self._y))

    # As a rule you should always add the __repr__
    def __repr__(self):
        return 'Point2D({}, {})'.format(str(self._x), str(self._y))

    def __add__(self, other):
        return Point2D(self._x + other._x, self._y + other._y)

    def __format__(self, format_spec):
        return 'Formatted point: {}, {}, {}'.format(self._x, self._y, format_spec)


if __name__ == '__main__':
    p1 = Point2D(5, 7)
    # p2 = Point2D(-1, 3)
    # print(p1)
    # print(str(p1))
    # print(repr(p1))
    # print(p1 + p2)
    #
    # # try list
    # l = [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=3)]
    # print(l)

    print('This is a point({})'.format(p1))

    # dict works too
