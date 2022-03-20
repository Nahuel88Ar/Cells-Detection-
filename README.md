# Automatic Cell Counter
What is this?
This repository provides an automatic cell counter algorithm to count cell numbers in 2D microscopy images from Diatoms.

Please star this repository if you like it :)

Installation:
This algorithm has been implemented using Python 3.8.8 64 bit. To install the necessary packages for this framework run:

pip install -r requirements.txt
If you are using conda first install pip by: conda install pip

Usage:
To run the cell counter, the user can easily input the following code in the terminal.

Require arguments:

-image: The path of the input image or the path of the directory.
python viewer.py --image example_data/8.tif
or

python viewer.py --image example_data/

Here is a tutorial to set up your Automatic Cell Counter for Windows: https://github.com/HelmholtzAI-Consultants-Munich/Automatic-Cell-Counter/blob/master/Python%20tutorial%20for%20Windows.pdf

Example output:

The user interface will be built based on every input image for manual correction. Inside each image, red dots are used to denote the centers of the detected cells. We also used green dots and red bounding boxes to guide users to pay more attention to those easy-to-make-mistake areas: green dots (detected cells are quite small, perhaps one cell is divided to several parts) and red bounding box (high density areas, perhaps two cells are merged). The user may add dots or delete dots manually based on the automatically detected results.

After manual correction, press the 'd' (denotes Done) key on the keyboard to print the updated cell numbers on the terminal and close the current window. When all images are corrected, an excel file named result will be generated which contains both automatically detected cell numbers and corrected cell numbers.

