import easyocr
import cv2

PROPORTION = 4
reader = easyocr.Reader(['en'])
img = cv2.imread('../image/8.png')
img = cv2.resize(img, (int(img.shape[0] / PROPORTION), int(img.shape[1] / PROPORTION)), cv2.INTER_CUBIC)
cv2.imwrite("../image/8_.png", img=img)
result = reader.readtext('../image/8_.png')
print("result = ", result)
img = cv2.imread('../image/8_.png')

for i, (coordinate, txt, prob) in enumerate(result):
    print(i, "coorinate = ", coordinate, "TXT = ", txt)
    for index in range(4):
        if index < 3:
            img = cv2.line(img, (int(coordinate[index][0]), int(coordinate[index][1])),
                           (int(coordinate[index + 1][0]), int(coordinate[index + 1][1])), color=(255, 0, 0))
        else:
            img = cv2.line(img, (int(coordinate[index][0]), int(coordinate[index][1])),
                           (int(coordinate[0][0]), int(coordinate[0][1])), color=(255, 0, 0))
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)
cv2.waitKey(0)
