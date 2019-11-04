import argparse   # to pass the argument
import cv2   # to import the openCV library

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])      # to read the image

# grab the pixel at (0,0) of the image and print the color values
(b,g,r) = image[0,0]
print("pixel at (0,0)- Red: {} , Green: {} , Blue: {}".format(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print("pixel at (0,0)- Red: {} , Green: {} , Blue: {}".format(r,g,b))



#grap the region and show in the cv2 window
corner = image[0:100, 0:100]     # to specify the corner

# load image into cv2 window
# wait for key press
# write image into another format

# cv2.imshow("Image Title", image)     # to show the image
# cv2.waitKey(0)     # wait until any key press from keyboard


# change color of the area of image
image[0:100, 0:100] = (0,255,0)     # to specify the corner 
cv2.imshow("color of area changed", image)
cv2.waitKey(0)