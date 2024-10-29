from PIL import Image
import cv2 as cv

def menu(take_action):
    take_action = take_action.lower()
    if take_action == "capture":
        capture()
        return
    elif take_action == "play":
        play()
        return
    elif take_action == "solve":
        solve()
        return
    elif take_action == "calibrate":
        calibrate()
        return
    elif take_action == "checkered":
        checkered()
        return
    else:
        return ("This command does not exist.")

def capture():
    cam_port1 = 0
    cam_port2 = 1

    cam1 = cv.VideoCapture(cam_port1)
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
    actionString = input().lower()
    while actionString != "q":
        for action in actionString:
            match action:
                case "u":
                    #turn U
                    pass
                case "d":
                    #turn D
                    pass
                case "l":
                    #turn L
                    pass
                case "r":
                    #turn R
                    pass
                case "f":
                    #turn F
                    pass
                case "b":
                    #turn B
                    pass
                case _:
                    print("Invalid Turns")
        actionString = input()
def calibrate():
    pass
def solve():
    pass
def checkered():
    pass

take_action = input().lower()
menu(take_action)