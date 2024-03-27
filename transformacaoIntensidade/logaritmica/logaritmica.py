import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgInput = cv.imread("fourier.jpg", 0)

c = 255/np.log10(1 + np.max(imgInput))
imgOutput = np.array(
    c * np.log10(imgInput + 1), 
    dtype="uint8"
)
        
cv.imshow("Original", imgInput)
cv.imshow("Transformacao Logaritmica", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("fourier_output.jpg", imgOutput)

plt.hist(imgInput.ravel(), 256, [0, 256])
plt.savefig("hist_fourier_input.jpg")
plt.cla()
plt.hist(imgOutput.ravel(), 256, [0, 256])
plt.savefig("hist_fourier_output.jpg")