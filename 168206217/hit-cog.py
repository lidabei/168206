# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:37:21 2018

@author: Administrator
"""
import os
start = 'hit'
end = 'cog'

adiction = ('hot','dot','dog','lot','log')

def find_path(start,end,paths):
    if start == end:
        return "start=end"
    else:
        visited = []
        visited.append(start)
        for word in visited:
             for i in range(len(word)):
                 for j in range(ord('a'),ord('z')+1):
                    word = word[:i] + chr(j) + word[i+1:]
                    print(word)
                    if word in adiction:
                        visited.append(word)
           
find_path(start,end,adiction)
os.system("pause")
        