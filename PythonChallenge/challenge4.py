"""
Challenge for:
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import urllib
import urllib.request


# <html>
# <head>
#   <title>follow the chain</title>
#   <link rel="stylesheet" type="text/css" href="../style.css">
# </head>
# <body>
# <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough. -->
# <center>
# <a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>
# <br><br><font color="gold"></center>
# Solutions to previous levels: <a href="http://wiki.pythonchallenge.com/"/>Python Challenge wiki</a>.
# <br><br>
# IRC: irc.freenode.net #pythonchallenge
# </body>
# </html>



# urllib.request
# urllib.parse
# urllib.robotparser
def test_chain():
    baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    nothing = 12345
    # and the next nothing is 16044
    # Yes.Divide by two and keep going.
    nothing = 16044/2
    list = []
    for i in range(400):
        site = urllib.request.urlopen(baseurl+str(nothing))
        b_msg = site.read()
        msg = b_msg.decode()
        site.close()
        last_nothing = nothing
        print(msg)
        nothing = int(msg[msg.find('and the next nothing is')+23:])
        if nothing in list:
            print(str(i) + '  ' + str(last_nothing) + '  ' + str(nothing))
            return list
        list.append(nothing)
        # print(msg)
    return list

if __name__ == '__main__':
    list = test_chain()
    print(list)

# peak.html
# http://www.pythonchallenge.com/pc/def/peak.html 