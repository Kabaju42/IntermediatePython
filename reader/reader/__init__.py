# print("reader is being interpreted")

from reader.reader.Compressed.gzipped import opener as gzip_opener


# rules for import *
__all__ = ['bz2_opener', 'gzip_opener']