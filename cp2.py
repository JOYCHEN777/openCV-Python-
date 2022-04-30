import cv2

# 改变图片形状 resize 裁剪crop
img = cv2.imread("Resources/lambo.PNG")
print(img.shape)
imgResized = cv2.resize(img, (300, 200))
print(imgResized.shape)
imgCropped = img[0:200, 200:500]
print(imgCropped.shape)
cv2.imshow("img",img)
cv2.imshow("img2",imgCropped)

cv2.waitKey(0)