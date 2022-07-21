# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:26:29 2021

@author: juanc
"""

#8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out
#the second word in the line (i.e. the entire address of
# the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output 
#to see how to print the count.

import os
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)

manejador=open('mbox-short1.txt')


result=[]
counting=0
for line in manejador:
    if line.startswith("From") and not line.startswith("From:") and len(line)>1: 
        result.append(line)
        counting=counting+1
    else:
        continue
    
result_2=result 


#particion linea
part_1=[]
part_2=[]
for i in range(len(result_2)):
    part_1.append(str(result_2[i].split(', ')))
    part_2.append(part_1[i].replace(' ',','))


len(part_2)
part_2_1=[]
mail=[]
for i in range(len(part_1)):
    part_2_1.append(part_2[i].split(","))
    mail.append(part_2_1[i][1])
    
for i in range(len(mail)):     
    print(mail[i])   
print("There were", counting, "lines in the file with From as the first word")

################################################################################
