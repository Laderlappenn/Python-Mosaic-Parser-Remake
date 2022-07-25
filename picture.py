import os

from PIL import Image, ImageDraw, ImageFile

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True


def create_canvas():
    square = Image.new('RGB', (10000, 10000), 'white')
    square.save('square.jpg')
    pass


def get_sample_data() -> object:
    main_pic = Image.open("main_pic.jpg")
    main_pic = main_pic.resize((10000, 10000))
    pix = main_pic.load()
    main_pic.save('main_pic.jpg')

    return pix

def get_area_data(x: int, y: int , pix: object):
    r = []
    g = []
    b = []
    for i in range(x, x+100):
        for j in range(y, y+100):
            r.append(pix[i, j][0])
            g.append(pix[i, j][1])
            b.append(pix[i, j][2])

    avg_r = sum(r) / len(r)
    avg_g = sum(g) / len(g)
    avg_b = sum(b) / len(b)
    avg_list = [avg_r, avg_g, avg_b]

    return avg_list


def get_pic(avg_r, avg_g, avg_b, edge=40):
    dir_r = avg_r
    dir_g = avg_g
    dir_b = avg_b

    # TODO delete cringe
    if dir_r > 200:
        dir_r = 200
    if dir_r > 150 and dir_r < 200:
        dir_r = 150
    if dir_r > 100 and dir_r < 150:
        dir_r = 100
    if dir_r > 50 and dir_r < 100:
        dir_r = 50
    if dir_r > 0 and dir_r < 50:
        dir_r = 0

    if dir_g > 200:
        dir_g = 200
    if dir_g > 150 and dir_g < 200:
        dir_g = 150
    if dir_g > 100 and dir_g < 150:
        dir_g = 100
    if dir_g > 50 and dir_g < 100:
        dir_g = 50
    if dir_g > 0 and dir_g < 50:
        dir_g = 0

    if dir_b > 200:
        dir_b = 200
    if dir_b > 150 and dir_b < 200:
        dir_b = 150
    if dir_b > 100 and dir_b < 150:
        dir_b = 100
    if dir_b > 50 and dir_b < 100:
        dir_b = 50
    if dir_b > 0 and dir_b < 50:
        dir_b = 0

    parent_dir = "./pics"
    directory = f"{dir_r} {dir_g} {dir_b}"
    path = os.path.join(parent_dir, directory)

    for pic in os.listdir(path):
        with open(os.path.join(path, pic), 'r+b') as opened_pic:
            pic_Image = Image.open(opened_pic)

            with open('used_pics.txt', 'r') as used_pics:
                name = opened_pic.name
                if name in used_pics:
                    print('skip pic')
                    continue


            r = []
            g = []
            b = []
            for x in range(100):
                for y in range(100):
                    r.append(pic_Image.getpixel((x, y))[0])
                    g.append(pic_Image.getpixel((x, y))[1])
                    b.append(pic_Image.getpixel((x, y))[2])

        pic_avg_r = sum(r) / len(r)
        pic_avg_g = sum(g) / len(g)
        pic_avg_b = sum(b) / len(b)

        coefficient_r = abs(int(avg_r) - int(pic_avg_r))
        coefficient_g = abs(int(avg_g) - int(pic_avg_g))
        coefficient_b = abs(int(avg_b) - int(pic_avg_b))

        if coefficient_r < edge or coefficient_g < edge or coefficient_b < edge:
            with open('used_pics.txt', 'a') as used_pic:
                used_pic.write(opened_pic.name)
            return pic_Image
        elif edge > 100:
            return edge
        else:
            edge += 10


def paste_pic_on_canvas(x,y, pic):
    square = Image.open("square.jpg")
    square.paste(pic, (x, y))
    square.save('square.jpg')
    pass


def main():
    # create_canvas()
    # file_url = open('used_pics.txt', 'w')
    pix = get_sample_data()

    x = 0
    y = 0
    area_pix = get_area_data(x, y, pix)
    print(area_pix)
    x=0
    y=0
    paste_pic_on_canvas(x, y, get_pic(area_pix[0], area_pix[1], area_pix[2]))

if __name__ == "__main__":
    main()
