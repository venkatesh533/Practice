import numpy as np
import cv2

cap = cv2.VideoCapture(0)

## To make screen display resolutions ##
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


make_480p()
change_res(1280, 720)

while True:
	## Capture frame by frame ##
	ret, frame = cap.read()

	## Display the resulting frame ## 
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()