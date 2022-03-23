# Cells Detection (*The aim of the scripts is more to measure the cell sizes, which is a significant upgrade from cell detection only, so I would suggest changing the title to something that contains measure/measuments/size - maybe diatoMeasure?*)

## What is this?
This repository provides an automatic cell detector algorithm to detect and count cell numbers in 2D microscopy images from Diatoms Cells. (*Here you should mention that it detects the cells and measures their size. Also in this very beginning part I would already mention that there are 2 different methods called 'elipsis' and 'label' that have independent scripts, and that one of these two method can be run in batch*)

(*I think you should give a brief overview of the contents of the repository, something like this:
Description of files included:
The folder SCRIPTS contains the python scripts that run the cell detection and measurement.
The folder PROPERTIES contains ......
requirements.txt - text file listing all required libaries and version.
and so on)*

( *Also here I think it would be good to say a few words on how to use these scripts in very simple words, something like this:
The general strategy of both methods is to first segment the cells by ......
Next the elipsis method measures the cells by....
The label method measures the cells by....
input: an image of cells, we use microscope images in .tiff format.
output: 

Also mention that the script was developed to detect and measure ellipsoidal cells.*)

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

**ELIPSIS**

*Require arguments*

*Stage 1*

You maybe input the path of the picture.

[![path-elipsis.png](https://i.postimg.cc/4NpjfRCy/path-elipsis.png)](https://postimg.cc/4mNWPMxR)

*Stage 2*

After we use the rgb2gray function converts RGB images to grayscale.You have values between 0 and 1,black and white, foreground and background.
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

PENDIENT

**BATCH**

PENDIENT

## Methods:

It is the script logical process.

[Elipsis and Label](https://github.com/Nahuel88Ar/Cells-Detection-/blob/a3657b42ebfb9e00c2f75c595bfc3d197ba82801/elipsis%20and%20label%20script%20logical%20process.pdf)






