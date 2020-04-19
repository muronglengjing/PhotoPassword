import cv2

array = cv2.imread("photo.bmp")

for i in array:
    for j in i:
        print(chr(int(j[0]*65536+j[1]*256+j[2])), end="")
