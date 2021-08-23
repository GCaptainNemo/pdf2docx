import easyocr
import cv2
from docx import Document
import pickle


PROPORTION = 4
reader = easyocr.Reader(['en'])
# img = cv2.imread('../image/24.png')
# img = cv2.resize(img, (int(img.shape[0] / PROPORTION), int(img.shape[1] / PROPORTION)), cv2.INTER_CUBIC)
# cv2.imwrite("../image/24_.png", img=img)
# result = reader.readtext('../image/24_.png')
# with open("../result_24.pkl", "wb+") as f:
#     pickle.dump(result, f)
with open("../result_24.pkl", "rb+") as f:
    result = pickle.load(f)

result.sort(key=lambda x: x[0][0][1])  # sort according to y

rows_lst = []
row_lst = []
for i in range(len(result)):
    if not row_lst:
        row_lst.append(result[i])
    elif abs((result[i][0][0][1] + result[i][0][3][1]) / 2 -
             (row_lst[-1][0][0][1] + row_lst[-1][0][3][1]) / 2) < 4:
        row_lst.append(result[i])
    else:
        row_lst.sort(key=lambda x: x[0][0][0])   # sort according to x
        rows_lst.append(row_lst)
        row_lst = []

for i, row in enumerate(rows_lst):
    print("row {} = ".format(i), row)

img = cv2.imread('../image/24_.png')
document = Document()

for i, (coordinate, txt, prob) in enumerate(result):
    # print(i, "coorinate = ", coordinate, "TXT = ", txt)

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

document.save("../test.docx")

