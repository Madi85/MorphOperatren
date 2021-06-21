import numpy as np
from imageio import imread
from matplotlib import pyplot as plt

from main import *
from model.methods import *
from view.pathes import *


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def sea():
    seaImg(imread(IMG_SEA)[..., 0] / 255.0)


def one():
    oneImg(imread(IMG_ONE) / 255.0)
    # oneImg(rgb2gray(imread(IMG_ONE) / 255.0), imread(IMG_ONE))


def two():
    twoImg(imread(IMG_TWO) / 255.0)


def money():
    moneyImage(imread(IMG_MONEY) / 255.0)


def man():
    manImage(imread(IMG_MAN) / 255.0)


def mill():
    manImage(imread(IMG_MILL) / 255.0)

def slice2():
    manImage(imread(IMG_SLICE1) / 255.0)

def seastar():
    seastarImage(rgb2gray(imread(IMG_SEASTAR) / 255.0), imread(IMG_SEASTAR))


def map():
    mapImage(rgb2gray(imread(IMG_MAP) / 255.0), imread(IMG_MAP))


def img3d():
    img3dImage(np.load(ARRAY_CONFOCAL))
