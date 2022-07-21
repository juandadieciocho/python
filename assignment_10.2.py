# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:00:09 2021

@author: juanc
"""

#10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time 
#and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the 
#counts, sorted by hour as shown below.

import os
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)


manejador=open('mbox-short1.txt','r')


list_1=list()
for line in manejador:
    if line.startswith("From") and not line.startswith("From:") and len(line)>1:
        list_1.append(line)
    else:
        continue


list_11=[]
for i in range(len(list_1)):
    list_11.append(list_1[i].replace(" ",","))
    
list_12=[]
list_13=[]
list_14=[]
for i in range(len(list_11)):
    list_12.append(list_11[i].replace(",,",","))
    list_13.append(list_12[i].replace("'",""))
    list_14.append(list_13[i].split(","))
    
hours=[]
for i in range(len(list_14)):
    hours.append(list_14[i][5])


hours_cut=[]
for i in range(len(hours)):
    hours_cut.append(hours[i][:2])
    
t_hours=list(dict.fromkeys(hours_cut))  


frequen_1=[]
for h in t_hours:
    frequen_1.append(hours_cut.count(h))
 
values=frequen_1    
dict_1=dict() 
for k in t_hours:
    for v in values:
        dict_1[k]=v
        values.remove(v)
        break
    
    
f_ans_1=sorted( [(k,v) for k,v in dict_1.items()])

for k,v in f_ans_1:
    print(k,v)







    
    
    




list_12[1][1]        
    