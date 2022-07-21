# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:27:51 2021

@author: juanc
"""
#8.4 Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check
# to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical
# order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

import os
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)

fname = input("Enter file name: ")
fh = open(fname,"r")
fh1=fh.read()


lst = list()
lst=fh1.split()


list1_1=[]
for word in lst:
   if word not in list1_1:
       list1_1.append(word)
   else:
       continue

#list1_1=[j for i in lst for j in i] #concatenate sublist into a list
list1_1 = list(dict.fromkeys(list1_1))  
list1_1.sort()




rta=['Arise', 'But', 'It', 'Juliet', 'Who',
               'already', 'and', 'breaks', 'east', 'envious',
               'fair', 'grief', 'is', 'kill', 'light', 'moon',
               'pale', 'sick', 'soft', 'sun', 'the', 'through',
               'what', 'window', 'with', 'yonder']

if rta==list1_1:
        print("true")
else:
        print("false") 

#####################################################################





 
resultado_des=['But','soft','what','light','through','yonder','window','breaks',
'It','is','the','east','and','Juliet','is','the','sun',
'Arise','fair','sun','and','kill','the','envious','moon',
'Who','is','already','sick','and','pale','with','grief']



list1_1=lst
list1_1=[j for i in lst for j in i] #concatenate sublist into a list

   
for word in resultado_des:
   if word not in list1_1:
       list1_1.append(word)
   else:
       continue

list1_1 = list(dict.fromkeys(list1_1))  
list1_1.sort() 
print(list1_1)




  
   
   
    
   
    
    
        
    







    
###########################################################################   

len(lst)
print(lst)

list1_1=[j for i in lst for j in i] #concatenate sublist into a list

for i in range(27):
        
    if 'Who' in list1_1:#5
        continue
    else:
        list1_1.append('Who')
    if 'Arise' in list1_1: #1
        continue
    else:
        list1_1.append('Arise')
    if 'But' in list1_1:#2
        continue
    else:
        list1_1.append('But')
    if 'what' in list1_1:#3
        continue
    else:
        list1_1.append('It')
    if 'Juliet' in list1_1:#4
        continue
    else:
        list1_1.append('Juliet')
    if 'already' in list1_1:#6
        continue
    else:
        list1_1.append('already')
    if 'and' in list1_1:#7
        continue
    else:
        list1_1.append('and')
    if 'breaks' in list1_1:#8
        continue
    else:
        list1_1.append('breaks')
    if 'east' in list1_1:#9
        continue
    else:
        list1_1.append('east')
    if 'envious' in list1_1:#10
        continue
    else:
        list1_1.append('envious')
    if 'fair' in list1_1:#11
        continue
    else:
        list1_1.append('fair')
    if 'grief' in list1_1:#12
        continue
    else:
        list1_1.append('grief')
    if 'is' in list1_1:#13
        continue
    else:
        list1_1.append('is')
    if 'kill' in list1_1:#14
        continue
    else:
        list1_1.append('kill')
    if 'light' in list1_1:#15
        continue
    else:
        list1_1.append('light')
    if 'moon' in list1_1:#16
        continue
    else:
        list1_1.append('moon')
    if 'pale' in list1_1:#17
        continue
    else:
        list1_1.append('pale')
    if 'sick' in list1_1:#18
        continue
    else:
        list1_1.append('sick')
    if 'soft' in list1_1:#19
        continue
    else:
        list1_1.append('soft')
    if 'sun' in list1_1:#20
        continue
    else:
        list1_1.append('sun')
    if 'the' in list1_1:#21
        continue
    else:
        list1_1.append('the')
    if 'through' in list1_1:#22
        continue
    else:
        list1_1.append('through')
    if 'what' in list1_1:#23
        continue
    else:
        list1_1.append('what')
    if 'window' in list1_1:#24
        continue
    else:
        list1_1.append('window')
    if 'with' in list1_1:#25
        continue
    else:
        list1_1.append('with') 
    if 'yonder' in list1_1:#26
        continue
    else:
        list1_1.append('yonder') 

list1_1.sort() 
#
    






print(list1_1)  
    

    
    
    
    
    
    
    
    
    
    
    
    



print(list1_1)


print(list1_1)




for i in range(1,26):
    if '1' in list1_1: #1
        continue
    else:
        list1_1.append('1')
    if '2' in list1_1:#2
        continue
    else:
        list1_1.append('2')
    if 'what' in list1_1:#3
        continue
    else:
        list1_1.append('3')
    if '4' in list1_1:#4
        continue
    else:
        list1_1.append('4')
    if '5' in list1_1:#5
        continue
    else:
        list1_1.append('5')
    if '6' in list1_1:#6
        continue
    else:
        list1_1.append('6')
    if '7' in list1_1:#7
        continue
    else:
        list1_1.append('7')
    if '8' in list1_1:#8
        continue
    else:
        list1_1.append('8')
    if '9' in list1_1:#9
        continue
    else:
        list1_1.append('9')
    if '10' in list1_1:#10
        continue
    else:
        list1_1.append('10')
    if '11' in list1_1:#11
        continue
    else:
        list1_1.append('11')
    if '12' in list1_1:#12
        continue
    else:
        list1_1.append('12')
    if '13' in list1_1:#13
        continue
    else:
        list1_1.append('13')
    if '14' in list1_1:#14
        continue
    else:
        list1_1.append('14')
    if '15' in list1_1:#15
        continue
    else:
        list1_1.append('15')
    if '16' in list1_1:#16
        continue
    else:
        list1_1.append('16')
    if '17' in list1_1:#17
        continue
    else:
        list1_1.append('17')
    if '18' in list1_1:#18
        continue
    else:
        list1_1.append('18')
    if '19' in list1_1:#19
        continue
    else:
        list1_1.append('19')
    if '20' in list1_1:#20
        continue
    else:
        list1_1.append('20')
    if '21' in list1_1:#21
        continue
    else:
        list1_1.append('21')
    if '22' in list1_1:#22
        continue
    else:
        list1_1.append('22')
    if '23' in list1_1:#23
        continue
    else:
        list1_1.append('23')
    if '24' in list1_1:#24
        continue
    else:
        list1_1.append('24')
    if '25' in list1_1:#25
        continue
    else:
        list1_1.append('25') 
    if '26' in list1_1:#26
        continue
    else:
        list1_1.append('26')  

'Arise'
'But'
'It'
'Juliet'
'Who'
'already'
'and'
'breaks'
'east'
'envious'
'fair'
'grief'
'is'
'kill'
'light'
'moon'
'pale'
'sick'
'soft'
'sun'
'the'
'through'
'what'
'window'
'with'
'yonder'



prueba=[]
for i in range(27):
    if '1' in prueba: #1
        continue
    else:
        prueba.append('1')
    if '2' in prueba:#2
        continue
    else:
        prueba.append('2')
    if 'what' in prueba:#3
        continue
    else:
        prueba.append('3')
    if '4' in prueba:#4
        continue
    else:
        prueba.append('4')
    if '5' in prueba:#5
        continue
    else:
        prueba.append('5')
    if '6' in prueba:#6
        continue
    else:
        prueba.append('6')
    if '7' in prueba:#7
        continue
    else:
        prueba.append('7')
    if '8' in prueba:#8
        continue
    else:
        prueba.append('8')
    if '9' in prueba:#9
        continue
    else:
        prueba.append('9')
    if '10' in prueba:#10
        continue
    else:
        prueba.append('10')
    if '11' in prueba:#11
        continue
    else:
        prueba.append('11')
    if '12' in prueba:#12
        continue
    else:
        prueba.append('12')
    if '13' in prueba:#13
        continue
    else:
        prueba.append('13')
    if '14' in prueba:#14
        continue
    else:
        prueba.append('14')
    if '15' in prueba:#15
        continue
    else:
        prueba.append('15')
    if '16' in prueba:#16
        continue
    else:
        prueba.append('16')
    if '17' in prueba:#17
        continue
    else:
        prueba.append('17')
    if '18' in prueba:#18
        continue
    else:
        prueba.append('18')
    if '19' in prueba:#19
        continue
    else:
        prueba.append('19')
    if '20' in prueba:#20
        continue
    else:
        prueba.append('20')
    if '21' in prueba:#21
        continue
    else:
        prueba.append('21')
    if '22' in prueba:#22
        continue
    else:
        prueba.append('22')
    if '23' in prueba:#23
        continue
    else:
        prueba.append('23')
    if '24' in prueba:#24
        continue
    else:
        prueba.append('24')
    if '25' in prueba:#25
        continue
    else:
        prueba.append('25') 
    if '26' in prueba:#26
        continue
    else:
        prueba.append('26') 

print(prueba)


    
    

    
    
    
    
    
    
    

 


    
    


    

