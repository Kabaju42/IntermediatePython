import sys

import reader

r = reader.reader(sys.argv[1])
try:
    print(r.read)
finally:
    r.close()

# print("Executing __main__.py with name {}".format(__name__))

