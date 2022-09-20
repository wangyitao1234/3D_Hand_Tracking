import cv2
from hands_detect_moudle import handDetector
#from cvzone.HandTrackingModule import  HandDetector

import socket

#parameters
width, height =1280,720

#webcam
cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#Hand Detector
detector =handDetector()

#Communication
sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddressPort =("172.22.1.64",5052)

while True:
    success, img =cap.read()
    img, allHands = detector.findHands(img, draw=True)

    data =[]
    if allHands:
        hand =allHands[0]
        lmlist =hand["lmlist"]
        #print(lmlist)
        for lm in lmlist:
            data.extend([lm[0],height-lm[1],lm[2]])
        #print(data)
        sock.sendto(str.encode(str(data)),serverAddressPort)


    cv2.imshow("image",img)
    cv2.waitKey(1)



