#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:48:51 2020

@author: chujiechen
"""

from datamuse import datamuse

class Word2Homo:
    def __init__(self, word):
        self.word = word
        self.api = datamuse.Datamuse()
    def getHomophones(self):
        homos_info = self.api.words(sl=self.word, max=10)
        homos = [info['word'] for info in homos_info]
        return homos
        
    
if __name__ == "__main__":
    w2h = Word2Homo("brake")
    print(w2h.getHomophones())