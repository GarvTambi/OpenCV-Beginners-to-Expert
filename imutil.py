import numpy as np
import cv2
def translate(image, x, y):
	# M is a translation matrix
	# Our translation matrix M is defined as a floating point array because OpenCV expects this matrix to be of floating point type to be passed to the function
	M = np.float32([[1,0,x], [0, 1, y]])  # x denoes no. of pixels shifted towards x- axis and y denotes no. of pixels shifted up and down
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) # image.shape[1] denote width of the image  and image.shape[0] denotes height of the image
	return shifted

 
def rotate(image, angle, center = None, scale = 1.0):
	(h, w) = image.shape[:2]  # to find the width and height of the im

	if center is None:
		center = (w // 2, h // 2)      # to find the center of the image

	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w,h))
	return rotated


def resize(image, width =  None, height = None, inter = cv2.INTER_AREA):     # interpolation is the algorithm in imaageprocessing which is used to resizing the image
	dim = None       # dim = dimension of image
	(h, w) = image.shape[:2]    # height and width of the iomage

	if width is None and height is None:
		return image

	if width is None:
		r = height/float(h)
		dim = (int(w * r), height)
	else:
		r = width/float(w)
		dim = (width, int(h * r))

	resized = cv2.resize(image, dim, interpolation = inter)
	return resized
