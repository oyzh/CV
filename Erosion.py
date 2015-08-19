#!/bin/python

from cv2 import *
import numpy as np

def erosion( img ):
    # @para img : requir grayscale image
    # @ret erosioned image
    #0 1 0
    #1 1 1
    #0 1 0
    ret = np.zeros( img.shape )
    for i in range( 1 , img.shape[0] - 1 ):
        for j in range( 1 , img.shape[1] - 1 ):
            if img[i][j] > 0 and img[i-1][j] > 0 and img[i][j-1] > 0 and img[i][j+1] > 0 and img[i+1][j] > 0:
                ret[i][j] = 255
    return ret

            
