# imutil library  defines in imutil.py

import argparse   # import argument
import imutil       # import imutil file for translate function
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])

# shift image down
shifted = imutil.translate(image, 0, 100)   #  shift image down by 100 px
cv2.imshow("shifted down image", shifted)
cv2.waitKey(0)


# shift image up 
shifted = imutil.translate(image,0,-100)   # shift image up by -100 px
cv2.imshow("shifted up image", shifted)
cv2.waitKey(0)

#shift image right
shifted = imutil.translate(image,100,0)     # shift image by right by 100 px
cv2.imshow("shifted right image",shifted)
cv2.waitKey(0)

#shift image right and down
shifted = imutil.translate(image, 100, 50)    # shift image right by 100 px and down by 50 px
cv2.imshow("Shifted right image", shifted)
cv2.waitKey(0)