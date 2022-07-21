# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:00:34 2021

@author: juanc
"""

print(ord('G'))
print(chr(42))
codigos=[108,105,110,101]


mensaje=[]
for codigo in codigos:
        mensaje.append(chr(codigo))

texto="<p>Please click <a href=http://www.dr-chuck.com>here</a></p>"
import re

a=[]
a=re.findall("href=(.+)",texto)


#Tarea
#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1129519.html (Sum ends with 85)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
# Recuperar todas las etiquetas de anclaje
etiquetas = sopa('span')
texto=str(etiquetas)
numeros=re.findall("\d+",texto)
numeros_1=[]
for numero in numeros:
    numeros_1.append(int(numero))
print(sum(numeros_1))



import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_1129519.html'
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
# Recuperar todas las etiquetas de anclaje
etiquetas = sopa('span')
texto=str(etiquetas)
numeros=re.findall("\d+",texto)
numeros_1=[]
for numero in numeros:
    numeros_1.append(int(numero))
print(sum(numeros_1))

#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1129519.html (Sum ends with 85)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#Data Format
#The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1129519.html' 
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
tags = soup('span')
texto=str(tags)
numeros=re.findall('\d+',texto)
numeros_1=[]
for numero in numeros:
    numeros_1.append(int(numero))
print(sum(numeros_1))

#Following Links in Python

#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Finley.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: S
#Strategy
#The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' http://py4e-data.dr-chuck.net/known_by_Finley.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
nombres=[]
for tag in tags:
    nombres.append(tag.get('href', None))

sopa=[]
html1=[]
for name in nombres:
    html1 = urllib.request.urlopen(name, context=ctx).read()
    sopa.append(BeautifulSoup(html, 'html.parser'))

textos=[]
for texto in sopa:
    textos.append(str(texto))


nombres=[]
for nombre in textos:
    nombres.append(re.findall(">\w+<",nombre))  





nombres1=[]
for nombre in nombres:
   nombres1.append(nombre[17])
    



# Ignore SSL certificate errors

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url2=[]
url = ' http://py4e-data.dr-chuck.net/known_by_Finley.html'
url2.append(url)
html1 = urllib.request.urlopen(url2[0], context=ctx).read()
soup1 = BeautifulSoup(html1, 'html.parser')
tags = soup1('a')
link=[]
for tag in tags:
    link.append(tag.get('href', None))
url2.append(link[19])

for i in range(1,9):
    html1 = urllib.request.urlopen(url2[i], context=ctx).read()
    soup1 = BeautifulSoup(html1, 'html.parser')
    tags = soup1('a')
    link=[]
    for tag in tags:
        link.append(tag.get('href', None))
    url2.append(link[19])




htmlf = urllib.request.urlopen(url2[7], context=ctx).read()
soupf = BeautifulSoup(html1, 'html.parser')
tagsf = soup1('a')
textof=str(tagsf)

nombres=re.findall(">\w+<",textof)
nombresf=[]
for nombre in nombres:
    nombresf.append(re.findall("\w+",nombre))
print(nombresf)
    

###################################################################SAMPLE

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def numero_adel(pos):
    n=pos-1
    return n
def repeticion(nrep):
    rep=nrep-1
    return rep
 

n_k=numero_adel(3)
repet1=repeticion(4)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url2=[]
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url2.append(url)
html1 = urllib.request.urlopen(url2[0], context=ctx).read()
soup1 = BeautifulSoup(html1, 'html.parser')
tags = soup1('a')
link=[]
for tag in tags:
    link.append(tag.get('href', None))
url2.append(link[n_k])


for i in range(1,repet1):
    html1 = urllib.request.urlopen(url2[i], context=ctx).read()
    soup1 = BeautifulSoup(html1, 'html.parser')
    tags = soup1('a')
    link=[]
    for tag in tags:
        link.append(tag.get('href', None))
    url2.append(link[n_k])



html_11=[]
soup_11=[]
tags_11=[]
texto_11=[]
for base in url2:
    html_11 = urllib.request.urlopen(base, context=ctx).read()
    soup_11 = BeautifulSoup(html_11, 'html.parser')
    tags_11 = soup_11('a')
    texto_11.append(str(tags_11))

nombres_todo=[]
for line in texto_11:
    nombres_todo.append(re.findall(">\w+<",line))


for line in nombres_todo:
    print(line[n_k])
       
#################################################### ACTUAL DATA

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def numero_adel(pos):
    n=pos-1
    return n
def repeticion(nrep):
    rep=nrep-1
    return rep
 

n_k=numero_adel(18)
repet1=repeticion(7)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url2=[]
url = 'http://py4e-data.dr-chuck.net/known_by_Finley.html'
url2.append(url)
html1 = urllib.request.urlopen(url2[0], context=ctx).read()
soup1 = BeautifulSoup(html1, 'html.parser')
tags = soup1('a')
link=[]
for tag in tags:
    link.append(tag.get('href', None))
url2.append(link[n_k])


for i in range(1,repet1):
    html1 = urllib.request.urlopen(url2[i], context=ctx).read()
    soup1 = BeautifulSoup(html1, 'html.parser')
    tags = soup1('a')
    link=[]
    for tag in tags:
        link.append(tag.get('href', None))
    url2.append(link[n_k])



html_11=[]
soup_11=[]
tags_11=[]
texto_11=[]
for base in url2:
    html_11 = urllib.request.urlopen(base, context=ctx).read()
    soup_11 = BeautifulSoup(html_11, 'html.parser')
    tags_11 = soup_11('a')
    texto_11.append(str(tags_11))

nombres_todo=[]
for line in texto_11:
    nombres_todo.append(re.findall(">\w+<",line))


for line in nombres_todo:
    print(line[n_k])            
        

                
        


# Montgomery Mhairade Butchi Anayah





















