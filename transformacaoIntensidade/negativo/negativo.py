import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 

imgInput = cv.imread("./assets/mamografia.jpg", 0)
imgOutput = 255 - imgInput

cv.imshow("Original", imgInput)
cv.imshow("Negativo", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("./negativo/mamografia_output.jpg", imgOutput)

plt.hist(imgInput.ravel(), 256, [0 , 256])
plt.savefig("./negativo/hist_mamografia_input.jpg")
plt.show()

plt.hist(imgOutput.ravel(), 256, [0 , 256])
plt.savefig("./negativo/hist_mamografia_output.jpg")
plt.show()