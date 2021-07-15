import cv2
import numpy as np

# 画图，np.unit8 是2^8=256 就是每个像素点取值0-255
img = np.zeros((512, 512, 3), np.uint8)  # 512 512 rgb
print(img)
img[:] = 0, 255, 0  # 设置颜色 BGR

cv2.imshow("img", img)
cv2.waitKey(0)
