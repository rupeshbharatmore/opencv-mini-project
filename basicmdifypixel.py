import numpy as np
import cv2
cv2.namedWindow('lena',cv2.WINDOW_NORMAL)
cv2.resizeWindow('lena',(512,512))
cap = cv2.VideoCapture(0)
th = 127
max_val= 255
while True:
  if cap.isOpened():
    ret,frame = cap.read()
  rt,out = cv2.threshold(frame,th,max_val,cv2.THRESH_BINARY_INV)
  cv2.imshow('lena',out)
  if cv2.waitKey(1) == 27:
    break
cv2.destroyAllWindows()
cap.release()

