import numpy as np
import cv2
import datetime as dt

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
while(True):
    now_time = dt.datetime.now().strftime('%F-%T')
    now_time = now_time.replace(":", "-")
    out = cv2.VideoWriter(now_time+'.mp4',fourcc, 20.0, (640, 480), True)
    at = 0
    #frameCount = 0
    while(cap.isOpened()):
        cv2.waitKey(40)
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)
            out.write(frame)
            at+=1
            #frameCount = frameCount + 1
            #cv2.imshow('frame',frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
         #    	break
            if at>=200:
                break
        else:
            break
    #print('总帧数：', frameCount)
    print('successful')
    out.release()
    #cv2.destroyAllWindows()
cap.release()