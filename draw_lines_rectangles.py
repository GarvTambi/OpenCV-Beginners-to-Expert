import numpy as np  # import numpy library
import cv2     # import  cv2 library

#define a canvas of size 300x300 px, with 3 channels (R,G,B) and data type as 8 bit unsigned integer means 0 - 255
canvas = np.zeros((300,300,3), dtype ="uint8")

#define color
#draw the line
#arguments are canvas/image, starting point, ending point, color, thickness(optional)
#display in cv2 window
green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green) # (0,0) is starting coordinates and (300,300) is ending coordinates oof line
cv2.imshow("The line 1", canvas)        # to show the line on canvas
cv2.waitKey(0)    # wait for key press from keyboard

# draw line with thickness with thickness = 3
red = (0,0,255)
cv2.line(canvas,(0,0),(300,300),red, 3)
cv2.imshow("The line 2", canvas)
cv2.waitKey(0)

#draw rectangles
green = (0,255,0)
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("The rectangle 1", canvas)
cv2.waitKey(0)

# draw rectangles with thickness 3
red = (0,0,255)
cv2.rectangle(canvas,(10,10),(60,60),red, 3)
cv2.imshow("The rectangle 2", canvas)
cv2.waitKey(0)


# draw filled rectangles
blue = (255,0,0)
cv2.rectangle(canvas,(10,10),(60,60),blue, -1)
cv2.imshow("The rectangle 3", canvas)
cv2.waitKey(0)