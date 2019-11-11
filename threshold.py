# use coins.jpg image for better understanding and results.

import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(image, (5,5), 0)    # (3,3) represent the colonel image   and o represent standard deviation

cv2.imshow("Gaussian blurr", blurred)    # use Gaussian blurring techniques

#simple Thresholding using binary # if the value exceed 155 then it is directly assign 255
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)   # cv2.Thresh_Binary technique
cv2.imshow("Threshold Binary", thresh)

#simple Thresholding using inv binary
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Inv Binary", threshInv)

cv2.imshow("Only Coins", cv2.bitwise_and(image, image, mask = threshInv))


#adaptive thresholding using mean
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive mean", thresh)

#adaptive thresholding using gaussian
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive gaussian", thresh)



cv2.waitKey(0)