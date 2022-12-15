import cv2 as cv
import numpy as np
from imageio import imread, imwrite


original = cv.imread("./resources/eifellTower.jpg")

cv.imshow("Eifell",original)
cv.waitKey()

for gamma in [1,0.1,0.5,1.2,2.2,4,10]:
    gamma_corrected = np.array(255 * ((original/255) ** gamma),dtype='uint8')
    cv.imshow("Gamma "+ str(gamma), gamma_corrected)
    cv.waitKey()