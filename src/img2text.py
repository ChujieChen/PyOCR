#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:50:27 2020

@author: chujiechen
"""

import os
from PIL import Image,ImageTk
import pytesseract

class Img2Text:
    def __init__(self, img):
        self.img = img
        self.text =  pytesseract.image_to_string(img)
    def get_text(self):
        return self.text