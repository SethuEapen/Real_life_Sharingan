"""import cv2


scale = 30


cv2.namedWindow("preview")
vc = cv2.VideoCapture('http://192.168.1.155:5555/video')
rval, frame = vc.read()
width = int(frame.shape[1] * scale / 100)
height = int(frame.shape[0] * scale / 100)
dim = (width, height)
print(dim)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while True:
    rval, frame = vc.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.resize(gray, dim)
    out.write(gray)
    cv2.imshow("preview", gray)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
out.release()
cv2.destroyAllWindows()"""
import time
import numpy as np
import cv2

scale = 30

cap = cv2.VideoCapture('boar_trim.avi')#'http://192.168.1.155:8080/video')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('boar.avi',fourcc, 20.0, (640,480), 0)

while(True):
    ret, frame = cap.read()
    time.sleep(.03)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out.write(gray)
    viewer = cv2.resize(gray, (1280, 720))
    cv2.imshow('frame',viewer)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()


import numpy as np
import cv2

scale = 30

cap = cv2.VideoCapture('http://192.168.1.155:8080/video')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('boar.avi',fourcc, 20.0, (640,480), 0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)
    viewer = cv2.resize(gray, (1280, 720))
    cv2.imshow('frame',viewer)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()