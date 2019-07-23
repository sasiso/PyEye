import abc
#from scipy.linalg import norm
#import cv2
from scipy import sum
from scipy.ndimage.filters import sobel
from skimage.filters.edges import roberts
from skimage.filters.thresholding import threshold_otsu, threshold_adaptive
from skimage.morphology._skeletonize import skeletonize


class IDetection(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def detect(self, image_1, image_2):
        return False


class DetectionStub(IDetection):
    def __init__(self):
        pass

    def binarize(self, image):
        import numpy as np
        image = roberts(image)
        cv2.imshow("edge detection", image)

        if False:
            me= np.median(image)
            image[image > me] = 255
            image[image < me] = 0
            image[image > 155] = 255


        return image

    def detect(self, image_1, image_2):
        if image_1 is None or image_2 is None:
            print("Warning, Skipping detection , One of image is none")
            return False

        image_1_edge_sobel = self.binarize(image_1)
        image_2_edge_sobel = self.binarize(image_2)
        cv2.imshow('1', image_1_edge_sobel)
        cv2.imshow('2', image_2_edge_sobel)

        print(self.compare_images(image_1_edge_sobel, image_2_edge_sobel))


        # Display the resulting frame
        cv2.waitKey(1)
        return False

    def compare_images(self, img1, img2):
        diff = img1 - img2  # elementwise for scipy arrays
        m_norm = sum(abs(diff))  # Manhattan norm

        return m_norm

    def normalize(self, arr):
        rng = arr.max() - arr.min()
        amin = arr.min()
        return (arr - amin) * 255 / rng
