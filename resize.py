#!/bin/python 
#Biliner interpolation

from cv2 import *
import numpy as np
import sys
import string

def Resize( img , newsize ):
    if (newsize[0] <= 0) or (newsize[1] <=0):
        return False
    if img.ndim == 2:
        newimg = np.zeros(newsize,img.dtype)
        temp = np.zeros((img.shape[0]+1,img.shape[1]+1),img.dtype)
    if img.ndim == 3:
        newimg = np.zeros((newsize[0],newsize[1],3),img.dtype)
        temp = np.zeros((img.shape[0]+1,img.shape[1]+1,3),img.dtype)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            temp[i][j] = img[i][j]

    for i in range( newimg.shape[0] ):
        x = float(i) / newsize[0] * img.shape[0]
        for j in range( newimg.shape[1] ):
            y = float(j) / newsize[1] * img.shape[1]
            m = int(x)
            n = int(y)
            u = x - m
            v = y - n
            if img.ndim == 2:
                newimg[i][j] = (1-u)*(1-v)*temp[m][n] + (1-u)*v*temp[m][n+1] + u*(1-v)*temp[m+1][n] + u*v*temp[m+1][n+1]

            else:
                for k in range(3):
                    newimg[i][j][k] = (1-u)*(1-v)*temp[m][n][k] + (1-u)*v*temp[m][n+1][k] + u*(1-v)*temp[m+1][n][k] + u*v*temp[m+1][n+1][k]
    return newimg

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "error"
        exit()
    img = imread(sys.argv[1])
    img = Resize( img , (string.atoi(sys.argv[2]) , string.atoi(sys.argv[3]) ))
    imshow('newimg',img)
    waitKey(0);
