# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:39:30 2020

@author: Dennis Mose
"""

print("Enter 3 integers which are sides of a triangle");
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("side A is ", a)
print("Side B is ", b)
print("Side C is ", c)

def IsATriangle(a, b, c):  
    if(a < b + c) and (b < a + c) and (c < a + b) : 
        return True
    else: 
        return False 
if IsATriangle:
    if  a == b == c:
        print("Equilateral") 

    elif a != b != c:
        print("scalene")
    
    elif a == b or b == c or a == c:
        print ("isoscless")
    else:
        print("NotATriangle")

