import socket
from pprint import pprint as pp


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        # make the instance callable - ie a function
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


def sequence_class(immutable):
    # One way to to it
    # if immutable:
    #     cls = tuple
    # else:
    #     cls = list
    # return cls

    # The pythonic way to do it
    return tuple if immutable else list


def test_sequence_class():
    seq = sequence_class(immubable = True)
    t = seq("Weber State")
    print(t)


def test_lambda():
    scientists = ['Marie Curie French',
                  'Nicholas Bohr Germany',
                  'Issac Newton England',
                  'Dimitri Mendelev Russia',
                  'Charles Darwin Engerland',
                  'Albert Einstien Germany']

    # print list sorted
    # pp(sorted(scientists))

    # use a lambda function to sort by last name
    pp(sorted(scientists, key=lambda name: name.split()[-2]))

    # Task create a definition to sort the array by country

    pp(scientists)


# def sort_country (input):
#     name.split()[-2])


def main():
    # seq = sequence_class(immutable = True)
    # t = seq("Timbuktu")
    # print(t)
    # print(type(t))
    # print("\n\n")
    #
    # seq = sequence_class(immutable = False)
    # t = seq("Timbuktu")
    # print(t)
    # print(type(t))
    test_lambda()

if __name__ == '__main__':
    main()