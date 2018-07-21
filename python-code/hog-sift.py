import cv2
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, color, exposure

filenames = glob.glob('/Users/jinwoo/Desktop/breast-cancer-img/original/*.png')
exportCounter = 1
hogPath = '/Users/jinwoo/Desktop/breast-cancer-img/hog/'
siftPath = '/Users/jinwoo/Desktop/breast-cancer-img/sift/'

for filename in filenames:
    originalImage = cv2.imread(filename)
    greyImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

    # for HOG (Histogram of Oriented Gradients)
    fd, hogImage = hog(greyImage, orientations=8, pixels_per_cell=(2,2), cells_per_block=(1,1), visualise=True)
    hogFilename = 'hog-' + str(exportCounter) + '.jpg'
    cv2.imwrite(os.path.join(hogPath, hogFilename), hogImage)

    # for SIFT (Scale Invariant Feature Transform)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(greyImage,None)
    siftImage = cv2.drawKeypoints(greyImage, kp, outImage=np.array([]))
    siftFilename = 'sift-' + str(exportCounter) + '.jpg'
    cv2.imwrite(os.path.join(siftPath, siftFilename), siftImage)

    exportCounter += 1
