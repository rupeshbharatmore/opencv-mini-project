import cv2
import numpy as np
cv2.namedWindow('lena',cv2.WINDOW_NORMAL)
cv2.resizeWindow('lena',(512,512))
cap = cv2.VideoCapture(0)
low = np.array([100,50,50])
high = np.array([140,255,255])
while True:
  if cap.isOpened():
    ret,frame = cap.read()
  output = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  img = cv2.inRange(output,low,high)
  cv2.imshow('lena',img)
  
  if cv2.waitKey(111) == 27:
    break
  ret,frame = cap.read()
cv2.destroyAllWindows()
cap.release()

  
