import cv2

img = cv2.imread("butterfly.jpg")

text_to_show = ("I love programming")
cv2.putText(img,
            text_to_show,
            (100,100),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,255) )

cv2.imshow("Display Image" , img)
cv2.waitKey(0)