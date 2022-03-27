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

The general strategy of both methods is to first segments the cells by intensity of the pixels.

Next the elipsis method measures the cells by simple scale(black and white), background and foreground.It use on the connectivity of the pixels to each other. As long as neighboring pixels share the same value if intensity, they will be labeled as a single region, a region can be a cell.
After I got information of each region as: area, perimeter, major axis lengths,minor axis length, etc.

Next the label method measures the cells by Thresholding, also it use a simple scale(black and white) and replace each pixel in an image with a black pixel if the
image intensity is less than a value or a white pixel if the image intensity is greater than that value.Returns a single intensity threshold that separate pixels into two classes,foreground and background.Use the variance generated in the histogram of intensity of each pixel in the image.

**Input:** on image of cells, we use microscope images in .tiff format.

**Output:** Dataframe save in a excel file and binary image with the detected cells.

The scripts was developed to detect and measure ellipsoidal cells.

**Please star this repository if you like it :)**

## Installation:
This algorithm has been implemented using **Python 3.8.8 bit 64**. To install the necessary packages for this framework run:
```
pip install -r requirements.txt
```
If you are using conda first install pip by: ```conda install pip```


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

**Here is a tutorial to set up your Automatic Cell Detector for Windows**: [Tutorial](https://github.com/Nahuel88Ar/Cells-Detection-/blob/72874b90ea4922d54d36b3e1101acefd4447c4c6/Python%20tutorial%20for%20Windows.pdf) 

(*I am not exactly sure what the rules are, but if you want to use this tutorial in you own repository I think you should credti the makers*)

**ELIPSIS**
(*I think you should give a bit more explanation, let's go over it next week*)

*Require arguments*

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

**LABEL**

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


**BATCH**

PENDIENT

## Methods:

It is the script logical process.

[Elipsis and Label](https://github.com/Nahuel88Ar/Cells-Detection-/blob/a3657b42ebfb9e00c2f75c595bfc3d197ba82801/elipsis%20and%20label%20script%20logical%20process.pdf)






