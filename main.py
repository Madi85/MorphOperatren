import os

import matplotlib

from presenter.helper import *

if os.environ.get('DISPLAY', '') == '':
    matplotlib.use('TkAgg')

if __name__ == '__main__':

    mill()
    #one()
    #two()
    money()
    map()
    sea()
    seastar()
    man()
