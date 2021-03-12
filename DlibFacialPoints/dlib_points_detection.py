import cv2 as cv
import dlib
import numpy as np

def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68,2), dtype = dtype)
    for i in range(0,68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

img = cv.imread("image.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

detector = dlib.get_frontal_face_detector()
rects = detector(gray,1)

predictor = dlib.shape_predictor('shape_68.dat')
for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_np(shape)
    for (x, y) in shape:
        cv.circle(img, (x, y), 2, (0, 0, 255), -1)
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()
