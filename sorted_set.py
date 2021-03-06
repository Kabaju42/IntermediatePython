"""
A Sorted set to test
"""

class SortedSet:
    def __init__(self, items = None):
        """
        Sorted returns a list regardless of
        which iterable object you passed
        """
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # equivalent code Python 3.3 or less
        # for item in self._items:
        #     yield item

        # equivalent code > Python 3.3
        # yield from self._items

        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return (SortedSet(result)
                if isinstance(index, slice)
                else result)

    def __repr__(self):
        return "SortedSet({})".format(repr(self._items
                                           if self._items
                                           else ''))

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self._items == other._items
