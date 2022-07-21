# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Ejercicio 1: Escribe una función llamada recortar que toma una lista y
# la modifica,
#removiendo el primer y último elemento, y regresa None. Después escribe una
#función llamada medio que toma una lista y regresa una nueva lista que contiene
#todo excepto el primero y último elementos.

lista=['a','b','c']
type(lista)
hola=lista

def recortar(a):
    lista_1=a
    lista_1.pop(0)
    indicador=int(len(lista_1)-1)
    lista_1.pop(indicador)
    resultado_1=('None:',lista_1)
    return resultado_1
    
resultado=recortar(hola)
print(resultado)


#remove elimina un elemento dado
#pop elimina un elemento por el indice

#Ejercicio 2: Encontrar que línea del programa de arriba no está protegida 
#(método guardián) propiamente.







#Trata de construir un archivo de
#texto que cause que el programa falle y después modifica el programa de
#modo que la línea es propiamente protegida y pruébalo para asegurarte
#que el programa es capaz de manejar tu nuevo archivo de texto.

#Ejercicio 3: Reescribe el código guardián en el ejemplo de arriba sin las
#dos sentencias if. En vez de eso, utiliza una expresión lógica compuesta
#utilizando el operador lógico or con una sola sentencia if.


import os
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)


manejador = open('mbox-short.txt')

contador = 0
for line in manejador:
    palabras = line.split()
    if len(palabras) == 0 : continue
    if palabras[0] != 'From' : continue
print(palabras)


contador = 0
for linea in manejador:
    palabras = line.split() 
    # print 'Depuración:', palabras
    if len(palabras) == 0 or palabras[0] != 'From': continue
print(palabras[2])




import os
path_1='C:\\Users\\juanc\\OneDrive\\Escritorio\\learning Python\\bases_de_datos'
os.chdir(path_1)


manejador = open('mbox-short.txt')

result=[]
for line in manejador:
    if not line.startswith("From") : continue
    result.append(line)
    
result_2=result 



a=[]
for i in range(53):
    a.append(str(result_2[i].split(' ')))
    
 
contador=0
leo=[]
for i in range(52): 
    contador=contador+1
    leo.append(contador)
print(contador)
    
b=[]
len(a)
for i in range(52): 
    contador=contador+1
    b.append(a[i].split(','))
    leo.append(contador)
print(contador)

c=[]
for i in range(len(b)-1):
    if len(b[i])>3:
        c.append(b[i][2])
    else: 
        continue

print(c)

################################################################
#para imprimir variables con el mismo nombre diferente numeral

for k in range(5):
    exec(f'cat_{k} = k*2')  
   
    palabras.append(result[i][3])
  
    
    
       


         
    







   
    
   






        
   

