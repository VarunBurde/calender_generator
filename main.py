# import calendar
# import cv2
# import numpy as np
# from PIL import Image, ImageFont, ImageDraw
# import os
#
# col = 4
# width = 2
# lines = 2
# space = 4
# img_location = "images"
#
#
# print("Enter your name")
# Name = input()
#
# # img = Image.new('RGB', (13530, 1550), color = (255,255,255))
# # fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 500)
# # ImageDraw.Draw(img).text((0,0),"Hello " + Name + ", this is your life" , font=fnt, fill=(0,0,0))
# # img_path = os.path.join(img_location,'start.png' )
# # img = img.save(img_path)
#
#
# print("Enter your birth year")
# i_start = int(input())
# print("Enter you life expectancy")
# life_expectancy = input()
# i_end = int(i_start) + int (life_expectancy)
#
# for i in range(i_start,i_end):
#     img = Image.new('RGB', (1670, 1550), color = (255,255,255))
#     fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
#     ImageDraw.Draw(img).text((0,0),calendar.TextCalendar(calendar.MONDAY).formatyear(i, width, lines,space, col) , font=fnt, fill=(0,0,0))
#     img_path = os.path.join(img_location,'{}.png'.format(i) )
#     img = img.save(img_path)
#
# white_line = np.ones((1550, 10, 3)) * 0
# black_line = np.ones((1550, 10, 3)) * 255.0
#
# img_cal = dummy_mask = np.ones((10,13530 , 3)) * 255.0
# black_line_horzontal = np.ones((10,13530 , 3))
#
#
# for j in range(i_start, i_end, 8):
#     print("loading year", j)
#     img1 = cv2.imread(os.path.join(img_location, str(j)+ '.png'))
#     img2 = cv2.imread(os.path.join(img_location, str(j + 1) + '.png'))
#     img3 = cv2.imread(os.path.join(img_location, str(j + 2) + '.png'))
#     img4 = cv2.imread(os.path.join(img_location, str(j + 3) + '.png'))
#     img5 = cv2.imread(os.path.join(img_location, str(j + 4) + '.png'))
#     img6 = cv2.imread(os.path.join(img_location, str(j + 5) + '.png'))
#     img7 = cv2.imread(os.path.join(img_location, str(j + 6) + '.png'))
#     img8 = cv2.imread(os.path.join(img_location, str(j + 7) + '.png'))
#
#     image_ver = [white_line, black_line, img1, white_line, black_line, img2,
#                  white_line, black_line, img3, white_line, black_line, img4,
#                  white_line, black_line, img5, white_line, black_line, img6,
#                  white_line, black_line, img7, white_line, black_line, img8,
#                  white_line]
#     image = np.concatenate(image_ver, axis=1)
#     print(image.shape)
#     print(black_line_horzontal.shape)
#     img_cal = cv2.vconcat([img_cal, image, black_line_horzontal])
#     cv2.imwrite("calender.jpeg", img_cal)


from helper.utils import calender_creater

if __name__ == '__main__':
    cal = calender_creater()
    cal.get_data()