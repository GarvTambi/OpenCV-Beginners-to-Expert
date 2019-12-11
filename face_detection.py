from PIL import Image   # Python image library
import face_recognition
import numpy as np
import argparse
import cv2


# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("image",image)
cv2.waitKey(0)

# Find all the faces in the image using the library
face_locations = face_recognition.face_locations(image)   # to detect how many face in the photograph

# printing the number of items in the array
print("I found {} face(s) in this photograph".format(len(face_locations)))

for face_location in face_locations:

	#print location of each face in this image
	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))   # to get the value of,top,bottom,left,right of each of the face in the photograph

	#access and show each face in the image
	face_image = image[top:bottom, left:right]    # forming a canvas of top:bottom and left:right from the value we get above
	pil_image = Image.fromarray(face_image)       # fitting the face in the canvas
	pil_image.show()

