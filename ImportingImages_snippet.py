#####code snippet for importing images - co written by Carmen and Johnathan for python3


#needed modules
import pims
import numpy as np
from skimage import filters
import matplotlib  as mpl 
import matplotlib.pyplot as plt

#Call this if you are trying to import a bunch of individuals images
def ImportImg(directory, prefix, preprocess_func): # you can also process the images as you load them here, say if you know you want to crop them or sharpen them
    frames = pims.ImageSequence(os.path.join(directory, prefix + '*.tif'), process_func=preprocess_func)
    return frames



#Call this if you are trying to import a multi image stack (tif)
def ImportStack(directory, prefix):
    frames = pims.TiffStack(os.path.join(directory, prefix))
    return frames


def crop(img):
    """
    Crop the image to select the region of interest
    """   
    x_min = 474
    x_max = 1024
    y_min = 208
    y_max = 328
    return img[y_min:y_max,x_min:x_max]

def preprocess_sharpen(img):
    
    img = crop(img)
    img = filters.unsharp_mask(img, radius = 2, amount = 5)
    img *= 255.0/img.max()
    return img
