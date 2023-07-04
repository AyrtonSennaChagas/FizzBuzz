# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:44:21 2023

@author: ayrth
"""

teste = 11

def dividirFizzBuzz (n):
    i = teste%3
    i2 = teste%5
    return i == 0 and i2 == 0

def dividirFizz (n):
    i = teste%3
    return i == 0

def dividirBuzz (n):
    i = teste%5
    return i == 0

if dividirFizzBuzz (teste):
    print ("FizzBuzz")
    
elif dividirFizz (teste):
    print ("Fizz")
    
elif dividirBuzz (teste):
    print("Buzz")
    
else:
    print (teste)