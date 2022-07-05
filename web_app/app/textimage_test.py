import cv2
from GenerateTextImage import GenerateTextImage

textimg = GenerateTextImage()

textimg.generate(400, 400, (255, 255, 255), 'AAA', (0, 255, 0), cv2.FONT_HERSHEY_PLAIN, 5)
