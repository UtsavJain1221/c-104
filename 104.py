import cv2

img = cv2.imread("butterfly.jpg")


#print(img)


text_to_show = "I love coding"

cv2.putText(img,
            text_to_show,
            (20,220),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,255)
            )
#gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#v2.imshow("Grayscale", gray_img)

cv2.imshow("Display Image",img)
cv2.waitKey(0)
