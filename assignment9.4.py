# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:08:40 2021

@author: juanc
"""

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

mail_1=list(dict.fromkeys(mail))    


count_1=[]
count_2=0
for mail_1 in mail:
    if mail_1 in mail:
        count_2=mail.count(mail_1)
        count_1.append(count_2)
    else:
        continue



for value in count_1:
    print(value)

d_mail={}
values_1=count_1
for word in mail:
    for value in values_1:
       d_mail[word]=value
       values_1.remove(value)
       break
        
for key,value in d_mail.items():
    if value == max(d_mail.values()):
        print(key,value)
    else:
        continue
    






# initializing lists 
test_keys = ["Rash", "Kil", "Varsha"] 
test_values = [1, 4, 5] 
  
# Printing original keys-value lists 
print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  
# using naive method 
# to convert lists to dictionary 
res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break  





    

