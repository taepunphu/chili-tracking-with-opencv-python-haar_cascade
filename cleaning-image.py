import cv2
import numpy as np
import os
import time
import glob

def find_uglies():
    for ugly in glob.glob("badNegative/*.jpg"):
        try:
            ugly_image_path = ugly
            ugly_jpeg = cv2.imread(ugly_image_path)
            if ugly_jpeg is not None:
                cv2.imshow('show_ugly', ugly_jpeg)
                cv2.waitKey(1)
                for img in glob.glob("neg/*.jpg"):
                    try:
                        img_image_path = img
                        img_jpeg = cv2.imread(img_image_path)
                        print
                        str(img_image_path) + " from " + str(len(ugly)) + " - " + str(ugly_image_path) + " from " + str(
                            len(img))
                        if img_jpeg is not None:
                            cv2.imshow('show_neg', img_jpeg)
                            cv2.waitKey(1)
                            print
                            str(img_jpeg.shape) + " - " + str(ugly_jpeg.shape)
                            if (ugly_jpeg.shape) == (img_jpeg.shape) and not (
                            np.bitwise_xor(ugly_jpeg, img_jpeg).any()):
                                print
                                "***That is one ugly pic! Deleting!***"
                                print
                                str(img_image_path)
                                os.remove(img_image_path)
                        else:
                            print
                            "***That is one connot open pic! Deleting!***"
                            print
                            str(img_image_path)
                            os.remove(img_image_path)
                    except IOError as e:
                        print
                        "neg - " + str(e.value)
            else:
                print
                "***That is one connot open pic! Deleting!***"
                print
                str(ugly_image_path)
                os.remove(ugly_image_path)
        except IOError as e:
            print ("badNegative - " + str(e.value))


find_uglies()
