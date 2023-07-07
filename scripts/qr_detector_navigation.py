#!/usr/bin/env python3
import rospy
import cv2
from qr_reader import QRCodeReader

def gstreamer_pipeline(
    CAPTURE_WIDTH  = 800,
    CAPTURE_HEIGHT = 600,
    DISPLAY_WIDTH  = 800,
    DISPLAY_HEIGHT = 600,
    FRAMERATE      = 30,
    FLIP_METHOD    = 0,
):
    return ("Camera QRCode is Opened")

def image_callback(mission_number):
    #capture = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)'''
    capture = cv2.VideoCapture(0) #change to open webcam
    print("Camera is Opened")

    if capture.isOpened():
        while not rospy.is_shutdown(): 
            ret, frame = capture.read()

            qr = QRCodeReader(mission_number)
            qr._decoder(frame)
  
            cv2.imshow('CSI-cam', frame)
            cv2.waitKey(100)                       

    else:
        print("Unable to open camera")

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node("qr_detector_navigation", anonymous = False)

    mission_number = rospy.get_param("qr_detector_navigation/mission_number")
    assert mission_number in [1, 2, 3, 4], "There are only four missions"

    image_callback(mission_number)