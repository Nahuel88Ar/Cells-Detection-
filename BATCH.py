#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Glob
import glob

#Numpy
import numpy as np

#Pandas
import pandas as pd

#Cv2
import cv2

#Seaborn
import seaborn as sns

#Matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Scikit-Image
from skimage.measure import label, regionprops, regionprops_table
from skimage.transform import rotate
from skimage import data, filters, measure, morphology
from skimage.io import imread
import skimage.color
import skimage.io
from skimage import io
from skimage.util import img_as_ubyte
from skimage.segmentation import clear_border

#Plotly
import plotly
import plotly.express as px
import plotly.graph_objects as go


# In[25]:


file = 'W:\\LAB\\Nahuel Ramos\\Size reduction data\\IMAGES\\Long term - slow\\SS\\210404_SS\\*.tif'


# In[26]:


glob.glob(file)


# In[ ]:





# In[27]:


images = [cv2.imread(image) for image in glob.glob(file)]

for i in range(0,len(images)):
    array = np.array(images[i])
    red = array[:,:, 0]
    fig = plt.figure(figsize = (10,10))

    threshold = filters.threshold_otsu(red)
    mask =  red<= threshold

    mask = morphology.remove_small_objects(mask, 7000)
    mask = morphology.remove_small_holes(mask, 7000)
    labels = measure.label(mask)
        
    fig = plt.imshow(images[i])
        
    props = measure.regionprops(labels,red)
    properties = ['minor_axis_length']
        
    for index in range(0, labels.max()):
        label_i = props[index].label
        contour = measure.find_contours(labels == label_i,0.5)[0]
        y, x = contour.T
        hoverinfo = ''
        for prop_name in properties:
            hoverinfo += f'<b>{prop_name}: {getattr(props[index], prop_name):.2f}</b><br>'
            array = np.array(getattr(props[index], prop_name))
            print(array)


# In[ ]:




