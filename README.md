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

## Functionality
* Import one image from your computer at a time and OCR the imported image
* Select a part of the image and do OCR only on that region
* Can edit/copy/paste the result
* Provide homographs and homophones as other possible words

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
In your console, at directory `/PyOCR/pyocr/` run below commend line:
* **./PyOCR.py**

Or
* **python3 PyOCR.py**

to launch the GUI. Then you can select the image to OCR with. And you
can also get a list of homographs and homophones of a word as its candidates.

## Using PyOCR
Once you launch the GUI, you will see an interface like this:

![main_interface](https://github.com/ChujieChen/PyOCR/blob/master/docs/main_interface.png)

Click the `Browse` then you can select the image you want to do OCR with. For example, below there, a scan of a business card is imported. And the OCR results are shown in the middle.
![all_business](https://github.com/ChujieChen/PyOCR/blob/master/docs/all_business.png)

If you only need the information about this Dan Porter, you can drag a rectangular box on this image and click `Update OCR`, and the tool will only do OCR on text inside that box.
![some_business](https://github.com/ChujieChen/PyOCR/blob/master/docs/some_business.png)

Here is an example showing the result with a photo and the fuzzy search on a word `fast`.
![photo](https://github.com/ChujieChen/PyOCR/blob/master/docs/photo.png)

Another example with a screenshot of SMS.
![simtxt](https://github.com/ChujieChen/PyOCR/blob/master/docs/simtxt.png)
