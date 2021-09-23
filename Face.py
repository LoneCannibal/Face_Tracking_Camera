
import cv2
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[7].angle=90;#Clockwise-Decrease Anticlockwise-Increase
kit.servo[8].angle=90;#Up-decrease down-Increase

global servo1
global servo2

def up(a):
    return a-2
def down(a):
    return a+2
def clockwise(a):
    return a-2
def anticlockwise(a):
    return a+2

    
        

def track():
    servo1=90
    servo2=90
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
    cap = cv2.VideoCapture(-1)
    while 1:  
        ret, img = cap.read()  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
       
        for (x,y,w,h) in faces: 
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = img[y:y+h, x:x+w]
            if((210-(y+h/2))>50 and servo2>=30 and servo2<=120):#Face is 30px above center of camera
                servo2=up(servo2)
                print("Moving up")
            elif((210-(y+h/2))<-30 and servo2>=30 and servo2<=120):
                servo2=down(servo2)
                print("Moving down")
                
            if((290-(x+w/2))>30 and servo1>=30 and servo1<=150):
                servo1=anticlockwise(servo1)
                print("Moving anticlockwise")
            elif((290-(x+w/2))<-60 and servo1>=30 and servo1<=150):
                servo1=clockwise(servo1)
                print("Moving clockwise")
            kit.servo[7].angle=servo1;
            kit.servo[8].angle=servo2;
        cv2.imshow('img',img) 
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            if(servo2>90):
                while(servo2!=90):
                    servo2=up(servo2)
            else:
                while(servo2!=90):
                    servo2=down(servo2)
            if(servo1>90):
                while(servo1!=90):
                    servo1=clockwise(servo1)
            else:
                while(servo1!=90):
                    servo1=anticlockwise(servo1)        
            break
    cap.release() 
    cv2.destroyAllWindows()
track()

    

