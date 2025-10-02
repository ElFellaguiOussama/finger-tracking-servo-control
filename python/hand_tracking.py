import cv2
import mediapipe as mp
import numpy as np
from math import hypot
import serial
import time

arduino = serial.Serial('COM5' , 9600 , timeout = 1)
time.sleep(2)





cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
mpface = mp.solutions.face_mesh
draw = mp.solutions.drawing_utils
face_mesh = mpface.FaceMesh(static_image_mode=False, 
                                  max_num_faces=1, 
                                  refine_landmarks=False, 
                                  min_detection_confidence=0.5)
while True :
    success , img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    result1 = hands.process(imgRGB)
    result2 = face_mesh.process(imgRGB)


    if result1.multi_hand_landmarks and result2.multi_face_landmarks:
        for handlandmark in result1.multi_hand_landmarks:

            h,w,c = img.shape
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)
            thumb = handlandmark.landmark[4]
            x1 , y1 = int(thumb.x * w), int(thumb.y * h)
            index = handlandmark.landmark[8]
            x2 , y2 = int(index.x *w) , int(index.y * h)
            cv2.circle(img ,(x1 ,y1) , 10 ,(255 , 0 , 0) , 1 )
            cv2.circle(img ,(x2 ,y2) , 10 ,(255 , 0 , 0) , 1 )
            cv2.line(img , (x1 ,y1) , (x2,y2) , (0 , 0 , 255) , 10)

            distance = int(hypot(x2-x1,y2 - y1))
            cv2.putText(img , f'distance :{distance} px' ,(x1 - 50 , y1 + 50) , cv2.FONT_ITALIC ,0.8 , (255 , 0 , 0) , 4)
            min_dist = 20
            max_dist = 200
            angle = int((distance - min_dist) / (max_dist - min_dist) * 180)
            angle = max(0, min(180, angle))
            arduino.write(f"{angle}\n".encode('utf-8'))
                
    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()









