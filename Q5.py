import numpy as np
import cv2 as cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc ('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

def fixColor(image):
    return(cv2.cvtColor (image, cv2.COLOR_BGR2RGB))

#Input Video here
cap=cv2.VideoCapture('Vid/video.mp4')

while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))

    if ret==True:
        # cv2.imshow('Vid',frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur (gray, (5,5), 0)
        #cv2.imshow ('img',fixColor (gray))
        edges=cv2.Canny(gray,50,100)
        #cv2.imshow('can',edges)
        lines=cv2.HoughLinesP(edges,rho=1,theta=np.pi/100,threshold=130,minLineLength=5,maxLineGap=250)
        for line in lines:
            x1,y1,x2,y2=line[0]
            if (y1>430 or y2>430):
                cv2.line(frame,(x1,y1),(x2,y2),(0,100,200),2)
        cv2.imshow('Final Video',fixColor(frame))
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()