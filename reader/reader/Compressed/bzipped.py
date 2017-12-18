import bz2
import sys

#
opener = bz2.open


def main():
    """
    Test Function
    """
    # ./file.py out.bz "YES" "NO" "MAYBE"
    f = bz2.open(sys.argv[1], mode='wt', encoding='utf-8')
    f.write(' '.join(sys.argv[2:]))
    f.close()
    pass


if __name__ == '__main__':
    main()
    exit(0)