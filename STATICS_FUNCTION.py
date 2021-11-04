

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:26:24 2021

@author: get-a
"""

import numpy as np               
from PIL import ImageStat

class STATICS_FUNCTION:
    
    # https://pillow.readthedocs.io/en/stable/reference/ImageStat.html
    
    #Returnning the MAX value of the grayscale image .
    def Max_value(self,img): 
        min_max = ImageStat.Stat(img).extrema 
        max_value=min_max[0][1]
        return max_value
        
     #Returnning the MIN value of the grayscale image .
    def Min_value(self,img): 
        min_max = ImageStat.Stat(img).extrema 
        min_value=min_max[0][0]
        return min_value
 
    
    
     #Returnning the MEAN of the pixels level in the grayscale image. 
    def Mean_value(self,img): 
        Mean_value = ImageStat.Stat(img).mean[0] 
        return Mean_value

  
    #Returnning the MEDIAN  pixels level in the grayscale image.
    def Median_value(self,img): 
        Median_value = ImageStat.Stat(img).median[0]
        return Median_value
    
    
    
    ### https://stackoverflow.com/questions/2374640/how-do-i-calculate-percentiles-with-python-numpy
    #Returnning the N'th percentile of the image .
    def percentile_value(self,img,p):
        
        # converting PIL image to NumPy array
        converttonumpy = np.asarray(img) 
        # Calculating the  N'th percentile of the image
        percentile= np.percentile(converttonumpy,p) 
        return percentile