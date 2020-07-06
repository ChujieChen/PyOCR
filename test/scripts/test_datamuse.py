# -*- coding: utf-8 -*-

"""
Created on Fri Jul  3 11:01:06 2020

@author: chujiechen
"""

from datamuse import datamuse
api = datamuse.Datamuse()
for w in ["brake", "cell", "cent", "for"]:
    print("Original: \n" + w)
    words_info = api.words(sl=w, max=5)
    words = [info['word'] for info in words_info]
    print("Homophones: ")
    print(words)
