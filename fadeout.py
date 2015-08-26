#!/bin/python
#Make pictures fade out
#g(x) = (1-a)f0(x) + af1(x)
#where a is 0->1
#usage: python fadeout.py img1name img2name delaytime

from cv2 import *
import string
import sys

def getsumimg(img1,alpha1,img2,alpha2):
    temp = img1*alpha1 + img2*alpha2
    temp = temp.astype('uint8')
    return temp

def fadeout(img1,img2,time=1):
    if time == 0:
        #default 1 second
        time = 1
    img2 = resize( img2 ,(img1.shape[1],img1.shape[0]))
    alpha = 0
    alphastep = 20.0 / (time * 1000)
    while alpha <= 1 :
        temp = getsumimg(img1,1-alpha,img2,alpha)
        imshow('pic',temp)
        waitKey(20)
        alpha = alpha + alphastep
    imshow('pic',img2)
    waitKey(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "error"
        exit()
    img1 = imread(sys.argv[1])
    img2 = imread(sys.argv[2])
    if len(sys.argv) > 3:
        time = string.atoi(sys.argv[3])
        fadeout(img1,img2,time)
    else:
        fadeout(img1,img2)
