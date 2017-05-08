#!/usr/bin/env python3

import cv2
import numpy as np
import os
import time

class ArmController():

    def __init__(self):
        self.startCam()
        self.startTime = time.time()

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
        self.main()
        

    def main(self):
        while cv2.waitKey(1) != 27:  # infinite loop until esc is pressed, 100ms wait
            if self.usbCam.isOpened():
                blnFrameReadSuccessfully, img = self.usbCam.read()

                if not blnFrameReadSuccessfully or img is None:     
                    print("Lost usbCam Connection")
                    self.usbCam.release()
                    cv2.destroyAllWindows()
                    time.sleep(2)
                    continue
                timeSinceLast = time.time() - self.startTime
                #print("TimeSinceLast: " + str(timeSinceLast))
                framePerSecond = "FPS: " + "{:.3}".format(str(1/timeSinceLast))
                #print("FPS: " + str(framePerSecond))
                self.startTime = time.time()
                cv2.putText(img, framePerSecond, (10,25), self.font, 0.5, (255,255,255),2)
                cv2.namedWindow("Stream", cv2.WINDOW_AUTOSIZE)
                cv2.imshow("Stream", img)
            else:
                time.sleep(2)
                self.startCam()
            

        cv2.destroyAllWindows()  # If we leave the while loop, destroy all windows
            

    def startCam(self):
        self.usbCam = cv2.VideoCapture(0)
        
        if self.usbCam.isOpened():
            self.usbCam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240.0)
            print("Cam Open")
            print("default resolution = " + str(self.usbCam.get(cv2.CAP_PROP_FRAME_WIDTH)) + "x" + str(self.usbCam.get(cv2.CAP_PROP_FRAME_HEIGHT)))


if __name__ == "__main__":
    a = ArmController()
