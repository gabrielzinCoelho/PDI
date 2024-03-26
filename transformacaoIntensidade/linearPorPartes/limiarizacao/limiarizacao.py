import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgInput = cv.imread("cameramen.jpg", 0)
height, width = imgInput.shape[:2]
imgOutput = np.zeros((height, width), dtype="uint8")

limiar = 128

for i in range(height):
    for j in range(width):
        imgOutput[i, j] = 255 if imgInput[i, j] >= limiar else 0

cv.imwrite("cameramen_output.jpg", imgOutput)

cv.imshow("Original", imgInput)
cv.imshow("Limiarizacao", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()

plt.hist(imgInput.ravel(), 256, [0, 256])
plt.savefig("hist_cameramen_input.jpg")
plt.show()

plt.hist(imgOutput.ravel(), 256, [0, 256])
plt.savefig("hist_cameramen_output.jpg")
plt.show()