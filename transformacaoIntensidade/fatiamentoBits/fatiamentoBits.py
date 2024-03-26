import numpy as np
import cv2 as cv

def convertToBinary(num):
    binaryList = [int(i) for i in list("{0:0b}".format(num))]
    for i in range(8 - len(binaryList)):
        binaryList.insert(0, 0)
    return binaryList

imgInput = cv.imread("./assets/pele.jpg", 0)
height, width = imgInput.shape

imgPlanes = np.zeros((height, width, 8), dtype="uint8")

for i, lines in enumerate(imgInput):
    for j, pixel in enumerate(lines):
        imgPlanes[i, j] = convertToBinary(imgInput[i, j])

for i in range(8):
    cv.imshow("Plano {}".format(7 - i), imgPlanes[:, :, i] * 255)
    cv.imwrite("./planosBits/plano{}.jpg".format(7 - i), imgPlanes[:, :, i] * 255)
    cv.waitKey(0)
    cv.destroyAllWindows()

for i in range(8):
    imgOutput = np.zeros((height, width), dtype="uint8")
    for j in range(8):
        imgOutput += imgPlanes[:, :, j] * 2**(7 - j) * int(j <= 7 - i) 
    cv.imshow("{} MSB".format(8 - i), imgOutput)
    cv.imwrite("./planosBits/msb{}.jpg".format(8 - i), imgOutput)
    cv.waitKey(0)
    cv.destroyAllWindows()