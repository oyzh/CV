#!/bin/python
#TODO edge processing
from math import *

def GaussBooth(src,sigma):
#caculate kernel
#ksize=(6*sigma+1),and must be odd
    ksize=(int)((ceil(sigma*3))*2+1)
    if ksize==1:
        return src
    kernel=[0]*ksize
    center=ksize/2
#use sum to  Normalization
    sum=0
    for i in range(center+1):
        value=exp(-0.5*(center-i)**2/(sigma**2))
        kernel[i]=value
        sum=sum+2*value
    sum=sum-kernel[center]
    for i in range(center+1):
        kernel[i]=kernel[ksize-i-1]=kernel[i]/sum

#convolution image
    dst=src.copy()
    row=len(src)
    col=len(src[0])

    #x direction
    for i in range(row):
        for j in range(col):
            dst[i][j]=0
            for k in range(ksize):
                point=j-center+k
                if (point >= 0) and (point < col):
                   dst[i][j]=dst[i][j]+kernel[k]*src[i][point]

    #y direction
    for i in range(row):
        for j in range(col):
            src[i][j]=0
            for k in range(ksize):
                point=i-center+k
                if (point >= 0) and (point < row):
                    src[i][j]=src[i][j]+kernel[k]*dst[point][j]
    return src
