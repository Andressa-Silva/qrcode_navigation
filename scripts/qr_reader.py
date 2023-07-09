#!/usr/bin/env python3
import rospy
import cv2
import math
from pyzbar.pyzbar import decode
from qr_detector.msg import Direction

class QRCodeReader():
    """ Class to read the QR Code data for navigation """

    def _decoder(self, frame):
        """ Find and read the center of the QRCode """
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
        qr_decoded = decode(im)

        imgHeight, imgWidth = im.shape

        centerImgX = int(imgWidth/2)
        centerImgY = int(imgHeight/2)

        cv2.circle(frame, (centerImgX, centerImgY), 2, (255, 0, 0), 3)
	    
        for decodedObject in qr_decoded:
            (x,y,w,h) = decodedObject.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            centerQrCodeX = int((x+w) - (w/2))
            centerQrCodeY = int((y+h) - (h/2))
            cv2.circle(frame, (centerQrCodeX, centerQrCodeY), 2, (255, 0, 0), 3)

            distanceX = centerQrCodeX - centerImgX
            distanceY = centerQrCodeY - centerImgY

            cv2.line(frame, (centerQrCodeX,centerQrCodeY), (centerImgX,centerImgY), (255,0,0), 3)

            self.distancia_pixels = math.sqrt(distanceX**2 + distanceY**2)

            barCode = str(decodedObject.data.decode("utf-8"))
            barCodeFiltered = barCode.split(",")

            direction_msg = Direction()
            direction_msg.mission_number = barCodeFiltered[-1]
            direction_msg.direction = barCodeFiltered[self.mission_number-1]
       
    def __init__(self, mission_number) -> None:
        """ External variables
        
        mission_number: 1 - Delivering the kit,
                        2 - Eletrical scan
                        3 - Victims in tall building
                        4 - Return starting point
        """
        self.mission_number = mission_number