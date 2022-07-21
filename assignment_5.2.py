# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:14:07 2021

@author: juanc
"""

#5.2 Write a program that repeatedly prompts
# a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest 
#of the numbers. If the user enters anything other than a valid
# number catch it with a try/except and put out an appropriate 
#message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
#match the output below.

#prueba
n=range(6)
num=None
largest=None
smallest=None
for i in n :
    num=input('introduce a number: ')
    try:
        num=int(num)
        if smallest is None:
            smallest=num
        elif  num < smallest  :
            smallest=num
        else:
            smallest=smallest
        if largest is None:
            largest=num
        if num > largest:
            largest=num
        else:
            largest=largest
    except:
        if num=='done':
            print('Maximum is ',largest,'Minimum is ',smallest)
            break
        elif type(num) is str:
            print('invalid value')
            continue
#examen
num=None
largest=None
smallest=None
while True :
    num=input('introduce a number: ')
    try:
        num=int(num)
        if smallest is None:
            smallest=num
        elif  num < smallest  :
            smallest=num
        else:
            smallest=smallest
        if largest is None:
            largest=num
        if num > largest:
            largest=num
        else:
            largest=largest
    except:
        if num=='done':
            print('Maximum is',largest)
            print('Minimum is',smallest)
            break
        elif type(num) is str:
            print('Invalid input')
            continue
   
   
       
    
    

