import cv2
from PIL import Image
import numpy as np

img = cv2.imread("img6.bmp")
width, height, bit = np.shape(img)

for i in range(0, width):
    for j in range(0, height):
        img[j][i][0] = 255 - img[j][i][0]
        img[j][i][1] = 255 - img[j][i][1]
        img[j][i][2] = 255 - img[j][i][2]
        
cv2.imshow('image', img)
cv2.waitKey(0)        
