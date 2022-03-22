import cv2
# Always use: pip install opencv-python

def meanfilter():
    count = 0
    img = cv2.imread('peppers_gray_ruido.bmp')
    while count < 3:
        img = cv2.blur(img, (3, 3))
        cv2.imshow('blur Method', img)
        cv2.waitKey()
        count += 1


def medianfilter():
    count = 0
    img = cv2.imread('peppers_gray_ruido.bmp')
    while count < 3:
        img = cv2.medianBlur(img, 3)
        cv2.imshow('medianBlur Method', img)
        cv2.waitKey()
        count += 1


option = int(input("Which filter do you want? Type 1 for mean filter and 2 for median filter."))
if option == 1:
    meanfilter()
elif option == 2:
    medianfilter()
else:
    print("\nThis is not a option. Program closed.")

