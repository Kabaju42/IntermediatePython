from zipfile import ZipFile
from pprint import pprint as pp

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
    # filenumber = 7331
    text = ''
    nums = []
    comments = []

    with ZipFile('channel.zip') as zipped:
        pp(zipped.filelist)
        try:
            while filenumber:
                #with open('.\\channel\\{}.txt'.format(filenumber), 'rt', encoding='utf-8') as file:
                with zipped.open('{}.txt'.format(filenumber) ) as file:
                    data = (file.read())
                    text = data.decode('utf-8')

                    comments.append(text[:16])
                    nums.append(filenumber)


                    # print(data)
                    # print(zip(data))
                    filenumber = int(text[text.find('Next nothing is')+16:])
                    comments.append(text)
                    nums.append(filenumber)
        except ValueError:
            # print(text.split())
            print('value error')
            print(file.name + ' ' + repr(text))
            # with open('.\\channel\\' + str(filenumber) + '.txt', 'b') as file:
            #     file.print()
            zip2 = list(zip(comments, nums))
            return zip2


def get_file():
    filenumber = 90052
    # filenumber = 7331
    text = ''
    nums = []
    comments = []

    try:
        while filenumber:
            with open('.\\channel\\{}.txt'.format(filenumber) ) as file:
                text= (file.read())

                comments.append(text)
                nums.append(filenumber)

                # print(data)
                filenumber = int(text[text.find('Next nothing is')+16:])

    except ValueError:
        print('value error')
        print(file.name + ' ' + repr(text))
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

    # get_file()
    pp(get_file())
