import numpy as np
import cv2 as cv

def calcHist(img):
    count = np.zeros(256, dtype="uint32")
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            count[img[i, j]] += 1
    return count

imgInput = cv.imread("einsten.jpg", 0)
height, width = imgInput.shape
imgOutput = np.zeros((height, width), dtype="uint8")

totalPixels = height * width
count = calcHist(imgInput)
rangePixels = len(count)

pr = [i/totalPixels for i in count]
ps = np.zeros(rangePixels, dtype="uint8")

sum = 0

for k in range(rangePixels):
    sum += pr[k] 
    ps[k] = int(round(sum * (rangePixels - 1)))

# print(pr)
# print(ps)

for i in range(height):
    for j in range(width):
        imgOutput[i, j] = ps[imgInput[i, j]]

cv.imshow("Original", imgInput)
cv.imshow("Equalizacao Histograma", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()
