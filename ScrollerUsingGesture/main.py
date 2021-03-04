# Doing this project, I have used three module. First one is cv2 or computer vision 2, which is mostly
# used in computer vision, machine language and image processing. This python module commonly use in
# real time project. Second one is numpy library, which is working for array and 50x faster than
# traditional array. It has worked for linear algebra, fourier transform and matrices.Last one is pyautogui.
# it's a special to control mouse and keyboard.
import cv2
import numpy as np
import pyautogui

# define a range of red color,which is define as BGR format.
lower_red = np.array([0, 80, 80])
upper_red = np.array([10, 255, 255])
prev_y = 0

# Using this VideoCapture we define a object. Device index 0 or 1 we pass as a argument. You can
# capture frame-by-frame. At the end don't forget to release the capture.
cap = cv2.VideoCapture(0)

while True:
    # The real function gives boolean value, if the camera work correctly, then it provide True.
    # Otherwise False
    ret, frame = cap.read()
    # resize function is uses to scaling the image. First parameter refer the image source, second one
    # the pixel size of images and last one is interpolation, here we used INTER_AREA to shrinking any
    # image.
    frame = cv2.resize(frame, (342, 192), interpolation=cv2.INTER_AREA)
    # cvtColor or convert color one to another. There are 150 color space conversion in this function.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # inRange function use to identify the color range. Here the hsv is the image source, lower_red and
    # upper_rad value indicate the rage of color.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # The findContours is highly used in shape analysis, object detection and recognition. As you can see there
    # are three parameter, first one working as a source, second one to make retrieval mode and last one is
    # contour approximation method.
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # The contourArea function is used to calculate the detected area by findContours function
        area = cv2.contourArea(c)
        if area > 400:
            # Using drawContours function we could define the detected area with some specific color.
            # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
            # This function consider as straight rectangle. x and y define top-left corner and identify the
            # width and height.
            x, y, w, h = cv2.boundingRect(c)
            # Draw a rectangle with this function.
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # pretty awesome logic to move down by space key.
            if y < prev_y:
                # print('Moving down')
                pyautogui.press('space')

            prev_y = y
    # Make two windows. One for Hue Saturation Value and another one for normal image.
    cv2.imshow("HSV Frame", mask)
    cv2.imshow('Video Frame', frame)
    # Wait for press a key
    if cv2.waitKey(10) == ord("q"):
        break
# It is used to release an acquire lock. If the lock is locked, the function does the unlock.
cap.release()
# This function can demolish all of the windows we create.
cv2.destroyAllWindows()
