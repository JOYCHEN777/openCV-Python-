import cv2

frameWidth = 64
frameHeight = 480
minArea = 200
color = (255, 0, 255)
# 先整一个分类器对象，这个对象可以调用一些分类方法（我猜的
nPlateCascad = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
count = 0  # 保存车牌的序号

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlate = nPlateCascad.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlate:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "Car Numbers", (x, y - 5), cv2.FONT_HERSHEY_TRIPLEX, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)
    cv2.imshow("result", img)

    # cv2.waitKey(1) 1为参数，单位毫秒，表示间隔时间
    # ord(' ')将字符转化为对应的整数（ASCII码）
    # waitKey(int delay)键盘绑定函数，共一个参数，表示等待毫秒数，将等待特定的几毫秒，看键盘是否有输入，如果delay大于0，那么超过delayms后，如果没有按键，
    # 那么会返回-1，如果按键那么会返回键盘值,返回值为ASCII值。
    # 如果其参数为0，则表示无限期的等待键盘输入。(其实就是不让while break)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_" + str(count) + ".jpg", imgRoi)
        # 标记下图片被保存，先搞个绿色底，再加上字
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("save",img)
        cv2.waitKey(500)
        count+=1
