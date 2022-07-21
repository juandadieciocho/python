# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:49:57 2021

@author: juanc
"""

#7.2 Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values
# from each of the lines and compute the average of those values 
#and produce an output as shown below. Do not use the sum() function
# or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are
# testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

import os
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)


fname = input("Enter file name: ")
fh = open(fname)
result=[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    result.append(line)






index_numbers_1=[]
numbers=[]
longitud=[]
numbers_1=[]
for i in range(0,27):
    index_numbers_1.append(result[i].find('0'))
    longitud.append((len(result[i])))
    numbers.append((result[i][index_numbers_1[i]:longitud[i]]))
    numbers_1.append(float(numbers[i]))



def mean(a):
    try:
        addition_1=0
        avg_1=0
        if isinstance(a,list)==True :
            for i in range(0,len(a)):
                addition_1=addition_1+a[i]           
    except:
        quit()
    avg_1=addition_1/len(a)
    return(avg_1)                             
               
                
result_2=mean(numbers_1)

print("Average spam confidence:",result_2)    











del index_numbers_1
del longitud
del numbers
del numbers_1



    







for line in fh.readlines():
   if  line.startswith("X-DSPAM-Confidence:"):
       index=line.find("X-DSPAM-Confidence:")
       if index != -1:
           result.append(index)    
   else:    
       continue    
print(result)

for line in fh.readlines():
        # Find the start of the word
        index = line.find("X-DSPAM-Confidence:")
        # If the word is inside the line
        if index != -1:
            if index < 60:
                result.append(line[:index])
            else:
                result.append(line[index-60:index])
print(result)   

result=[]
for line in fh:
    if  line.startswith("X-DSPAM-Confidence:"):
        result.append(print(line))
    else:
        continue
    
    
    
    
    
    
    if fh.find("X-DSPAM-Confidence:"):
        result.append(line)
    else:
        continue





for line in fh.readlines():
        # Find the start of the word
        index = line.startswith("X-DSPAM-Confidence:")
        # If the word is inside the line
        if index != -1:
            if index < 60:
                result.append(line[:index])
            else:
                result.append(line[index-60:index])
print(result)  
             
                
                
                
                


a="X-DSPAM-Confidence:"
text=ft.append(a)




a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
i_1=a.append(b)
print(i_1)









def counter_1(fh):
    
    for line in fh:
        text=0
        if line.startswith("X-DSPAM-Confidence:"):
            text=fh[0:]
        else:
            continue
return(text)


text_1=counter_1(fh)

text=fh.read()
text_1=text.rstrip()





#%config InteractiveShell.ast_node_interactivity='all'



   


