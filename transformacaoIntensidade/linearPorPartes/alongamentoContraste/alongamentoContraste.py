import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgInput = cv.imread("pollen.jpg", 0) 
height, width = imgInput.shape[:2]
imgOutput = np.zeros((height, width), dtype="uint8")

r1 = 97
s1 = 30
r2 = 126
s2 = 150
a1 = s1/r1
a2 = (s2 - s1)/(r2 - r1)
a3 = (255 - s2)/(255 - r2)

# func = np.zeros(256, dtype="uint8")

# for i in range(256):
#     if (i < r1):
#         func[i] = int(a1 * i)
#     elif (i <= r2):
#         func[i] = int(s1 + a2 * (i - r1))
#     else:
#         func[i] = int(s2 + a3 * (i - r2))

rangePixels = range(256)
func = [a1 * i for i in rangePixels[:r1]] + [s1 + a2 * (i - r1) for i in rangePixels[r1:r2 + 1]] + [s2 + a3 * (i - r2) for i in rangePixels[r2 + 1:]]

for i in range(height):
    for j in range(width):
        imgOutput[i, j] = int(func[imgInput[i, j]])

cv.imwrite("pollen_output.jpg", imgOutput)

cv.imshow("Original", imgInput)
cv.imshow("Transformacao de Intensidade por Partes", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()

# histInput = cv.calcHist([imgInput], [0], None, [256], [0, 256])
# histOutput = cv.calcHist([imgOutput], [0], None, [256], [0, 256])

# plt.plot(hist, color='b')

plt.hist(imgInput.ravel(), 256, [0, 256])
plt.savefig("hist_polen_input.jpg")
plt.show()

plt.hist(imgOutput.ravel(), 256, [0, 256])
plt.savefig("hist_polen_output.jpg")
plt.show()

plt.plot(range(256), func)
plt.savefig("func.jpg")
plt.show()
