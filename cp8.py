import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# 获取轮廓
def getContours(img):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contour:
        area = cv2.contourArea(c)
        # print(area)
        if area > 500:
            cv2.drawContours(imgContour, c, -1, (255, 0, 0),3)
            peri = cv2.arcLength(c, True)  # 算周长
            # print(peri)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            if objCor == 3:
                objType = "Tri"
            elif objCor == 4:
                # 通过长宽比判断是正方形还是长方形 aspectRatio
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objType = "Square"
                else:
                    objType = "rectangle"
            elif objCor > 4:
                objType = "Cycle"
            else:
                objType = "other"
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(imgContour, objType, (x + w // 2 - 10, y + h // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 255), 2)


path = "Resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()

imgBlank = np.zeros_like(img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgStk = stackImages(0.8, [[img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]])
imgBlank = np.zeros_like(img)

print(imgCanny.shape)
print(img.shape)
cv2.imshow("img", imgStk)
cv2.waitKey(0)
