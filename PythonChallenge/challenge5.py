import pickle
from pprint import pprint as pp


file = open('banner.p', 'rb')
# c = file.read()

peak_hill = pickle.load(file)

file.close()

lengths = []
# pp(peak_hill)
for array in peak_hill:
    lengths.append(len(array))
    string = ''
    # print(str(len(array)) + ' ' + str(array))
    for t in array:
        # print(t[0]*t[1])
        # num += t[1]
        string = string + t[0] * t[1]
    print(string)

# print(lengths)
# answer: channel

