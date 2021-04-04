import numpy as np
import cv2
import keyboard

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('result')
cv2.createTrackbar('values', 'result', 1, 30, nothing)

blurValue = 1

#flags
flagRegular = 1
flagBlur = 0



while(True):
   
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    
    if(flagRegular):
        cv2.imshow('result', frame)
    
    if(flagBlur):
       
        blurValue = cv2.getTrackbarPos('values', 'result')
        blur = cv2.GaussianBlur(frame, (2*blurValue+1,2*blurValue+1), cv2.BORDER_DEFAULT)
        cv2.imshow('result', blur)
     
    if cv2.waitKey(1) == ord('q'):
        break

    if cv2.waitKey(1) == ord('b'):
        if(not flagBlur):
            flagRegular = 0
            flagBlur = 1
        
   

    


cap.release()
cv2.destroyAllWindows()