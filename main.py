import cv2 as cv
import numpy as np
# from imageio import imread, imwrite

def myCrazyFunctionThatDrawsShapes(src_img):
    pts = [(50, 50), (80, 150), (170, 30)]
    cv.polylines(src_img, np.array([pts]), True, (255,0,255), 5) # TRIANGLE
    cv.circle(src_img, (150, 150), 40, (255, 0, 0), 3) # CIRCLE
    cv.rectangle(src_img, (10, 10), (200, 200), (0, 255, 0), 5) # RECTANGLE
    cv.putText(src_img, 'ZAIMOGLU', (50, 250),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_AA) # ALSO MY LAST NAME
    return src_img

original = cv.imread("./resources/eifellTower.jpg")

result_image = myCrazyFunctionThatDrawsShapes(original.copy())
cv.imshow("ZAIMOGLU",result_image)

cv.imshow("Eifell",original)
cv.waitKey()

for gamma in [1,0.1,0.5,1.2,2.2,4,10]:
    gamma_corrected = np.array(255 * ((original/255) ** gamma),dtype='uint8')
    cv.imshow("Gamma "+ str(gamma), gamma_corrected)
    cv.waitKey()