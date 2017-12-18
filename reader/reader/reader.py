import os

from reader.Compressed import gzipped
from reader.compressed import bzipped

# Map extensions
extension_map={
    '.bz2' : bzipped.opener,
    '.gz'  : gzipped.opener,
}


class Reader:
    def __init__(self, filename):
        # get the extension
        extension = os.path.splitext(filename)[1]

        opener = extension_map.get(extension, open)
        self._filename = filename
        self._f = open(self._filename, mode='rt', encoding='utf-8')

    def close(self):
        self._f.close()

    def read(self):
        return self._f.read()

def main():
    """
    Test Function
    """
    r = Reader('../test.bz2')
    print(r.read())
    r.close()
    pass


if __name__ == '__main__':
    main()
    exit(0)