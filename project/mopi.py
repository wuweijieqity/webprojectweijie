import numpy as np
import cv2
import signal
face_cascade = cv2.CascadeClassifier("/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
value1=3
value2=1
dx=value1*5
fc=value1*12.5
p=50
while(cap.isOpened()):

    ok, frame = cap.read()
    #frame = cv2.flip(frame, 1)
    temp=frame
    temp1=cv2.bilateralFilter(temp,dx,fc,fc)
    temp2 = temp1 - frame + 128
    temp3 = cv2.GaussianBlur(temp2, (2 * value2 - 1, 2 * value2 - 1), 0, 0)
    temp4 = frame + 2 * temp3 -255
    dst = frame * 0.9 + temp4 * 0.1
    cv2.imshow('s',temp1)
    #cv2.imshow('s1',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()