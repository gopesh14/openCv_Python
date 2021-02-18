import time
import cv2 as cv
video = cv.VideoCapture(0)

a = 1
while True:
    a += 1
    check,frame = video.read()

#print(check)
    print(frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("Capturing",frame)
    key = cv.waitKey(1)
    if key == ord('q') : break

print(a)
video.release()
cv.destroyAllWindows()
