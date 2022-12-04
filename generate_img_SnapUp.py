"""
Date:2022/12/04
Version for snap up the concert tickets.
"""
import os,sys
import cv2
import numpy as np
import random
import string
import re
from PIL import ImageFont, ImageDraw, Image


def draw_bg():
    canvas = [0]*12000
    # range為圖片長*寬*顏色(彩色*3、黑白*1)
    return canvas


def gen_char(chars=string.ascii_lowercase):
    # Only catch lowercase.
    return ''.join(random.choice(chars) for _ in range(4))


def get_fonttype():
    type_folder = 'fonts'
    type_list = ['Arial.ttf',
                 'Arial.ttf',
                 'Arial.ttf']
    return type_folder + '/' + type_list[random.randint(0, 2)]


def putText2(text, folder):
    img = Image.open(f"{folder}/{text}.jpg")
    # font_type = ImageFont.load_default()
    font_type = get_fonttype()
    font_size = 45
    origin = (9, 22) # (x, y)
    font = ImageFont.truetype(font_type, font_size, encoding='utf-8')
    draw = ImageDraw.Draw(img)
    draw.text(origin, text, font=font, fill=255)
    # img.show()
    img.save(f"{folder}/{text}.jpg")
    return text


def main(folder):
    text = gen_char()
    # 讓m或w不同時出現，否則會超出圖片邊界
    while re.search('[w]|[m]{2,}]', text):
        text = gen_char()
        print(text)

    # 設定圖片長、寬、顏色(彩色:3、黑白:1)
    img = np.resize(draw_bg(), (100, 120, 1))
    pic_name = f'{folder}/{text}.jpg'
    cv2.imwrite(pic_name, img)
    putText2(text, folder)




if __name__ == "__main__":
    loop_time = int(sys.argv[1])
    folder_name = str(sys.argv[2])
    os.makedirs(f'./{folder_name}', exist_ok=True)
    for _ in range(loop_time):
        main(folder_name)

    # ex. python generate_img.py 10 folder_name



