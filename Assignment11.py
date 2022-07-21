# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:02:12 2021

@author: juanc
"""
import os
import re
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)

data=open("regex_sum.txt") #actual data
data2=open("regex_sum2.txt") # Data format example
data3=open("regex_sums.txt") #sample data


def digitos(datos):
   data=datos.read() 
   resultvector=[]  
   x=[]
   b1=[]
   b2=[]
   b3=[]
   b4=[]
   b5=[]
   b6=[]
   b7=[]
   bcor=[]
   bcor2=data.split("\n")
   for line in bcor2:
       x.append(re.findall('\d+',line))
   b=str(x)
   b1=b.replace("[]","")
   b2=b1.replace("[","")
   b3=b2.replace("]","")
   b4=b3.replace(", ,",",")
   b5=b4.replace("'","")
   b6=b5.replace(" ","")
   b6=b5.split(",")
   for i in range(0,len(b6)):
      if b6[i]==" " or b6[i]=="":
        continue
      else:
          b7.append(b6[i]) 
   for i in range(0,len(b7)):
       resultvector.append(int(b7[i]))   
   return resultvector               

r_1=digitos(data)
print(sum(r_1))

digitos(data3) # 445833 Sample data is fine
digitos(data2) # 27486  Data format example is fine
digitos(data)  # 687652 actual data Error

#Optional: Just for Fun
#There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

#Python 2
#import re
#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

#Python 3:
#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
#Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )


#print( sum( [ data *** * in refindall('[0-9]+',.read()) ] )







#####################################################


resultvector=[]  
x=[]
b1=[]
b2=[]
b3=[]
b4=[]
b5=[]
b6=[]
b7=[]
bcor=[]
bcor2=data_1.split("\n")
for line in bcor2:
    x.append(re.findall('[0-9]+',line))
b=str(x)
b1=b.replace("[]","")
b2=b1.replace("[","")
b3=b2.replace("]","")
b4=b3.replace(", ,",",")
b5=b4.replace("'","")
b6=b5.replace(" ","")
b6=b5.split(",")
for i in range(0,len(b6)):
  if b6[i]==" " or b6[i]=="":
    continue
  else:
      b7.append(b6[i]) 
for i in range(0,len(b7)):
   resultvector.append(int(b7[i]))   
print(sum(resultvector))                
       
      
       
       
       
       
   

digitos(data_2)
 



################################


    
del b7  

b7[7]==" "
    
    
       result_vec.append(int(b6[i]))   
       
        
        

        


x=[]
result_vec=[]  
for line in data_1:
    x.append(re.findall('\d+',line))


data_2[1]

x=[]
result_vec=[]
base_cor=data_2.split("\n")

    
    
    
    
    
base_cor=base_cor.replace(" ",",") #reemplaza espacios simples
base_cor=base_cor.replace("\n",",") #reemplaza espacios compuestos
base_cor2=base_cor.split(",")



a="7746,12,1929,8827"

for line in base_cor:
    if re.search('^\d+',base_cor):
        print(line)
    else:
        continue


for i in a:
    if :
        print(i)
    




forlen(base_cor)






base_cor=base_cor.split(" ")
base_cor=base_cor.replace(" ","")
print(line)

dir(list)

for line in base_cor:
    if re.findall('^[0-9]+',line):
       x.append(line)

dir(str)    
 
    
    
 if re.findall('^\d+',line):
                x.append(line)
for i in range(0,len(x)):
   result_vec.append(int(x[i]))   
print(sum(result_vec))           

    


