from zipfile import ZipFile
from pprint import pprint as pp

import urllib
import urllib.request


# http://www.pythonchallenge.com/pc/def/channel.html

# http://www.pythonchallenge.com/pc/def/zipper.html
#
# [:3]
#
# todo: tell everyone that [:n] is to take the first n characters...

# download channel.zip
# http://www.pythonchallenge.com/pc/def/zip.html
# yes. find the zip.

# readme.txt:
# welcome to my zipped list.
#
# hint1: start from 90052
# hint2: answer is inside the zip



def get_Zip_file():
    filenumber = 90052
    # filenumber = 46145
    text = ''
    nums = []
    comments = []
    comments2 = ''

    with ZipFile('channel.zip') as zipped:
        pp(zipped.compression)
        # print(zipped.getinfo('{}.txt'.format(filenumber)))
        # pp(zipped.filelist)
        # pp(zipped.infolist())
        try:
            while filenumber:
                #with open('.\\channel\\{}.txt'.format(filenumber), 'rt', encoding='utf-8') as file:
                with zipped.open('{}.txt'.format(filenumber) ) as file:
                    data = (file.read())
                    text = data.decode('utf-8')


                    # comments.append(text[:16])
                    comments.append(text)
                    nums.append(filenumber)

                    filenumber = int(text[text.find('Next nothing is')+16:])
                    # % comments2 = comments2 + '{} '.format(filenumber%128)


        except ValueError:
            # print(text.split())
            print('value error')
            print(file.name + ' ' + repr(text))
            print(comments)
            # with open('.\\channel\\' + str(filenumber) + '.txt', 'b') as file:
            #     file.print()
            zip2 = list(zip(comments, nums))
            return zip2


def get_file():
    filenumber = 90052
    # filenumber = 46145
    text = ''
    nums = []
    comments = []

    try:
        while filenumber:
            # open()
            file = open('.\\channel\\{}.txt'.format(filenumber), mode='rt', encoding='ascii')
            text = (file.read())
            # text = data.decode('utf-8')
            file.close()

            comments.append(text[16:])
            nums.append(filenumber)


            print(text)
            filenumber = int(text[text.find('Next nothing is')+16:])


    except ValueError:
        # print('value error')
        # print(file.name + ' ' + repr(text))
        # file.close()
        zip2 = list(zip(comments, nums))
        return zip2


if __name__ == '__main__':
    # with ZipFile('channel.zip') as zipped:
    #     # print(zipped.comment('46145.txt'))
    #     # end = zipped.comment # open('46145.txt')
    #     # print(str(end))
    #
    #
    # zipped.close()

    get_Zip_file()
    # pp(get_file())
