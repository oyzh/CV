#!/bin/python

from cv2 import *
import numpy as np

def expansion( img ):
    # @para img : requir grayscale image
    # @ret expansioned image
    #0 1 0
    #1 1 1
    #0 1 0
    ret = np.zeros( img.shape )
    for i in range( 1 , img.shape[0] - 1 ):
        for j in range( 1 , img.shape[1] - 1 ):
            if (img[i][j] + img[i-1][j] + img[i][j-1] + img[i][j+1] + img[i+1][j]) != 0:
                ret[i][j] = 255
    return ret

            
