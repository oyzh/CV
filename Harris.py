#/bin/python
#Harris conner
#TODO:delete some detected conners,because some conners are very closed.

#[(Ix)**2 IxIy]
#[IxIy (Iy)**2]

from cv2 import *
import numpy as np
import sys
def harris( img , alpha=0.01 , t=0):
    #alpha and t :caculate R
    #if img.ndim == 3:
    harlist = []
    dy = filter2D( img , 3 , (-1,0,1) )
    dx = filter2D( img.T , 3 ,  (-1,0,1) ).T
    for i in range( 1, img.shape[0]-1 ):
        for j in range(1 , img.shape[1]-1):
            dxdy = dx[i][j] * dy[i][j]
            det = (dx[i][j]**2) * (dy[i][j]**2) - dxdy**2
            trace = dx[i][j] + dy[i][j]
            if (det - alpha * (trace**2)) >= t:
               harlist.append([i,j])
    return harlist
    
def showharris( img , harlist ):
    temp = img
    for i in range(len(harlist)):
        x = harlist[i][0]
        y = harlist[i][1]
        for j in range(-1,2):
            for k in range(-1,2):
                temp[x+j][y+k] = 255
    print len(harlist)
    imshow( 'harris' , temp )
    waitKey(0)
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    img = imread(sys.argv[1],CV_LOAD_IMAGE_GRAYSCALE)
    showharris( img , harris(img))
    
                
            
            
