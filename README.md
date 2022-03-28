# Cells diatoMeasure 

## What is this?
This repository provides automatic algorithms to detect and measure the size of each cell in 2D microscopy images from diatoms cells. There are 2 independent scripts called 'elipsis' and 'label'. Also LABEL can be run in batch.  

It contains 4 files and 4 folders.

The files are:

**Python Tutorial for Windows** Tutorial describing how to install the software and the correct packages to use the scripts.

**README:** General description of all the project.

**Elipsis and Label Logical Process:** Description of the theorical and logical base of the project.

**Requirements:** All the libraries you need to install to run the scripts.

The folders are:

**IMAGES:** All the images of my proyect since the first stage until last stage in each script.

**PROPERTIES:** Contains a description of the properties that can be measured using the scripts.

**SCRIPTS:** Contains the python scripts that run the cell detection and measurement.

**REQUIREMENTS:** Text file listing all required libraries and versions.

## Elipsis

The general strategy of both methods is to first segment the cells based on pixel intensities.

The elipsis method first converts the RGB microscope image to a grayscale image in which all pixels have a greyscale value between 0 and 1. Then the image is binarized (all pixels either 0 or 1) to assign each pixel to be either background or foreground (cells). You have to set a cutoff intensity (for example 0.5) and all pixel with lower intensities will be assigned as background and converted to pixel intensity 0, and all pixels with higher intensities will be assigned as foreground and get pixel intensity 1.
Next, the binarized imaged will be probed by a 3by3 pixels square (np.array) and four morphological operations, dialation, erosion, filling and closing will be applied. Each square will have a boolean value and the function will evaluate this value, for example you have 0 inside of the region with the function filling, erosion and closing you convert this value in foreground. 
For dialation, the maximum pixel intensity within the square will be determined and the center pixel in the square will be assigned to have that maximum pixel intensity. Erosion does a similar operation but considering the minimum intensity. 
The output is  a binarized image with the segmented cells having pixel intensity 1 but now the holes are filled and edges are more smooth. 
Adjust the cutoff intensity (usually 0.4-0.7) to the intensity that creates the best segmentation of cells without holes.

Next, the cleaned binary image is used to detect regions that are a cell and assigns a label to each of these regions. It uses the connectivity of the pixels to determine regions, as long as neighboring pixels share the same value if intensity, they will be labeled as a single region, a region can be a cell. 
Then you can analyze parameters of the detected regions: area, perimeter, major axis lengths, minor axis length, etc. A loop will run along each region and measure the indicated paremeters. The output are an image with the minor axis length and major axis length plotted onto the detected regions and a dataframe summarizing all measurements. Finally, you can download this Dataframe in a excel file(.xls).


