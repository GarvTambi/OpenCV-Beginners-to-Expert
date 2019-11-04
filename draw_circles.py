import numpy as np
import cv2

#define a canvas of size 300x300 px, with 3 channels (R,G,B) and data type as 8 bit unsigned integer
canvas = np.zeros((300,300,3), dtype ="uint8")

#define color
#draw a circle
#arguments are canvas/image, midpoint, radius, color, thickness(optional)
#display in cv2 window
green = (0,255,0)
cv2.circle(canvas,(100,100), 10, green)  # center (100,100) with radius of 10 px
cv2.imshow("Single circle", canvas)
cv2.waitKey(0)


# clearing the canvas
canvas = np.zeros((300,300,3), dtype ="uint8") # clearing the canvas


# draw concentric white circles
# calculate the center point of canvas
# generate circles using for loop
white = (255,255,255)
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)   # to calculate the center point of the canvas

for r in range(0,175,25):    # start from 0 and end at 175 with the gap of 25px
    cv2.circle(canvas, (centerX,centerY), r, white)

cv2.imshow("concentric circles", canvas)
cv2.waitKey(0)


# generate random radius, center point, color
# draw circles in for loop

canvas = np.zeros((300,300,3), dtype ="uint8") # for clearing the canvas or for new canvas
for i in range(0, 25):                         # loop run 25 times
    radius = np.random.randint(5, high = 200)      # the range of radius vary between o to 200 
    color = np.random.randint(0, high = 256, size = (3,)).tolist()    # the range of color vary from 0 to 256  and size = (3,) means colour has 3 channels i.e bgr
    pt = np.random.randint(0, high = 300, size = (2,))        #  the range of x and y coordinate is 0 to 300 and size = (2,) means (x,y) coordinate
    cv2.circle(canvas, tuple(pt), radius, color, -1)        # format of representation of circle in cv2
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)