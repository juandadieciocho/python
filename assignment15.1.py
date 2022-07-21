# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:21:53 2021

@author: juanc
"""

import sqlite3
import os
import re

path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\Estudios coursera\\learning Python\\bases_de_datos'
os.chdir(path_1)


manejador=open('mbox.txt').read().rstrip()
correos=re.findall('(From.\w+.\w+@\w+.\w+\w+.\w....\s?)',manejador)

c1=[]

for line in correos:
    c1.append(line.split())

correos=[]
for line in c1:
    correos.append(line[1])


message=[]
for line in correos:
    message.append(line.replace("From ",""))

domains=[]
for line in message:
    domains.append(str( re.findall('@\w+.+',line)))

domainsf=[]
for line in domains:
    domainsf.append(line.replace('@',""))


df1=[]
df2=[]
df3=[]


for line in domainsf:
   df1.append(line.replace("[",""))

for line in df1:
  df2.append(line.replace("]",""))

for line in df2:
   df3.append(line.replace("''",""))



t1=[]

domainsf=df3

for line in domainsf:
    if line not in t1:
        t1.append(str(line))
    else:
        continue
t2=[]
for line in t1:
    t2.append(domainsf.count(line))

path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\Estudios coursera\\learning Python\\SQL\\DB'

t3=[]
for line in t1:
   t3.append(line.replace("'",""))

t1=t3

conn = sqlite3.connect('Counts') # la conexion
cur = conn.cursor()# el manejador
#cur.execute('DROP TABLE Counts')
cur.execute('CREATE TABLE Counts1 (org TEXT, count INTEGER)')

for i in range(0,len(t1)):
   cur.execute(" INSERT INTO Counts1 (org ,count) VALUES (?,?) ",(t1[i],t2[i]))

cur.execute("CREATE TABLE Counts AS SELECT * FROM Counts1 ORDER BY count DESC")
cur.execute(" DROP TABLE Counts1")

    
conn.commit()
conn.close()
 
# Closi




    


ng the connection
conn.close()