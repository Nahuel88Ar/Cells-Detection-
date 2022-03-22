# Cells Detection

## What is this?
This repository provides an automatic cell counter algorithm to count cell numbers in 2D microscopy images from Diatoms Cells. 


**Please star this repository if you like it :)**

## Installation:
This algorithm has been implemented using **Python 3.8.8 bit 64**. To install the necessary packages for this framework run:
```
pip install -r requirements.txt
```
If you are using conda first install pip by: ```conda install pip```


## Usage:

To run the cell counter, the user can easily input the following codes in the terminal:ELIPSIS, LABEL OR BATCH.

For ELIPSIS and LABEL methods you can use the next picture.

![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/6.tif)

For BATCH Method you can use all this pictures to generate a folder and process in batch way.

![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/1.tif)
![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/2.tif)
![image](https://github.com//Nahuel88Ar/Cells-Detection-/example_data/3.tif)
![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/4.tif)
![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/5.tif)
![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/6.tif)
![image](https://github.com/Nahuel88Ar/Cells-Detection-/example_data/7.tif)

For all the methods you check the requirements on the libraries here:
[Libraries](https://github.com/Nahuel88Ar/Cells-Detection-/requirements.txt)


**ELIPSIS**

*Require arguments*

*Stage 1*

You maybe input the path of the picture.

![image](https://github.com/Nahuel88Ar/Cells-Detection-/IMAGES/path_elipsis.png)

*Stage 2*

After we use the rgb2gray function converts RGB images to grayscale.You have values between 0 and 1,black and white, foreground and background.
You can input any value between 0 and 1.

We get this result for a value <0.5.

![image](https://github.com/Nahuel88Ar/Cells-Detection-/IMAGES/grayscale_elipsis.jpg)

Still we have holes and irregular shapes in the detection, then we need to generate 2 functions for dilatation and erosion and use two more tools( closing and opening).

Dilatation to close the pixels,closing to fill the holes inside,erosion to restore the original shape of the objects and opening to remove the noise on the image.

![image](https://github.com/Nahuel88Ar/Cells-Detection-/IMAGES/grayscale_elipsis_2.jpg)

*Stage 3*

**LABEL**

**BATCH**


**Here is a tutorial to set up your Automatic Cell Counter for Windows**: [Tutorial](https://github.com/HelmholtzAI-Consultants-Munich/Automatic-Cell-Counter/blob/master/Python%20tutorial%20for%20Windows.pdf)

**Example output**:

## Data:

### Example images:

## Methods:






