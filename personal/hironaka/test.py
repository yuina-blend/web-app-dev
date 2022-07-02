import cv2
import numpy as np

img = np.zeros((400, 400, 3), np.uint8)
img[:,:] = [255, 255, 255]

cv2.putText(img, 'HELLO', (int(img.shape[0]/3), int(img.shape[1]/2)), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 5, cv2.LINE_AA)

cv2.imwrite('image/textimg.jpg', img)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()