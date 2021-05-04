# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:25:14 2019

@author: koush
"""

def palindrome_check(a):
    i=0
    j=len(a)-1
    while i <= j:
        if a[i] != a[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

max=-1

for i in range(100,1000):
    for j in range(100,1000):
        if(palindrome_check(str(i*j))):
            if(i*j>max):
                max=i*j
                x=i
                y=j
                
print(str(x)+" "+"X"+" "+str(y)+"="+str(max))