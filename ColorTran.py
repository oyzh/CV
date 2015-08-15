#!/bin/python

#transfrom color type
#RGB
#HSL
#HSV
#now RGB -> HSV

from cv2 import *
import sys

def max( x , y , z):
    if x < y:
        x = y
    if x < z:
        x = z
    return x

def min( x , y , z):
    if x > y:
        x = y
    if x > z:
        x = z
    return x

def RGB_NORMAL( img ):
    #make RGB to [0,1]
    row = len( img )
    col = len( img[ 0 ] )
    for i in range( row ):
        for j in range( col ):
            img[ i ][ j ][ 0 ]=img[ i ][ j ][ 0 ]/255.0
            img[ i ][ j ][ 1 ]=img[ i ][ j ][ 1 ]/255.0
            img[ i ][ j ][ 2 ]=img[ i ][ j ][ 2 ]/255.0
    return img

def RGB2HSV( img ):
    RGB_NORMAL( img )
    row = len( img )
    col = len( img )

    for i in range( row ):
        for j in range( col ):
            r = img[ i ][ j ][ 0 ]
            b = img[ i ][ j ][ 1 ]
            g = img[ i ][ j ][ 2 ]
            max_num = max( r , b , g)
            min_num = min( r , b , g)

            if max_num == min_num:
                h = 0
            elif (max == r):
                h = 60 * (g - b)/(max - min)
                if g < b:
                    h = h + 360
            elif (max == g):
                h = 60 * (b - r)/(max - min) + 120
            else:
                h = 60 * (r - g)/(max - min) + 240
            
            if max == 0:
                s = 0
            else:
                s = 1 - min/max
                
            v = max
            img[ i ][ j ] [ 0 ] = h
            img[ i ][ j ] [ 1 ] = s
            img[ i ][ j ] [ 2 ] = v

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Need a image name\n"
    img = imread( sys.argv[1] )
    img = RGB_NORMAL( img )
    print img
    
