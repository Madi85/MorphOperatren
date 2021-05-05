import os

import matplotlib

from presenter.helper import sea, seastar, money, man , map

if os.environ.get('DISPLAY', '') == '':
    matplotlib.use('TkAgg')

if __name__ == '__main__':
    money()
    map()
    sea()
    seastar()
    man()
