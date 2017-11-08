import numpy as np
import cv2
import signal

cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier("/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/Users/weijiewu/Desktop/dsplab/project/haarcascades/haarcascade_eye.xml")

i = 0
j = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('d',frame)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        cv2.destroyAllWindows()
        break

while (cap.isOpened()):


    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #cv2.imshow('face1', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        j = j + 1
        i = i + 1
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    if (j > 0):
        j = 0
        #i=0
        #cv2.imwrite('/Users/weijiewu/Desktop/dsplab/project/output/' + str(i) + '.jpg', frame)

    cv2.imshow('face', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break


cap.release()
cv2.destroyAllWindows()