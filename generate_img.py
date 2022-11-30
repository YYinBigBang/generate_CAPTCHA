"""Generate the Captcha code image"""
import os,sys
import cv2
import numpy as np
import random
import string
import re
from PIL import ImageFont, ImageDraw, Image


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
    return ''.join(random.choice(chars) for _ in range(5))


def putText(img):
    """Use opencv to draw text"""
    text = gen_char()
    origin = (10, 23)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.75
    color = (0, 0, 0)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(img, text, origin, fontFace, fontScale, color, thickness, lineType)
    return f'{text}.jpg'


def putText2(text, folder):
    """Use PIL(Pillow) to draw text"""
    img = Image.open(f"{folder}/{text}.jpg")
    # font_type = ImageFont.load_default()
    font_type = 'Arial.ttf'
    font_size = 25
    origin = (5, 2.5) # (x, y)
    font = ImageFont.truetype(font_type, font_size, encoding='utf-8')
    draw = ImageDraw.Draw(img)
    draw.text(origin, text, font=font, fill=0)
    # img.show()
    img.save(f"{folder}/{text}.jpg")
    return text


def main(folder):
    text = gen_char()
    while re.search('[mw]{4}]', text):
        text = gen_char()
        print(text)

    # 設定圖片長、寬、顏色(彩色:3、黑白:1)
    img = np.resize(draw_dot(), (30, 90, 1))
    img = draw_lines(img)
    # pic_name = putText(img)
    pic_name = f'{folder}/{text}.jpg'
    cv2.imwrite(pic_name, img)
    putText2(text, folder)




if __name__ == "__main__":
    loop_time = int(sys.argv[1])
    folder = "captcha_data"
    os.makedirs(f'./{folder}', exist_ok=True)
    for _ in range(loop_time):
        main(folder)

    # TODO(ok): generate the randomly dot
    # TODO(ok): lower case letters and digits generation
    # TODO(ok): record the verification string
    # TODO(ok): draw lines randomly (line 1~5)
    # TODO: overlay picture

