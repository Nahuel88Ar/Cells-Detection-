# Cells diatoMeasure 

## What is this?
This repository provides automatic algorithms to detect and measures the size of each cell in 2D microscopy images from Diatoms Cells.There is 2 different independent scripts called 'elipsis' and 'label'. Also LABEL can be run in batch.  

It contain 4 files and 4 folders.

The files are:

**Python Tutorial for Windows** Tutorial where can see as install the software and the correct packages to use the scripts.

**README:** General description of all the proyect.

**Elipsis and Label Logical Process:** Description of the theorical and logical base of the proyect.

**Requirements:** All the libraries you need to install to run the scripts.

The folders are:

**IMAGES:** All the images of my proyect since the first stage until last stage in each script.

**PROPERTIES:** It contains all the measures you can get with those scripts.

**SCRIPTS:** It contains the python scripts that run the cell detection and measurement.

**REQUIREMENTS:** Text file listing all required libraries and version.

## Elipsis

The general strategy of both methods is to first segments the cells by intensity of the pixels.

Next the elipsis method segments the cells based on the intensity of the pixels. You set a cutoff intensity (for example 0.5) and all pixel with lower intensities will be assigned as background and converted to pixel intensity 0, and all pixels with higher intensities will be assigned as foreground and get pixel intensity 1.
Next, the binarized imaged will be probed by a square and in each square contain boolean values(0 or 1), the function evaluate this value and for example you have o inside of the region with the function filling, erosion and closing you convert this value  in foreground. Now the output is again a binarized image with the segmented cells having pixel intensity 1 but now the holes are filled. Adjust the cutoff intensity (usually 0.4-0.7) to the intensity that creates the best segmentation of cells without holes.
Next, the binary image is used to detect regions that are a cell and gives a label to each of these regions. It use on the connectivity of the pixels to each other. As long as neighboring pixels share the same value if intensity, they will be labeled as a single region, a region can be a cell. 
After I got information of each region as: area, perimeter, major axis lengths,minor axis length, etc.

Next, one time we got a clear detection with properties we need we can generate a plot and dataframe.In the plot draws the measured parameters on top of the image.

It is a explication on what is a elipsis and your coordenates:

[![elipsis-theory.png](https://i.postimg.cc/7Ynxcbtw/elipsis-theory.png)](https://postimg.cc/sv1dGfRN)

Next, it run a loop for each properties in a region. We plot the minor and major length axis. In the last part you write the properties that you wish to get in your Dataframe. Finally, you can download this Dataframe in a excel file(.xls).

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

[![label-elipsis.png](https://i.postimg.cc/YSPt1zDP/label-elipsis.png)](https://postimg.cc/zLnmNKrw)

[![detection-elipsis.png](https://i.postimg.cc/rw8ycmtf/detection-elipsis.png)](https://postimg.cc/JG2C5RxX)

[![dataframe.png](https://i.postimg.cc/Wb7j9vfg/dataframe.png)](https://postimg.cc/sv1tXtzg)

[![dataframe2.png](https://i.postimg.cc/DzSTybfP/dataframe2.png)](https://postimg.cc/NyvVdFHK)

## Label

The general strategy of both methods is to first segments the cells by intensity of the pixels.
First the original RGB imaged is converted to a grey scale image where only the red channel is considered.
Next the label method detects the cells by Thresholding, also it use a simple scale(black and white) and replace each pixel in an image with a black pixel if the
image intensity is less than a value or a white pixel if the image intensity is greater than that value. Returns a single intensity threshold that separate pixels into two classes,foreground and background. Use the variance generated in the histogram of intensity of each pixel in the image.
The treshold is determined automatically by the otsu method, as follows:

[![label-script-logical.png](https://i.postimg.cc/SNP2rkVy/label-script-logical.png)](https://postimg.cc/7fgZPvpc)

Next, the tresholded images are filtered to remove objects/cells that are too small to be a cell and holes of a certain size are filled. The values for the filtering can be filled in (we usually use the value of 7000 for both).
Next the segmented and cleaned image is used to make labels that correspond to the cells.
Then a loop will measure the properties of each label and create a plot and dataframe.
In the plotted image you can now click wrongly assigned labels to remove objects that are not cells.
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

[![LABEL-OUTPUT.jpg](https://i.postimg.cc/3N559Y36/LABEL-OUTPUT.jpg)](https://postimg.cc/R6RDZr6Q)

You can remove a object(not cell or unclear cell) with a click in the picture but not in the Dataframe.If you want to remove in Dataframe you need filter for a value, as in the example Minor Axis Length, you can print only all the cells major at this value.

[![Removed-cell.jpg](https://i.postimg.cc/fkQnv82j/Removed-cell.jpg)](https://postimg.cc/wR2GqQd7)
[![click2.png](https://i.postimg.cc/nVjX0MSC/click2.png)](https://postimg.cc/RqmC0CBB)

Filter in the dataframe and download the new Dataframe in Excel:

[![filter-dataframe.png](https://i.postimg.cc/4xB4JT2D/filter-dataframe.png)](https://postimg.cc/ZWvzcXSH)


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






