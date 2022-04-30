import numpy as np
import cv2

img=np.zeros((512,512), np.uint8)
#cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 255), 3)
print(img)
cv2.imshow("a",img)
cv2.waitKey(0)