# PyOCR

## About
This is a python based optical character recognition tool (OCR) with GUI.
The GUI is supported with python tkinter. The OCR part is handled by
using [py-tesseract](https://pypi.org/project/pytesseract/) which is a
a wrapper for 
[Google’s Tesseract-OCR Engine](https://github.com/tesseract-ocr/tesseract). 
This tool also provide a manual correction 
(provided by [python-datamuse](https://pypi.org/project/python-datamuse/)) 
using homophones of target words. 

## Installing PyOCR
Once you've downloaded all files. Install following dependencies:
([Tesseract](https://github.com/tesseract-ocr/tesseract), 
[Pillow](https://pillow.readthedocs.io/en/stable/), 
[Numpy](https://numpy.org),
[py-tesseract](https://pypi.org/project/pytesseract/), 
[python-datamuse](https://pypi.org/project/python-datamuse/))

An example using Homebrew, Anaconda, Pip to install aboving dependencies 
contains following command lines:
* brew install tesseract
* conda install numpy pillow
* pip install pytesseract python-datamuse

## Running PyOCR
In your console, run below commend line:
* python3 PyOCR.py

to launch the GUI. Then you can select the image to OCR with. And you
can also get homophones of a word as its candidates.

