# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:59:33 2020

@author: Dennis Mose
"""

print("Enter 3 integers which are sides of a triangle");
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("side A is ", a)
print("Side B is ", b)
print("Side C is ", c)

if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
    print("NotATriangle")
else:
    if  a == b == c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")