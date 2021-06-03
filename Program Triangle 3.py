# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:35:44 2020

@author: Dennis Mose
"""

print("Enter 3 integers which are sides of a triangle");
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
c1 = (1 <= a) and (a <= 300)
c2 = (1 <= b) and (b <= 300)
c3 = (1 <= c) and (c <= 300)
if  (c1 < 1 or c1 > 300) or (c2 <1 or c2 > 300) or (c3 <1 or c3>300):
    print("Value is not in the range of permitted values")
    
elif    c1 and c2 and c3:
    print("side A is ", a)
    print("side B is ", b)
    print("side C is ", c) 
   
    if (a < b + c) and (b < a + c) and (c < a + b) : 
        IsATriangle = True
    else: 
        IsATriangle = False;
       
    if a == b == c:
        print("Equilateral")
    elif a != b != c:
        print("Scalene")
    else:
        print("Isosceles")
else:
  print("Not a Triangle")
