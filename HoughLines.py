#!/bin/python

#Hough transform
#reference: http://blog.csdn.net/viewcode/article/details/8090932
from cv2 import *
import numpy as np

def HoughLines( img , rho , theta , threshold ):
#img :source image ,had been process
#rho :length of spatial
#theta:length of angle
#threshold:the least number which a line must contain
    if theta == 0 or rho == 0:
        exit()
    irho = 1.0 / rho
    width = img.shape[1]
    height = img.shape[0]
    numangle = int(np.pi/theta)
    numrho = int(((width + height) * 2 + 1) / rho)
    accum = [0]*((numangle+2) * (numrho+2))
    tabSin = [0.]*numangle
    tabCos = [0.]*numangle
    position = []
    ret = []

    ang = 0
    for n in range(numangle):
        tabSin[n] = float(np.sin(ang) * irho)
        tabCos[n] = float(np.cos(ang) * irho);
        ang += theta

    for i in range(height):
        for j in range(width):
            if img[i][j] != 0:
                for n in range(numangle):
                    r = int(j*tabCos[n] + i*tabSin[n])
                    r += (numrho - 1) / 2
                    accum[(n+1) * (numrho+2) + r + 1] = accum[(n+1) * (numrho+2) + r + 1] + 1

    for r in range(numrho):
        for n in range(numangle):
            base = (n+1) * (numrho+2) + r + 1
            if accum[base] > threshold and accum[base] >accum[base - 1] and accum[base] >= accum[base + 1] and accum[base] > accum[base - numrho -2] and accum[base] >= accum[base + numrho + 2]:
                position.append(base)
    scale = 1./(numrho + 2)
    for i in range(len(position)):
        idx = position[i]
        n = int(idx*scale) - 1
        r = idx - (n+1)*(numrho+2) - 1
        grho = (r - (numrho - 1)*0.5)*rho
        gangle = n * theta
        ret.append( (grho,gangle) )
    return ret
        
            
                
