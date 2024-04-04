import numpy as np
import cv2 as cv

def calcHist(img):
    count = np.zeros(256, dtype="uint32")
    rows, cols = img.shape
    totalPixels = rows * cols

    for i in range(rows):
        for j in range(cols):
            count[img[i, j]] += 1
    return count/totalPixels

def equalization(img):
    hist = calcHist(img)
    histEqualizated = np.zeros(256, dtype="uint8")

    sum = 0
    for k in range(256):
        sum += hist[k] 
        histEqualizated[k] = int(round(sum * 255))
    return histEqualizated

imgInput = cv.imread("luna.jpg", 0)
height, width = imgInput.shape

imgReference = cv.imread("lunaReferencia.jpg", 0)

imgOutput = np.zeros((height, width), dtype="uint8")

inputEqualization = equalization(imgInput)
referenceEqualization = equalization(imgReference)

inputToOutput = np.zeros(256, dtype="uint8")
j = 0
for i in range(256):
    inputValue = i
    eqInputValue = inputEqualization[i]

    while(j < 255 and abs(int(eqInputValue) - int(referenceEqualization[j + 1])) <= abs(int(eqInputValue) - int(referenceEqualization[j]))):
        j+=1
    inputToOutput[inputValue] = j


for i in range(height):
    for j in range(width):
        imgOutput[i, j] = inputToOutput[imgInput[i, j]]

cv.imshow("Original", imgInput)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("Referencia", imgReference)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("Especificacao Histograma", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()
