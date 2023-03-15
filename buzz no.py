# -*- coding: utf-8 -*-
"""
Created on Wed 15 14:09:19 2023

@author: Akshay
"""
#BUZZ no. - A number div by 7 or ending with 7
def if_buzz(num):
        if num % 7 == 0 or num % 10 == 7:
              return True

num = int(input("Enter a number"))
if if_buzz(num):
    print("The number is Buzz number")
else:
    print("The number is not a Buzz number")
        
