import os
from PIL import Image, ImageDraw,ImageFont, ImageEnhance
import random
import numpy as np
from matplotlib import cm
import cv2
from tqdm import tqdm

from util import *


class ImageGenerator():
    
    def __init__(self, font_dir, output_dir,font_size_min, font_size_max, text_corpus_path, date_corpus_path, img_size=(1280, 720),bg_colour=(255, 255, 255, 255)):
        
        self.img_size=img_size
        self.bg_colour = bg_colour
        self.output_dir = output_dir
        self.font_dir = font_dir
        self.text_corpus = load_dict(text_corpus_path)
        self.date_corpus = load_date_dict(date_corpus_path)
        self.fonts = load_font(self.font_dir)
        self.noise_types  = load_noise_type()
        self.corpus = [self.text_corpus, self.date_corpus]
        self.font_size_min = font_size_min
        self.font_size_max = font_size_max
        
        
    def draw_text(self, draw, x, y , text, file, draw_rectangle):
    
        #print(os.path.join(self.font_dir,self.fonts[random.randrange(0,len(self.fonts))]))
        font=ImageFont.truetype(os.path.join(self.font_dir,self.fonts[random.randrange(0,len(self.fonts))]), random.randrange(self.font_size_min,self.font_size_max))

        (w,h) = textsize(text=text, font=font)
        if x+w > (self.img_size[0]-20) or y+h > (self.img_size[1]-20):
            return draw, (w,h), False
        draw.text((x, y), text, fill="black",font=font)
        file.write("{},{},{},{},{},{},{},{},{}\n".format(x,y,x+w,y,x+w,y+h,x,y+h,"text"))

        #(w,h) = draw.textsize(text)
        if draw_rectangle:
            draw.rectangle([x-1,y+2,x+w,y+h],outline="black")

        return draw, (w,h), True
        
    def generateImages(self, range_start, range_end, draw_rectangle=True):
        
        for i in tqdm(range(range_start,range_end+1)):
            
            file = open(os.path.join(self.output_dir, "img_"+str(i)+".txt"),'w')
            im = Image.new('RGB', self.img_size, self.bg_colour)
            ###################################small work around as noise code uses cv2 not PIL########################################################
            im.save("temp.jpg")
            cv2.imwrite("temp.png", noisy(self.noise_types[random.randrange(0,len(self.noise_types))],cv2.imread("temp.jpg")))
            ############################################################################################################################################
            im = Image.open("temp.png")
            draw = ImageDraw.Draw(im)
            start_x = random.randrange(5,25)
            start_y = random.randrange(5,25)
            y_list = []
            y_list.append(start_y)
            line_number_end = random.randrange(2,25)
            line_number =1

            while True:

                corpus_selection = self.corpus[random.randrange(0,len(self.corpus))]
                draw, shape, flag= self.draw_text(draw, start_x,start_y,corpus_selection[random.randrange(0,len(corpus_selection))], file, draw_rectangle)

                start_x = start_x+shape[0]+10
                y_list.append(start_y+shape[1])
                if start_x > 1280 or flag==False:
                    break

            while True:
                if line_number < line_number_end:
                    start_x = random.randrange(5,25)
                    start_y = max(y_list)+10
                    y_list = []
                    y_list.append(start_y)
                    
                    while True:
                        corpus_selection = self.corpus[random.randrange(0,len(self.corpus))]
                        draw, shape, flag= self.draw_text(draw, start_x,start_y,corpus_selection[random.randrange(0,len(corpus_selection))],file,draw_rectangle)
                        start_x = start_x+shape[0]+10
                        y_list.append(start_y+shape[1])
                        if start_x > 1260 or flag==False:
                            break

                    if start_y+10>700:
                        line_number += 1
                        break
                    line_number += 1
                else:
                    break

            im.save(os.path.join(self.output_dir, "img_"+str(i)+".jpg"))
            im.close()
            os.remove("temp.jpg")
            os.remove("temp.png")
            file.close()
    