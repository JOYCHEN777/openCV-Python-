import cv2
import numpy as np

# 画一些shape和text
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 255), 3)
cv2.rectangle(img, (100, 0), (250, 350), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (300, 300), 100, (255, 0, 0), 5)
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 3)
cv2.imshow("img", img)
cv2.waitKey(0)
