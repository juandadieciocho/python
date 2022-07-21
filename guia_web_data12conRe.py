# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:16:46 2021

@author: juanc
"""
import re

# re.search: busca un patrón en otra cadena:
# re.match: busca un patrón al principio de otra cadena:
# re.split: divide una cadena a partir de un patrón:
# re.sub: sustituye todas las coincidencias en una cadena:
# re.findall: busca todas las coincidencias en una cadena:

#Patrones con varios valores
#Si queremos comprobar varias posibilidades, podemos utilizar una tubería | a modo de OR. Generalmente pondremos el listado de alternativas entre paréntesis ():


texto = "hola adios hello bye"

re.findall('hola|hello', texto)

#Patrones con sintaxis repetida
#Otra posibilidad que se nos ofrece es la de buscar patrones con letras repetidas, y aquí es donde se empieza a poner interesante. Como podemos o no saber de antemano el número de repeticiones hay varias formas de definirlos.


texto = "hla hola hoola hooola hooooola"
#Antes de continuar, y para aligerar todo el proceso, vamos a crear una función capaz de ejecutar varios patrones en una lista sobre un texto:


def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )

patrones = ['hla', 'hola', 'hoola']
buscar(patrones, texto)

#Con meta-carácter +/* Lo utilizaremos para definir una o más repeticiones de la letra a la izquierda del meta-carácter:
    
#Con meta-carácter ?
#Lo utilizaremos para definir una o ninguna repetición de la letra a la izquierda del meta-carácter:

patrones = ['ho*', 'ho+', 'ho?', 'ho?la']
buscar(patrones, texto)

# Con número de repeticiones explícito {n}:
#Lo utilizaremos para definir 'n' repeticiones exactas de la letra a la izquierda del meta-carácter:
patrones = ['ho{0}la', 'ho{1}la', 'ho{2}la']
buscar(patrones, texto)

#Con número de repeticiones en un rango {n, m}
#Lo utilizaremos para definir un número de repeticiones variable entre 'n' y 'm' de la #letra a la izquierda del meta-carácter:
 
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']

buscar(patrones, texto)

#Cuando nos interese crear un patrón con distintos carácteres, podemos definir conjuntos entre paréntesis:

texto = "hala hela hila hola hula"
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
buscar(patrones, texto)

#Exclusión en grupos [^ ]:
#Cuando utilizamos grupos podemos utilizar el operador de exclusión ^ para indicar una búsqueda contraria:

texto = "hala hela hila hola hula"
patrones = ['h[o]la', 'h[^o]la'] 
buscar(patrones, texto)

#Rangos [ - ]:
#Otra característica que hace ultra potentes los grupos, es la capacidad de definir rangos. Ejemplos de rangos:

#[A-Z]: Cualquier carácter alfabético en mayúscula (no especial ni número).
#[a-z]: Cualquier carácter alfabético en minúscula (no especial ni número).
#[A-Za-z]: Cualquier carácter alfabético en minúscula o mayúscula (no especial ni número).
#[A-z]: Cualquier carácter alfabético en minúscula o mayúscula (no especial ni número).
#[0-9]: Cualquier carácter numérico (no especial ni alfabético).
#[a-zA-Z0-9]: Cualquier carácter alfanumérico (no especial).
#Tened en cuenta que cualquier rango puede ser excluido para conseguir el patrón contrario.

##Códigos escapados \

#Si cada vez que quisiéramos definir un patrón variable tuviéramos que crear rangos, al final tendríamos expresiones regulares gigantes. Por suerte su sintaxis también acepta una serie de caracteres escapados que tienen un significo único. Algunos de los más importantes son:

#Código	Significado
#\d	numérico
#\D	no numérico
#\s	espacio en blanco
#\S	no espacio en blanco
#\w	alfanumérico
#\W	no alfanumérico


#Ejercicio uno: escribe un programa simple que simule la operación del
#comando grep en Unix. Debe pedir al usuario que ingrese una expresión
#regular y cuente el número de líneas que coincidan con ésta:


import re
import os

path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\Estudios coursera\\learning Python\\bases_de_datos'
os.chdir(path_1)

for x in os.listdir('.'):
    if os.path.isfile(x): print('f-', x)
    elif os.path.isdir(x): print('d-', x)
    elif os.path.islink(x): print('l-', x)
    else: print('---', x)       

#Ejercicio 1: Cambia el programa del socket socket1.py para que le pida al
#usuario la URL, de modo que pueda leer cualquier página web. Puedes
#usar split('/') para dividir la URL en las partes que la componen, de
#modo que puedas extraer el nombre del host para la llamada a connect
#del socket. Añade comprobación de errores utilizando try y except para
#contemplar la posibilidad de que el usuario introduzca una URL mal
#formada o inexistente.

#########################################################################        
import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
while True:
datos = misock.recv(512)
if len(datos) < 1:
break
print(datos.decode(),end='')
misock.close()
##########################################################################3
import socket
import re
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#usuario_url=str(input("introduzca la url deseada : \n"))
usuario_url=str("http://data.pr4e.org/romeo.txt")
domain=re.findall("//\w+.\w+.\w+",usuario_url)
domain1=(domain[0].replace("//",""))
misock.connect((domain1, 80))
cmd1='GET'
prot1='HTTP/1.0\r\n\r\n'
usuario_request=cmd1+" "+usuario_url+" "+prot1
cmd=usuario_request.encode()
misock.send(cmd)
while True:
    datos = misock.recv(512)
    if len(datos) > 300:
        break
print(datos.decode(),end='')
misock.close()

print(datos)
#Ejercicio 2: Cambia el programa del socket para que cuente el número
#de caracteres que ha recibido y se detenga, con un texto en pantalla,
#después de que se hayan mostrado 3000 caracteres. El programa debe
#recuperar el documento completo y contar el número total de caracteres,
#mostrando ese total al final del documento.

import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
while True:
    datos = misock.recv(512)
    if len(datos) > 300:
        print('supera el limite de 3000 caracteres')
        break
print(datos.decode(),end='')
misock.close()
lectura=str(datos)
palabras=lectura.split()

cuentas=[]
for palabra in palabras:
    cuentas.append(palabras.count(palabra))

resultado2=[list(x) for x in zip(palabras, cuentas)]

#Ejercicio 3: Utiliza urllib para rehacer el ejercicio anterior de modo que
#(1) reciba el documento de una URL, (2) muestre hasta 3000 caracteres,
#y (3) cuente la cantidad total de caracteres en el documento. No te
#preocupes de las cabeceras en este ejercicio, simplemente muesta los
#primeros 3000 caracteres del contenido del documento.

import urllib.request, urllib.parse, urllib.error
datosej3=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#Syntax: os.read(fd, n)

#Parameter:
#fd: A file descriptor representing the file to be read.
#n: An integer value denoting the number of bytes to be read from the file associated with the given file descriptor fd.

man_a = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
info=man_a.read(3000)
texto=str(info)
texto1=texto.split(" ")
cuentas=[]
for palabra in texto1:
    cuentas.append(texto1.count(palabra))
resultado2=[list(x) for x in zip(texto1, cuentas)]

#Ejercicio 4: Cambia el programa urllinks.py para extraer y contar las
#etiquetas de párrafo (p) del documento HTML recuperado y mostrar
#el total de párrafos como salida del programa. No muestres el texto de
#los párrafos, sólo cuéntalos. Prueba el programa en varias páginas web
#pequeñas, y también en otras más grandes.

import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://code.visualstudio.com/docs/?dv=win64user'
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
print(sopa)
# Recuperar todas las etiquetas de anclaje
etiquetas = sopa('p')
texto=str(etiquetas)
parrafos=re.findall("<p>",texto)
parrafos.count("<p>")



#Exploring the HyperText Transport Protocol

#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

#http://data.pr4e.org/intro-short.txt
#There are three ways that you might retrieve this web page and look at the response headers:

#Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
#Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#Enter the header values in each of the fields below and press "Submit".


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


