import cv2
import numpy as np

def empty(x):
  pass
cv2.namedWindow('lena',cv2.WINDOW_NORMAL)
cv2.resizeWindow('lena',(512,512))

img = np.ones((512,512,3),np.uint8)
cv2.createTrackbar('B','lena',0,255,empty)
cv2.createTrackbar('G','lena',0,255,empty)
cv2.createTrackbar('R','lena',0,255,empty)

while True:
  cv2.imshow('lena',img)
  if cv2.waitKey(1) == 27:
    break
  blue = cv2.getTrackbarPos('B','lena')
  green = cv2.getTrackbarPos('G','lena')
  red = cv2.getTrackbarPos('R','lena')
  img[:]= [blue,green,red]
cv2.destroyWindow('lena')

   
  
    













              
