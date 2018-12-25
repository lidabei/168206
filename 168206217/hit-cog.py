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
                    newword = word[:i] + chr(j) + word[i+1:]
                    if newword in paths and newword not in visited:
                        visited.append(newword)
        print('所有遍历过的节点',visited,'\n')
        print('构建出来的散列表如下')
        for k,v in graph.items():
            print(k,"  ",v)
        print('\n')
        return graph
start="hitc"
end="cogc"
adict=['hotc','dotc',dogc','lotc','locc','logc']
       
aaa=find_path(start,end,adict)
       
jieguo=[]
adict.append(start)
jieguo.append(end)
while end!=start:
       for word in adict:
           if end in aaa[word]
               end=word
               jieguo.append(end)
jieguo.reverse()
print('最终转换路径如此列表顺序：',jieguo)
   
       
           
