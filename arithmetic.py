import numpy as np
import cv2

print("max of 255 by cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("max of 255 by cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("max of 255 by np: {}".format(np.uint8([200])+ np.uint8([100])))
print("max of 255 by np: {}".format(np.uint8([50])- np.uint8([100])))
