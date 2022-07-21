# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:21:49 2021

@author: juanc
"""


# Change the current working directory
#os.chdir('/tmp')
#En Pithon el separador de carpetas es \\

#manejador_archivo = open("C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos\mbox.txt")
#print(manejador_archivo)
#x=manejador_archivo.read()
#x
#f=io.TextIOWrapper( name='mbox.txt', mode='r', encoding='cp1252')

import os

directorio=os.getcwd()
directorio
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)

#7.1 Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
#and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

fname=input('introduce the name of the file \n')
fh=open(fname,'r')
data=fh.read()
data_1=data.rstrip()
data_1=str(data_1)
data_1=data_1.upper()
print(data_1)

