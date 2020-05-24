import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('messi5.jpg', 0)
cv2.namedWindow('Trackbar')

cv2.createTrackbar('X', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('Y', 'Trackbar', 0, 255, nothing)

while(True):
    cv2.imshow('Trackbar', img)
    k = cv2.waitKey(1) & 0xFF

    x = cv2.getTrackbarPos('X', 'Trackbar')
    y = cv2.getTrackbarPos('Y', 'trackbar')
    canny = cv2.Canny(img, x, y)
    titles = ['Image', 'canny']
    images = [img, canny]

    if k == 27:
        break

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()
