import numpy as np
import cv2
cv2.namedWindow('lena',cv2.WINDOW_NORMAL)
cv2.resizeWindow('lena',(512,512))
img = cv2.imread('b2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('lena',img)
cv2.waitKey(0)

