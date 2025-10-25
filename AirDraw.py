import cv2
import numpy as np
import time
import os
import handTrackingModule as htm

############
brushThickness=15
eraserThickness=50
xp,yp=0,0
############

folderPath="img"
myList=os.listdir(folderPath)
print(myList)
overlayList=[]  

for imPath in myList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header=overlayList[0]
drawColor=(255,0,255) #color of drawing

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)  

detector=htm.HandDetector(detectionCon=0.85)
xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8)#3 means color image

while True:
    # image import
    success, img = cap.read()
    img=cv2.flip(img,1) 

    # find hand landmarks
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)

    if len(lmList)!=0:
        # print(lmList)

        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:] # Middle finger tip

        # check which fingers are up
        fingers=detector.fingersup()
        print(fingers)


        # selection mode - two fingers up
        if fingers[1] and fingers[2]:
            xp,yp=0,0
            print("Selection Mode")
            # checking for the click
            if y1 < 125:    
                if 120 < x1 < 370:
                    header = overlayList[4]
                    drawColor = (0, 0, 255) # red
                elif 370 < x1 < 600:
                    header = overlayList[2]
                    drawColor = (255, 10, 10)   # blue
                elif 600 < x1 < 825:
                    header = overlayList[3]
                    drawColor = (0, 255, 255)   # yellow
                elif 825 < x1 < 1025:
                    header = overlayList[0]
                    drawColor = (0, 128, 0)   # green
                elif 1025 < x1 < 1200:
                    header = overlayList[1]
                    drawColor = (0, 0, 0)     # eraser
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
        # drawing mode - index finger up
        if fingers[1] and fingers[2]==False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp==0 and yp==0: #fix when starting point
                xp,yp=x1,y1
            if drawColor==(0,0,0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp,yp=x1,y1

    imgGray=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)#ggrayimg
    _,imgInv=cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)#bin img
    imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,imgInv)
    img=cv2.bitwise_or(img,imgCanvas)

        # header image setting
    img[0:125,0:1280]=header
    img=cv2.addWeighted(img,0.5,imgCanvas,0.5,0)#to merge two images

    if not success:
        break

    cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()