import morphsnakes
import numpy as np

from matplotlib import  pyplot as plt

def seaImg(image):
    inverseGaussianGradient = morphsnakes.inverse_gaussian_gradient(image, alpha=1000, sigma=5.48)
    initLevelSet = morphsnakes.circle_level_set(image.shape, center=(100, 126),radius= 30)
    morphsnakes.morphological_geodesic_active_contour(inverseGaussianGradient, iterations=65,
                                             init_level_set=initLevelSet,
                                             smoothing=20, threshold=0.31,
                                             balloon=1, iter_callback=plot_2d(image))

def seastarImage(image,imageRgp):
    inverseGaussianGradient = morphsnakes.inverse_gaussian_gradient(image, alpha=1000, sigma=2)
    initLevelSet = morphsnakes.circle_level_set(image.shape, center=(163, 137), radius=135)
    morphsnakes.morphological_geodesic_active_contour(inverseGaussianGradient, iterations=150,
                                             init_level_set=initLevelSet,
                                             smoothing=20, threshold=0.3,
                                             balloon=-1, iter_callback=plot_2d(imageRgp))

def moneyImage(image):
    inverseGaussianGradient = morphsnakes.inverse_gaussian_gradient(image)
    initLevelSet = np.zeros(image.shape, dtype=np.int8)
    initLevelSet[10:-10, 10:-10] = 1
    morphsnakes.morphological_geodesic_active_contour(inverseGaussianGradient, iterations=230,init_level_set= initLevelSet,
                                             smoothing=20, threshold=0.69,
                                             balloon=-1, iter_callback=plot_2d(image))

def mapImage(image,imageRgp):
    initLevelSet = morphsnakes.circle_level_set(image.shape, center=(80, 170),radius= 25)
    morphsnakes.morphological_chan_vese(image, iterations=250,
                               init_level_set=initLevelSet,
                               smoothing=30, lambda1=1, lambda2=1,
                               iter_callback=plot_2d(imageRgp))

def manImage(image):
    iterCallback = plot_2d(image)
    morphsnakes.morphological_chan_vese(image, iterations=35,
                               smoothing=30, lambda1=1, lambda2=1,
                               iter_callback=iterCallback)

def img3dImage(image):
    initLevelSet = morphsnakes.circle_level_set(image.shape, center=(30, 50, 80), radius=25)
    morphsnakes.morphological_chan_vese(image, iterations=200,
                               init_level_set=initLevelSet,
                               smoothing=30, lambda1=1, lambda2=2,
                               iter_callback=plot_3d(plot_each=20))


def oneImg(image):
    inverseGaussianGradient = morphsnakes.inverse_gaussian_gradient(image, alpha=1000, sigma=5.48)
    initLevelSet = morphsnakes.circle_level_set(image.shape, center=(150, 606), radius=20)
    morphsnakes.morphological_geodesic_active_contour(inverseGaussianGradient, iterations=545,
                                                      init_level_set=initLevelSet,
                                                      smoothing=20, threshold=0.31,
                                                      balloon=1, iter_callback=plot_2d(image))

def twoImg(image):
    inverseGaussianGradient = morphsnakes.inverse_gaussian_gradient(image, alpha=1000, sigma=5.48)
    initLevelSet = morphsnakes.circle_level_set(image.shape, center=(90, 806), radius=20)
    morphsnakes.morphological_geodesic_active_contour(inverseGaussianGradient, iterations=545,
                                                      init_level_set=initLevelSet,
                                                      smoothing=20, threshold=0.31,
                                                      balloon=1, iter_callback=plot_2d(image))


def plot_2d(image, figer=None):
    figer = plt.figure()
    plotA = figer.add_subplot(1, 2, 1)
    plotA.imshow(image, cmap=plt.cm.gray)
    plotB = figer.add_subplot(1, 2, 2)
    axisY = plotB.imshow(np.zeros_like(image), vmin=0, vmax=1)

    def iterCallback(levelset):
        if plotA.collections:
            del plotA.collections[0]
        plotA.contour(levelset, [0.8], colors='r')
        axisY.set_data(levelset)
        figer.canvas.draw()
        plt.pause(0.1)

    return iterCallback

def plot_3d(plot_each):
        figer = plt.figure()
        figer.clf()
        axis = figer.add_subplot(111, projection='3d')
        plt.pause(0.1)

        numPlot = [-1]

        def iterCallback(levelset):
            numPlot[0] += 1
            if (numPlot[0] % plot_each) != 0:
                return
            if axis.collections:
                del axis.collections[0]
            coords, triangles = mcubes.marching_cubes(levelset, 0.5)
            axis.plot_trisurf(coords[:, 0], coords[:, 1], coords[:, 2],
                            triangles=triangles)
            plt.pause(0.1)

        return iterCallback
