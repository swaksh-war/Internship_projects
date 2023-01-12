import cv2
import os
import numpy as np
from Crypto.Random import get_random_bytes

key = get_random_bytes(256)
# print(key)
randomByteArray = bytearray(key)
# print(randomByteArray)
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(16,16)
cv2.imwrite('RandomGray.png', grayImage)

img = cv2.imread('RandomGray.png', 0)
img = img.ravel()
key1 = np.ndarray.tobytes(img)
print(key == key1)
