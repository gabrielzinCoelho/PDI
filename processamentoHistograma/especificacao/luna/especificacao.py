import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

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

imgInput = cv.imread("assets/luna.jpg", 0)
height, width = imgInput.shape

imgReference = cv.imread("assets/lunaReferencia.jpg", 0)

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

cv.imwrite("luna_output.jpg", imgOutput)

plt.plot(range(256), inputToOutput, 'b')
plt.savefig("funcao_transformacao.jpg")
plt.show()
cv.waitKey(0)
plt.close()

plt.plot(range(256), referenceEqualization, 'g', referenceEqualization, range(256), 'b', range(256), range(256), 'r--')
plt.savefig("funcao_inversa.jpg")
plt.show()
cv.waitKey(0)
plt.close()

plt.hist(imgInput.ravel(), 256, [0, 256], color="g")
plt.hist(imgReference.ravel(), 256, [0, 256], color="b")
plt.hist(imgOutput.ravel(), 256, [0, 256], color="r")
plt.savefig("histogramas_juntos.jpg")
plt.show()
cv.waitKey(0)
plt.close()

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
for i, img in enumerate((imgInput, imgReference, imgOutput)):
    axs[i].plot(range(256), calcHist(img))
plt.savefig("histogramas.jpg")
plt.show()
cv.waitKey(0)
plt.close()