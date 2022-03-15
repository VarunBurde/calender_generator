import calendar
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import os

class calender_creater:
    def __init__(self):
        self.col = 4
        self.width = 2
        self.lines = 2
        self.space = 4
        self.img_location = "images"
        self.emoji_location = "emoji"
        self.Name = None
        self.i_start = None
        self.i_end = None
        self.life_expectancy = None
        self.s_cal_w = 1670
        self.s_cal_h = 1550
        self.white_line = np.ones((self.s_cal_h, 10, 3)) * 0
        self.black_line = np.ones((self.s_cal_h, 10, 3)) * 255.0
        self.cal_w = None
        self.calender = None
        self.black_line_horizontal = None
        self.white_line_horizontal = None

    def get_data(self):
        print("Enter your name")
        self.Name = input()
        print("Enter your birth year")
        self.i_start = int(input())
        print("Enter you life expectancy")
        self.life_expectancy = input()
        if (int(self.life_expectancy) % 8) == 0:
            years = int(self.life_expectancy)
        else:
            years = int(self.life_expectancy) + (8 - (int(self.life_expectancy) % 8))
        self.i_end = int(self.i_start) + years
        self.create_images()
        self.combine_images()
        self.cal_row_w = None


    def create_images(self):

        if not os.path.isdir(self.img_location):
            os.mkdir(self.img_location)

        for i in range(self.i_start,self.i_end):
            print("generating year", i )
            img = Image.new('RGB', (self.s_cal_w, self.s_cal_h), color = (255,255,255))
            fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
            ImageDraw.Draw(img).text((0,0),calendar.TextCalendar(calendar.MONDAY).formatyear(i, self.width, self.lines, self.space, self.col) , font=fnt, fill=(0,0,0))
            img_path = os.path.join(self.img_location,'{}.png'.format(i) )
            img.save(img_path)

    def make_start(self):
        img = Image.new('RGB', (self.cal_row_w, 200), color=(255, 255, 255))
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 100)
        ImageDraw.Draw(img).text((0, 0), "Hello " + self.Name + ", this is your life", font=fnt, fill=(0, 0, 0))
        img_path = os.path.join(self.img_location, 'start.png')
        img.save(img_path)

    def make_end(self):
        img = Image.new('RGB', (self.cal_row_w, 200), color=(255, 255, 255))
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 100)
        ImageDraw.Draw(img).text((0, 0), "Hello " + self.Name + ", end is near live your life to fullest", font=fnt, fill=(0, 0, 0))
        img_path = os.path.join(self.img_location, 'end.png')
        img.save(img_path)

    def make_cal_row(self, c, j):
        img = {}
        dim = (self.s_cal_w, self.s_cal_h)
        for k in range(c):
            print(j+k, self.i_end)
            if self.i_start == j+k:
                print("baby", j+k)
                img[k] = cv2.imread(os.path.join(self.emoji_location, 'baby.png'))
                img[k] = cv2.resize(img[k], dim, interpolation=cv2.INTER_AREA)

            elif self.i_start + 18 == j+k:
                print("boy", j+k)
                img[k] = cv2.imread(os.path.join(self.emoji_location, 'boy.png'))
                img[k] = cv2.resize(img[k], dim, interpolation=cv2.INTER_AREA)

            elif self.i_start + 35 == j+k:
                print("man", j+k)
                img[k] = cv2.imread(os.path.join(self.emoji_location, 'man.jpeg'))
                img[k] = cv2.resize(img[k], dim, interpolation=cv2.INTER_AREA)

            elif self.i_start + 60 == j+k:
                print("old", j+k)
                img[k] = cv2.imread(os.path.join(self.emoji_location, 'old.jpeg'))
                img[k] = cv2.resize(img[k], dim, interpolation=cv2.INTER_AREA)

            elif self.i_end-1 == j+k :
                print("Skull", j+k)
                img[k] = cv2.imread(os.path.join(self.emoji_location, 'skull.png'))
                img[k] = cv2.resize(img[k], dim, interpolation=cv2.INTER_AREA)
            else:
                img[k] = cv2.imread(os.path.join(self.img_location, str(j+k) + '.png'))
        image_ver = [self.white_line, self.black_line, img[0], self.white_line, self.black_line, img[1],
                     self.white_line, self.black_line, img[2], self.white_line, self.black_line, img[3],
                     self.white_line, self.black_line, img[4], self.white_line, self.black_line, img[5],
                     self.white_line, self.black_line, img[6], self.white_line, self.black_line, img[7],
                     self.white_line]

        cal_row_img = np.concatenate(image_ver, axis=1)
        return cal_row_img

    def combine_images(self):
        print("this tempelate is for A3 paper")
        c = 8
        self.cal_row_w = c * self.s_cal_w + 170
        black_line_horizontal = np.ones((10, self.cal_row_w, 3))
        self.calender = np.ones((10, self.cal_row_w, 3))
        for j in range(self.i_start, self.i_end, c):
            print("loading year", j)
            cal_row_img = self.make_cal_row(c, j)
            self.calender = cv2.vconcat([self.calender, cal_row_img, black_line_horizontal])
        self.make_start()
        self.make_end()
        start_img = cv2.imread(os.path.join(self.img_location, "start.png"))
        end_img = cv2.imread(os.path.join(self.img_location, "end.png"))
        f_image = [start_img, self.calender, end_img]
        calender_final = np.concatenate( f_image, axis=0)
        cv2.imwrite("calender.jpeg", calender_final)