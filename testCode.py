from PIL import Image
from get_Color import getColor
import cv2 as cv
import time

i = Image.open('Angle1.png')
p1 = i.getpixel((757, 222))
p2 = i.getpixel((720,583))
p3 = i.getpixel((945,700))
i = Image.open('Angle2.png')
p4 = i.getpixel((642, 551))
p5 = i.getpixel((867,415))
p6 = i.getpixel((875,666))

#cam_port1 = 0
#cam_port2 = 2

#cam1 = cv.VideoCapture(cam_port1)

#result, image1 = cam1.read()
# releasing the camera is important for the second camera to be able to capture.
#cam1.release()
color1 = getColor(p1[0],p1[1],p1[2])
color2 = getColor(p2[0],p2[1],p2[2])
color3 = getColor(p3[0],p3[1],p3[2])
color4 = getColor(p4[0],p4[1],p4[2])
color5 = getColor(p5[0],p5[1],p5[2])
color6 = getColor(p6[0],p6[1],p6[2])

print('\nOn Angle1, the following colors are:')
print(f'The first color @ 757, 222 is {color1}')
print(f'The second color @ 720, 583 is {color2}')
print(f'The third color @ 945, 700 is {color3}', end='\n\n')

print('On Angle2, the following colors are:')
print(f'The first color @ 642, 551 is {color4}')
print(f'The second color @ 867, 415 is {color5}')
print(f'The third color @ 875, 666 is {color6}')


#cv.imwrite("mary.png", image1)
#x = Image.open('mary.png')
#x.show()

