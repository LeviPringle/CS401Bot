from PIL import Image
import cv2 as cv

def menu(take_action):
    if take_action == "capture":
        capture()
    elif take_action == "play":
        play()
    elif take_action == "solve":
        solve()
    elif take_action == "calliberate":
        calliberate()
    elif take_action == "checkered":
        checkered()
    else:
        print("This command does not exist.")

def capture():
    cam_port1 = 0
    cam_port2 = 1

    cam1 = cv.VideoCapture()
    result, image1 = cam1.read()
    # releasing the camera is important for the second camera to be able to capture.
    cam1.release()
    cv.imwrite("mary.png", image1)
    x = Image.open('mary.png')
    x.show()

    cam2 = cv.VideoCapture(cam_port2)
    result, image1 = cam2.read()
    # releasing the camera is important for the second camera to be able to capture.
    cam2.release()
    cv.imwrite("mary.png", image1)
    x = Image.open('mary.png')
    x.show()

def play():
    pass
def calliberate():
    pass
def solve():
    pass
def checkered():
    pass

take_action = input().lower()
menu(take_action)