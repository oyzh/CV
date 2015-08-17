#!/bin/python

#Sobel

from cv2 import *
import numpy as np

SobelX=[[-1,0,1],
        [-2,0,2],
        [-1,0,1]]

SobelY=[[1,2,1],
        [0,0,0],
        [-1,-2,-1]]

def Sobel( img ):
    #gradient
    #G=|Gx|+|Gy|
    #require img as grayscale
    #before use Sobel,maybe you should use GaussianBlur
    #Cross border processing : multi 0
    Grad = img
    width = img.shape[1]
    height = img.shape[0]
    temp = np.zeros( ( height + 2 , width + 2 ) )
    
    for i in range( height ):
        for j in range( width ):
            temp[i+1][j+1] = img[i][j]
    for i in range( height ):
        for j in range( width ):
            x = i + 1
            y = j + 1
            Gx = SobelX[0][0] * temp[x-1][y-1] + SobelX[0][2] * temp[x-1][y+1] + SobelX[1][0] * temp[x][y-1] + SobelX[1][2] * temp[x][y+1] + SobelX[2][0] * temp[x+1][y-1] + SobelX[2][2] * temp[x][y+1]
            Gy = SobelY[0][0] * temp[x-1][y-1] + SobelY[0][1] * temp[x-1][y] +SobelY[0][2] * temp[x-1][y+1] + SobelY[2][0] * temp[x+1][y-1] + SobelY[2][1] * temp[x+1][y] + SobelY[2][2] * temp[x+1][y+1]

            Grad[i][j] = abs(Gx) + abs(Gy)
    return Grad
