#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:48:51 2020

@author: chujiechen
"""
import numpy as np 
from datamuse import datamuse

class Word2Homo:
    def __init__(self, word):
        self.word = word
        self.api = datamuse.Datamuse()
    def getCandidates(self):
        # homographs
        homographs_info = self.api.words(sp=self.word, max=5)
        homographs = [info['word'] for info in homographs_info]
        # homophones
        homophones_info = self.api.words(sl=self.word, max=5)
        homophones = [info['word'] for info in homophones_info]
        # concatenate
        homos = homographs + homophones
        homos = set(homos)
        homos.remove(self.word)
        return homos
        
        
    
if __name__ == "__main__":
    # print("what")
    w2h = Word2Homo("brake")
    print(w2h.getCandidates())
