import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("BGR Color Space", image)
cv2.waitKey(0)

# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)

# BGR to HSV
# the Hue-saturation-Value(HSV) color space is more similar to the humans think and conceive of color.
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# BGR to LAB
# LAB  color space is a 3-axis color system with dimensions L for lightness and a and b for the color dimensions.
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

cv2.waitKey(0)

