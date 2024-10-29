from PIL import Image
import cv2 as cv
import time

i = Image.open('Angle1.png')
p = i.getpixel((757, 222))

cam_port1 = 0
cam_port2 = 2

cam1 = cv.VideoCapture(cam_port1)

result, image1 = cam1.read()
# releasing the camera is important for the second camera to be able to capture.
cam1.release()

print(p)

cv.imwrite("mary.png", image1)
x = Image.open('mary.png')
x.show()

