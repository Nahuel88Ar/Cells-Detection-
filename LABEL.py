#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[5]:


img = cv2.imread('W:\\LAB\\Nahuel Ramos\\Size reduction data\\IMAGES\\Long term - slow\\D3S\\211012_D3S\\211012_D3S_299.tif')


# In[6]:


array = np.array(img)

red = array[:,:, 0]
green = array[:,:, 1]
blue = array[:,:, 2]

threshold = filters.threshold_otsu(red)
mask =  red<= threshold
#Replace each pixel in an image with a black pixel if the image intensity is less than some fixed constant T-curvature or a white pixel if the image intensity is greater than that constant.
#Input minimum size. The smallest allowable object size.
mask = morphology.remove_small_objects(mask, 7000)
#Input areas threshold.The maximum area, in pixels, of a contiguous hole that will be filled.
mask = morphology.remove_small_holes(mask, 7000)
labels = measure.label(mask)
#Two pixels are connected when they are neighbors and have the same value.
fig = px.imshow(red, binary_string=True)


# In[7]:


fig.update_traces(hoverinfo='skip') # hover is only for label info

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
        mean = np.mean(array)
        print(array)
    fig.add_trace(go.Scatter(x=x, y=y, name=label_i,mode='lines', fill='toself', showlegend=True,hovertemplate=hoverinfo,hoveron='points+fills'))
plotly.io.show(fig,width=10000,height=10000)


# In[ ]:




