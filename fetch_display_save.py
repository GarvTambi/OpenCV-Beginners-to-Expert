import argparse   # to pass the argument in the terminal
import cv2     # to import the library

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])      # to read the image
print("width of the image in pixels is: {}".format(image.shape[1]))
print("height of the image in pixels is: {}".format(image.shape[0]))
print("channels present the image is: {}".format(image.shape[2]))

# load image into cv2 window
# wait for key press
# write image into another format
cv2.imshow("Image Title", image)     # to show the image
cv2.waitKey(0)     # wait until any key press from keyboard
cv2.imwrite("newcat.jpg", image)    # to save the image