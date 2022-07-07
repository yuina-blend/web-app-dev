import base64

class GenerateTextImage:

    def generate(self, height : int, width : int, backcolor : tuple, text : str, textcolor : tuple, font : int, textsize : int):
        import cv2
        import numpy as np
        img = np.zeros((height, width, 3), np.uint8)
        img[:,:] = backcolor

        cv2.putText(img, text, (int(img.shape[0]/3), int(img.shape[1]/2)), font, textsize, textcolor, 4, cv2.LINE_4)

        cv2.imwrite('static/textimg.jpg', img)

        result, dst_data = cv2.imencode('.jpg', img)
        dst_base64 = base64.b64encode(dst_data).decode().replace("'", "")

        return dst_base64