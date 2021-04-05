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
flagCanny = 0
flagSobel = 0
flagBrightness = 0
lagContrast = 0
flagNegative = 0
flagGray = 0
flagResize = 0
flagRotate = 0
flagFlipHorizontal = 0
flagFlipVertical = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))



while(True):
   
    ret, frame = cap.read()
  
    cv2.imshow('frame',frame)
    
    

    if cv2.waitKey(1) == ord('q'):
        break

    elif cv2.waitKey(1) == ord('r'):
        
        if(not flagRegular):
            flagRegular = 1
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            lagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('b'):
        if(not flagBlur):
            flagRegular = 0
            flagBlur = 1
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            lagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('c'):
        if(not flagCanny):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 1
            flagSobel = 0
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('s'):
     
        if(not flagSobel):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 1
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('w'):
    
        if(not flagBrightness):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 1
            flagNegative = 0
            flagContrast = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('t'):
    
        if(not flagContrast):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagNegative = 0
            flagContrast = 1
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('n'):
    
        if(not flagContrast):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagNegative = 1
            flagContrast = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('g'):
    
        if(not flagGray):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 1
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('l'):
        
        if(not flagResize):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 1
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('o'):

        if(not flagRotate):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 1
            flagFlipHorizontal = 0
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('h'):

        if(not flagFlipHorizontal):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 1
            flagFlipVertical = 0

    elif cv2.waitKey(1) == ord('v'):

        if(not flagFlipVertical):
            flagRegular = 0
            flagBlur = 0
            flagCanny = 0
            flagSobel = 0
            flagBrightness = 0
            flagContrast = 0
            flagNegative = 0
            flagGray = 0
            flagResize = 0
            flagRotate = 0
            flagFlipHorizontal = 0
            flagFlipVertical = 1
    
    if(flagRegular):
        cv2.imshow('result', frame)
        out.write(frame)
    
    elif(flagBlur):
       
        blurValue = cv2.getTrackbarPos('values', 'result')
        blur = cv2.GaussianBlur(frame, (2*blurValue+1,2*blurValue+1), cv2.BORDER_DEFAULT)
        cv2.imshow('result', blur)
        out.write(blur)

    elif(flagCanny):
        canny = cv2.Canny(frame, 100, 100)
        cv2.imshow('result', canny)
        out.write(canny)

    elif(flagSobel):
        sobel = cv2.Sobel(frame, cv2.CV_8U, 1, 1)
        cv2.imshow('result', sobel)
        out.write(sobel)

    elif(flagBrightness):
        result = result = cv2.addWeighted(frame, 1, np.zeros(frame.shape, frame.dtype), 0, cv2.getTrackbarPos('values', 'result')*16 -255)
        cv2.imshow('result', result)
        out.write(result)

    elif(flagContrast):
        result = cv2.addWeighted(frame, cv2.getTrackbarPos('values', 'result'), np.zeros(frame.shape, frame.dtype), 0, 0)
        cv2.imshow('result', result)
        out.write(result)

    elif(flagNegative):
        result = 255-frame
        cv2.imshow('result', result)
        out.write(result)

    elif(flagGray):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        out.write(gray)

    elif(flagResize):
        resize = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('result', resize)
        

    elif(flagRotate):
        rotate = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('result', rotate)

    elif(flagFlipHorizontal):
        flip = cv2.flip(frame, 1)
        cv2.imshow('result', flip)
        out.write(flip)

    elif(flagFlipVertical):
        flip = cv2.flip(frame, 0)
        cv2.imshow('result', flip)
        out.write(flip)

     
    


        
   

    

out.release()
cap.release()
cv2.destroyAllWindows()