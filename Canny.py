#!/bin/python

from cv2 import *
import numpy as np

def canny( img , L2 = False):
    # @para img: requre grayscle
    # @para L2 : how to caculate grad
    # return :canny edge
    img = GaussianBlur( img , (5,5) , 0 )
    dx = Sobel( img , -1 , 1 , 0 , 3 )
    dy = Sobel( img , -1 , 0 , 1 , 3 )
    mag = np.zeros( img.shape )
    
    if L2 == True:
        for i in range(mag.shape[0]):
            for j in range(mag.shape[1]):
                mag[i][j] = abs(dx[i][j]) + abs(dy[i][j])
    else:
        for i in range(mag.shape[0]):
            for j in range(mag.shape[1]):
                mag[i][j] = np.sqrt(dx[i][j]**2 + dy[i][j]**2)
    
    N = np.zeros( img.shape )
    wit = N.shape[0]
    col = N.shape[1]

    for i in range( 1 , wit - 1 ):
        for j in range( 1 , col -1):
            if mag[i][j] == 0:
                continue
            Dx = dx[i][j]
            Dy = dy[i][j]
            #g1 g2
            #   c
            #   g3 g4
            temp1 = 0
            temp2 = 0
            if (Dx <= 0 and Dy >= 0 and abs(Dy) > abs(Dx)) or (Dx >= 0 and Dy <= 0 and abs(Dy) > abs(Dx)):
                g1 = mag[i-1][j-1]
                g2 = mag[i-1][j]
                g3 = mag[i+1][j]
                g4 = mag[i+1][j+1]
                Weight = float(abs(Dx))/abs(Dy)
                temp1 = g1 * Weight + g2 * (1 - Weight)
                temp2 = g4 * Weight + g3 * (1 - Weight)
            #g1
            #g2 c g3
            #     g4
            elif (Dx <= 0 and Dy > 0 and abs(Dy) <= abs(Dx)) or (Dx >= 0 and Dy < 0 and abs(Dy) <= abs(Dx)):
                g1 = mag[i-1][j-1]
                g2 = mag[i][j-1]
                g3 = mag[i][j+1]
                g4 = mag[i+1][j+1]
                Weight = float(abs(Dy))/(abs(Dx))
                temp1 = g2 * Weight + g1 * (1 - Weight)
                temp2 = g4 * Weight + g3 * (1 - Weight)
            #   g1 g2
            #   c 
            #g4 g3
            elif (Dx >= 0 and Dy >=0 and abs(Dy) > abs(Dx)) or (Dx <=0 and Dy <= 0 and abs(Dy) > abs(Dx)):
                g1 = mag[i-1][j]
                g2 = mag[i-1][j+1]
                g3 = mag[i+1][j-1]
                g4 = mag[i+1][j]
                Weight = float(abs(Dx))/(abs(Dy))
                temp1 = g2 * Weight + g1 * (1 - Weight)
                temp2 = g3 * Weight + g4 * (1 - Weight)
            #     g1
            #g4 c g2
            #g3
            elif (Dx != 0):
                g1 = mag[i-1][j+1]
                g2 = mag[i][j+1]
                g3 = mag[i+1][j-1]
                g4 = mag[i][j-1]
                Weight = float(abs(Dy))/(abs(Dx))
                temp1 = g1 * Weight + g2 * (1 - Weight)
                temp2 = g3 * Weight + g4 * (1 - Weight)
            
            if mag[i][j] >= temp1 and mag[i][j]>=temp2:
                N[i][j]=128
    #get threshold

    hist=[0] * 500
    for i in range(wit):
        for j in range(col):
            if N[i][j] == 128:
                hist[int(mag[i][j])] = hist[int(mag[i][j])] + 1
    edgenum = hist[0]
    maxmag = 0
    for i in range(500):
        if hist[i] != 0:
            maxmag = i;
        edgenum = edgenum + hist[i];
    drathigh = 0.79
    dratlow = 0.5
    nhighcount = int(drathigh * edgenum + 0.5)
    j=1
    edgenum = hist[1]
    while j < maxmag - 1 and edgenum < nhighcount:
        j = j + 1
        edgenum = edgenum + hist[j]
    threhigh = j
    threlow = int(threhigh * dratlow + 0.5)

    #detect
    for i in range(wit):
        for j in range(col):
            if N[i][j] == 128 and mag[i][j] >= threhigh:
                N[i][j] = 255
                N = traceedge(i , j , threlow , N , mag )

    for i in range(wit):
        for j in range(col):
            if N[i][j] != 255:
                N[i][j] = 0
    return N

def traceedge(y,x,threlow,N,mag):
    xNum = [1,1,0,-1,-1,-1,0,1]
    yNum = [0,1,1,1,0,-1,-1,-1]
    for k in range(8):
        yy = y + yNum[k]
        xx = x + xNum[k]
        if N[y][x] == 128 and mag[y][x] >= threlow:
            N[y][x] = 255
            N = traceedge(yy,xx,threlow,N,mag)
    return N
                    
        