This is a explication on what is a elipsis and your coordenates:
[![elipsis-theory.png](https://i.postimg.cc/7Ynxcbtw/elipsis-theory.png)](https://postimg.cc/sv1dGfRN)


## Usage:

To run the cell detector, the user can easily input the following codes in the terminal:ELIPSIS, LABEL OR BATCH.

For ELIPSIS and LABEL methods you can use the next picture.

[![6.png](https://i.postimg.cc/xTzF6yxm/6.png)](https://postimg.cc/crdmHYN1)

For BATCH Method you can use all this pictures to generate a folder and process in batch way.

[![1.png](https://i.postimg.cc/Y24XSzwP/1.png)](https://postimg.cc/XXbKHFqK)
[![2.png](https://i.postimg.cc/x1jMX9zd/2.png)](https://postimg.cc/Mv4v42tk)
[![3.png](https://i.postimg.cc/k5b44Hf4/3.png)](https://postimg.cc/t19yvB0Q)
[![4.png](https://i.postimg.cc/CLxxD5m9/4.png)](https://postimg.cc/K4CbhGX5)
[![5.png](https://i.postimg.cc/1tS9z38C/5.png)](https://postimg.cc/VS7yG1Bn)
[![6.png](https://i.postimg.cc/xTzF6yxm/6.png)](https://postimg.cc/crdmHYN1)
[![7.png](https://i.postimg.cc/TY1T1SP6/7.png)](https://postimg.cc/XXRRDsFH)

**Here is a very helpful tutorial provide by HelmholtzAI-Consultants-Munich/Automatic-Cell-Counter to set up your Automatic Cell Detector for Windows**: [Tutorial](https://github.com/Nahuel88Ar/Cells-Detection-/blob/72874b90ea4922d54d36b3e1101acefd4447c4c6/Python%20tutorial%20for%20Windows.pdf) 

**ELIPSIS**

*Stage 1*

You may input the path of the image.

[![path-elipsis.png](https://i.postimg.cc/4NpjfRCy/path-elipsis.png)](https://postimg.cc/4mNWPMxR)

*Stage 2*

After we use the rgb2gray function converts RGB images to grayscale. You have values between 0 and 1,black and white, foreground and background.
You can input any value between 0 and 1.

We get this result for a value <0.5.

[![grayscale-elipsis.jpg](https://i.postimg.cc/L4cnd2TW/grayscale-elipsis.jpg)](https://postimg.cc/JtQ1ZwS3)

Still we have holes and irregular shapes in the detection, then we need to generate 2 functions for dilatation and erosion and use two more tools( closing and opening).

Dilatation to close the pixels,closing to fill the holes inside,erosion to restore the original shape of the objects and opening to remove the noise on the image.

[![grayscale-elipsis-2.jpg](https://i.postimg.cc/Nj4MrTch/grayscale-elipsis-2.jpg)](https://postimg.cc/MnnxCnHt)

**Example output**:

You get a detection and dataframe with values of all measures of each cell.

[![label-elipsis.png](https://i.postimg.cc/pXC8SCnq/label-elipsis.png)](https://postimg.cc/F7f7djpL)

[![detection-elipsis.jpg](https://i.postimg.cc/QM0pWbjF/detection-elipsis.jpg)](https://postimg.cc/Y4L45QG7)

[![dataframe.png](https://i.postimg.cc/HsJDvYnx/dataframe.png)](https://postimg.cc/ykzbkzF4)

[![dataframe2.png](https://i.postimg.cc/sxQ6m2mC/dataframe2.png)](https://postimg.cc/gLpHkm1g)


## Label

The general strategy of both methods is to first segment the cells based on pixel intensities.
For the method 'label' the original RGB imaged is converted to a grey scale image where only the red channel is considered.
Next, the label method detects the cells by thresholding that separate pixels into two classes,foreground and background. The tresholding is done automatically according to Otsu's method. This method uses the intesity histogram to determine the intensity treshold that minimizes intra-class intensity variance. Pixels that are below the treshold will be assigned to be background, and pixels above the treshold will be assigned foreground. 
[![label-script-logical.png](https://i.postimg.cc/SNP2rkVy/label-script-logical.png)](https://postimg.cc/7fgZPvpc)

The resulting binarized images are filtered to remove objects/cells that are too small to be a cell and fill holes of a certain size. The values for the filtering can be filled in (we usually use the value of 7000 for both).
Next the segmented and cleaned image is used to assign labels to regions that correspond to cells.
Then a loop will measure the properties of each label and create an image and dataframe.
The produced image contains shows the identified regions, you can now click wrongly assigned labels to remove regions that are not cells.
Based on the labels that are left, you can determine the best cutoff values to create a subset of regions that only contains cells.
Then a new dataframe is produced that contains only the correct labels and you can dowload the dataframe in Excel file(.xls).

*Require arguments*

*Stage 1*

You may input the path of the image.

[![path-elipsis.png](https://i.postimg.cc/4NpjfRCy/path-elipsis.png)](https://postimg.cc/4mNWPMxR)

*Stage 2*

After you open this image wuth the path, the script generate am array to contain the intensity in each pixel with 3 different channel(RED, GREEN, BLUE), you remember any image have a RGB scale, we divide it to work in an unique colour, in this case we use RED.

After we use a tool of the Scilit Image library called Thresholding, we create a mask and the script use mathematical morphology operations to remove snall objects and holes in each cell, you can see more on this topic in the next link:

[Mathematical morphology](https://en.wikipedia.org/wiki/Mathematical_morphology)

**Example output**:

You get a detection and dataframe with values of all measures of each cell.

[![label-output.png](https://i.postimg.cc/Gtf20Xvs/label-output.png)](https://postimg.cc/2L4mhFcz)

You can remove a object(not cell or unclear cell) with a click in the picture but not in the Dataframe.If you want to remove in Dataframe you need filter for a value, as in the example Minor Axis Length, you can print only all the cells major at this value.

[![Removed-cell.jpg](https://i.postimg.cc/fkQnv82j/Removed-cell.jpg)](https://postimg.cc/wR2GqQd7)
[![click2.png](https://i.postimg.cc/nVjX0MSC/click2.png)](https://postimg.cc/RqmC0CBB)

Filter in the dataframe and download the new Dataframe in Excel:

[![filter-dataframe.png](https://i.postimg.cc/4xB4JT2D/filter-dataframe.png)](https://postimg.cc/ZWvzcXSH)

[![excel-label.png](https://i.postimg.cc/prMZxBxy/excel-label.png)](https://postimg.cc/Hc359XrC)

**BATCH**

This method is Label but run as batch, only have two difference with the Label script, first you open a folder with the Glob2 Library and you need use other loop to process all the images in the same time.

You may input the path of the folder.

[![path-batch.png](https://i.postimg.cc/RFvksPBv/path-batch.png)](https://postimg.cc/v1S2DtTK)

**Example output**:

You get a dataframe with of all measures of each cell.

[![dataframe-batch.png](https://i.postimg.cc/TYHWTS7H/dataframe-batch.png)](https://postimg.cc/6ynQ0HNd)


**Input:** on image of cells, we use microscope images in .tiff format.

**Output:** Dataframe save in a excel file and binary image with the detected cells.

The scripts was developed to detect and measure ellipsoidal cells.

**Please star this repository if you like it :)**

## Installation:
This algorithm has been implemented using **Python 3.8.8 bit 64**. To install the necessary packages for this framework download the requirements.txt file and run:
```
pip install -r requirements.txt
```
If you are using conda first install pip by: ```conda install pip```


## Methods:

It is the script logical process.

[Elipsis and Label](https://github.com/Nahuel88Ar/Cells-Detection-/blob/a3657b42ebfb9e00c2f75c595bfc3d197ba82801/elipsis%20and%20label%20script%20logical%20process.pdf)






