import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
#cv2.waitKey(0)

#generating one array and multiplying it with 100 px
#adding that array to the actual image numpy array
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)                # adding pixel in the given image
cv2.imshow("Added image", added)


#generating one array and multiplying it with 50 px
#substracting that array to the actual image numpy array
M = np.ones(image.shape, dtype = "uint8") * 100
subtracted = cv2.subtract(image, M)             # subtracting pixel in the given image
cv2.imshow("Subtracted image", subtracted)

cv2.waitKey(0)

