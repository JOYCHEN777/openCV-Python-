import cv2
import numpy as np

# 一些图像处理，变灰，模糊，取边缘等等
img = cv2.imread("Resources/lena.png")
# 卷积核，所有值都是一 np.ones
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 变灰
imgBlur = cv2.GaussianBlur(imgGray, (17, 17), 0)  # 模糊
imgCanny = cv2.Canny(img, 10, 200)  # 边缘
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # 膨胀
imgEroded = cv2.erode(imgDialation, kernel, iterations=3)

cv2.imshow("canny", imgDialation)
cv2.imshow("2", imgEroded)
cv2.imshow("imgGray", imgGray)
cv2.waitKey(0)
