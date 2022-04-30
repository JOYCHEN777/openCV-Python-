import cv2

print("pakage imported")

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3-weight
cap.set(4, 640)  # 4-height
cap.set(10, 10)

while True:
    # 读取摄像头当前这一帧的画面  success:True False image:当前这一帧画面
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
