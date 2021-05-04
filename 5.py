# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:49:22 2019

@author: koush
"""

import math

def lcm(a,b):
    return (a*b)/math.gcd(a,b)

ans=lcm(1,2)

for i in range (3,20):
    ans=lcm(int(ans),i)
    
print(ans)