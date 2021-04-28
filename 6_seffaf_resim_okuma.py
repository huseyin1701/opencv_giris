import cv2 as cv

resim = cv.imread("resim/seffaf.png", cv.IMREAD_UNCHANGED)
cv.imshow("Baslik", resim)
cv.waitKey(3000)

print(resim)