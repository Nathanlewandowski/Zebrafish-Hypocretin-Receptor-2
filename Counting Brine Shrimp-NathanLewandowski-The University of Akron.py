# -*- coding: utf-8 -*-

"""
Created on Sun Apr 30 22:21:32 2023
@author: nathan
"""

import numpy
import matplotlib.pyplot as plt
import skimage 
from skimage import io
import os
from skimage.measure import label, regionprops
import pandas as pd


#Directory where pictures are located 
os.chdir(r"C:\Users\natha\OneDrive - The University of Akron\Zebrafish Feeding Photos")
camera = skimage.io.imread("f1d1 0min.JPG") #Picture name being analyzed 
plt.figure(1)
io.imshow(camera) 

Isolate=numpy.copy(camera)
brine=skimage.color.rgb2gray(Isolate) #creates grayscale image
plt.figure(2)
plt.hist(brine.ravel(), bins=256, log=True) #creates histogram of values, 0:black, 1:white 

#Threshold to identify objects that are brine shrimp
thresh = .065
binary = brine > thresh

#Labels the objects in the image
label_image = label(binary)
plt.figure(3)
io.imshow(label_image)
props= regionprops(label_image)

#Calculates average size of objects counted 
output = pd.DataFrame(columns=['Size'])
for i in range(0,len(props)):
    
    if props[i]['area']>5:
      
       brine_size = props[i]['area']/4000
       output.loc[i]=(brine_size)
        
#Displays object count and size
print("")
print ('Total Number of Brine Shrimp= ',len(output.index))  
print ("Average Size (mm) =",output['Size'].mean())
