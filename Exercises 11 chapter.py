^# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 20:37:28 2021

@author: juanc
"""
import os
import re
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)

# circunflejo ^ alt 94
man = open('mbox-short.txt')

texto=[]
for linea in man:
    texto.append(linea.rstrip())
    

for linea in man:
    linea = linea.rstrip()
    if re.search('^From ', linea):
        print(linea)

for linea in texto:
    linea=linea.rstrip()
    if re.search('^From ', linea):
        print(linea)

####Funcion para contar ocurrencias
texto=[]
for linea in man:
    texto.append(linea.rstrip())
    
In_1=input('Introduzca la expresion regular a mirar:  \n')
In_1=r'^F..m\s'
resultados=[]
contador=0

for linea in texto:
    linea = linea.rstrip()
    if re.search(In_1, linea):
        resultados.append(linea)
contador=len(linea)

print("mbox.txt tiene ",contador," líneas que coinciden con ",In_1)

##################################################

busq_num=r'^X\S*:\s([0-1]+)'
resultados=[]
for linea in texto:
    linea = linea.rstrip()
    x= re.findall(busq_num, linea)
    if len(x)>0:
        resultados.append(linea)



a=resultados[2]
re.findall(r'\d+\.\d+',a)
re.findall(r'([0-9]+\.\d+)',a)
valorest=[]
busq_num2=r'(\d+\.\d+)'      
for linea in resultados:
    linea=linea.strip()
    valorest.append(re.findall(busq_num2,linea))


valorest1=[]
for i in range(0,len(valorest)):
    valorest1.append(str(valorest[i]))

 valorest1[1].rstrip('"')

print(valorest1)

valoresf=[]
for i in range(0,54):
    valoresf.append(float(valorest1[i]))