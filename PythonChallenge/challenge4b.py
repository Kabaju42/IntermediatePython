from urllib.request import urlopen


class NothingIterator:
    def __init__(self):
        self._address_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
        self._nothing = '12345'
        self._nothing = str(16044/2)

    def __iter__(self):
        return self

    def __next__(self):
        with urlopen(self._address_base + self._nothing) as f:
            for line in f:
                msg = line.decode('utf-8').split(' ')
                print(line)

                if msg[-1].isdecimal():
                    self._nothing = msg[-1]
                else:
                    print('{}: {}'.format(self._nothing, msg))
                    raise StopIteration()

        return msg



def main():
    itter = NothingIterator()
    print(type(itter))
    for i in range (400):
        next(itter)


if __name__ == '__main__':
    main()