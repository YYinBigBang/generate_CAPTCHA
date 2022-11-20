"""Generate the Captcha code image"""
import cv2
import numpy as np
import random
import string

def draw_dot():
    canvas = []
    # range為圖片長*寬*顏色(彩色*3、黑白*1)
    for _ in range(2700):
        dot = random.randint(1, 15)
        # 黑點散布機率為1/15
        if dot % 14 == 0:
            canvas.append(0)
        else:
            canvas.append(255)
        # data = np.resize(canvas, (30, 90, 1))
        # cv2.imwrite('test.jpg', data)

    return canvas


def draw_lines(img):
    for _ in range(random.randint(1, 5)):
        x1 = random.randint(0, 90)
        y1 = random.randint(0, 30)
        x2 = random.randint(0, 90)
        y2 = random.randint(0, 30)
        color = (0, 0, 0)
        thickness = 1
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)

    return img


def overlay(pic1, pic2):
    _pic1 = cv2.imread(pic1)
    _pic2 = cv2.imread(pic2)
    output = cv2.add(_pic1, _pic2)
    return output


def gen_char(chars=string.ascii_lowercase + string.digits):
    #TODO:數字最多占3個
    return ''.join(random.choice(chars) for _ in range(5))


def putText(img):
    text = gen_char()
    origin = (10, 23)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.75
    color = (0, 0, 0)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(img, text, origin, fontFace, fontScale, color, thickness, lineType)
    return text


def main():
    # 設定圖片長、寬、顏色(彩色:3、黑白:1)
    img = np.resize(draw_dot(), (30, 90, 1))
    img = draw_lines(img)
    pic_name = putText(img)
    cv2.imwrite(f'{pic_name}.jpg', img)




if __name__ == "__main__":
    main()

    # TODO(ok):generate the randomly dot
    # TODO(OK):lower case letters and digits generation
    # TODO(ok): record the verification string
    # TODO(ok):draw lines randomly (line 1~5)
    # TODO:overlay picture
