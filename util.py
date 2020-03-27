import os
import cv2
import numpy as np
from PIL import Image
import random



def load_noise_type():
    """
        Read the dictionnary file and returns all words in it.
    """
    noise_types = ["na", "gauss", "s&p", "poisson", "speckle"]
    
    return noise_types
  
def load_font(font_dir):
    """
        Read the dictionnary file and returns all words in it.
    """
    
    return os.listdir(font_dir)

def load_dict(corpus_path):
    """
        Read the dictionnary file and returns all words in it.
    """
    lang_dict = []
    with open(corpus_path, 'r', encoding="utf8", errors='ignore') as d:
        lang_dict = [l for l in d.read().splitlines() if len(l) > 0]
    return lang_dict

def load_date_dict(corpus_path):
    """
        Read the dictionnary file and returns all words in it.
    """
    lang_dict = []
    with open(corpus_path, 'r', encoding="utf8", errors='ignore') as d:
        lang_dict = [l for l in d.read().splitlines() if len(l) > 0]
    return lang_dict

def textsize(text, font=None, *args, **kwargs):
    """Get the size of a given string, in pixels."""

    return font.getsize(text)

def noisy(noise_typ,image):
    
    if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
    
    elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.004
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
    
    elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
    
    elif noise_typ =="speckle":
      lower_black = np.array([255,255,255], dtype = "uint16")
      upper_black = np.array([255,255,255], dtype = "uint16")
      black_mask = cv2.inRange(image, lower_black, upper_black)
      image[black_mask != 0] = [160,160,160]
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
    
    else:
      return image  

