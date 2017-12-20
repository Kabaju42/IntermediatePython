"""
From http://www.pythonchallenge.com/pc/def/map.html
"""

def challenge1():
    s = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
    rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw
    fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr
    gq qm jmle. sqgle qrpgle.kyicrpylq()
    gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
    print(s)

    code_from = 'abcdefghijklmnopqrstuvwxyz'
    code_to   = 'cdefghijklmnopqrstuvwxyzab'
    table = s.maketrans(code_from, code_to)
    a = s.translate(table)
    print(a)

    print('map -> ', 'map'.translate(table))

# hint:
# K -> M
# O -> Q
# E -> G

if __name__ == '__main__':
    challenge1()