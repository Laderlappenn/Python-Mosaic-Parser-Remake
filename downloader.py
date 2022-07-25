import os

import requests
from PIL import Image

from parser import get_urls_from_html


def save_jpg_with_data(url_list):
    for i in range(len(url_list)):

        # TODO prevent hit bad urls in url list
        try:
            r = requests.get(url_list[i])
            if 'https://www.gstatic.com/ui/v1/menu/' in url_list[i]:
                print('skip')
                continue

        except Exception as _ex:
            continue
        with open('./pic.jpg', 'w+b') as pic:
            pic.write(r.content)

        pic = Image.open('pic.jpg')
        if pic.mode != 'RGB':
            pic = pic.convert('RGB')
        pic = pic.resize((100, 100))
        pix_pic = pic.load()

        r = []
        g = []
        b = []
        for y in range(100):
            for x in range(100):
                # ??? def load(self) -> None: ...
                r.append(pix_pic[x, y][0])
                g.append(pix_pic[x, y][1])
                b.append(pix_pic[x, y][2])

        avg_r = round(sum(r) / len(r))
        avg_g = round(sum(g) / len(g))
        avg_b = round(sum(b) / len(b))


        avg_r = round(avg_r / 10) * 10
        avg_g = round(avg_g / 10) * 10
        avg_b = round(avg_b / 10) * 10


        # TODO delete cringe
        if avg_r > 200:
            avg_r = 200
        if avg_r > 150 and avg_r < 200:
            avg_r = 150
        if avg_r > 100 and avg_r < 150:
            avg_r = 100
        if avg_r > 50 and avg_r < 100:
            avg_r = 50
        if avg_r > 0 and avg_r < 50:
            avg_r = 0

        if avg_g > 200:
            avg_g = 200
        if avg_g > 150 and avg_g < 200:
            avg_g = 150
        if avg_g > 100 and avg_g < 150:
            avg_g = 100
        if avg_g > 50 and avg_g < 100:
            avg_g = 50
        if avg_g > 0 and avg_g < 50:
            avg_g = 0

        if avg_b > 200:
            avg_b = 200
        if avg_b > 150 and avg_b < 200:
            avg_b = 150
        if avg_b > 100 and avg_b < 150:
            avg_b = 100
        if avg_b > 50 and avg_b < 100:
            avg_b = 50
        if avg_b > 0 and avg_b < 50:
            avg_b = 0


        parent_dir = "./pics"
        directory = f"{avg_r} {avg_g} {avg_b}"
        path = os.path.join(parent_dir, directory)

        if not os.path.isdir(f"./pics/{avg_r} {avg_g} {avg_b}"):
            os.mkdir(path)

        pic_name = url_list[i].replace('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9Gc', '').replace('&usqp=CAU', '')
        print(f'{i}.{pic_name}')

        if os.path.isfile(f'./pics/{avg_r} {avg_g} {avg_b}/{pic_name}.jpg'):
            print('skip')
            continue


        # ??? def load(self) -> None: ...
        r = requests.get(url_list[i])

        with open(f'{path}/{pic_name}.jpg', 'w+b') as pic_in_dir:
            pic_in_dir.write(r.content)

        pic_in_dir = Image.open(f'./pics/{avg_r} {avg_g} {avg_b}/{pic_name}.jpg')
        if pic_in_dir.mode != 'RGB':
            pic_in_dir = pic_in_dir.convert('RGB')
        pic_in_dir = pic_in_dir.resize((100, 100))
        pic_in_dir.save(f'./pics/{avg_r} {avg_g} {avg_b}/{pic_name}.jpg')

    pass



if __name__ == "__main__":
    for i in range(20):
        url_list = get_urls_from_html()
        save_jpg_with_data(url_list)