# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:57:25 2021

@author: juanc
"""
#3.3 Escriba un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de rango, imprima un error. Si el puntaje está entre 0.0 y 1.0, imprima una calificación usando la siguiente tabla:
#Puntaje Calificación
#> = 0.9 A
#> = 0.8 B
#> = 0.7 C
#> = 0.6 D
#<0.6 F
#Si el usuario ingresa un valor fuera del rango, 
#imprima un mensaje de error adecuado y salir. 
#Para la prueba, ingrese una puntuación de 0.85.
class Exception_1(Exception):

    pass

class Exception_2(Exception):
    pass


try:
    text_score='write a number between 0.0 to 1.0 \n'
    score=input(text_score)
    if score.isdigit()==True:
        raise Exception_1("floating number")
    else:
        try:
          score=float(score) 
          if score<0 or score>1.0:
            raise Exception_2("number between 0 and 1")
          else:
            if score>=0.9 :
                print('A')
            elif score>=0.8 :
                print('B')
            elif score>=0.7 :
                print('C')
            elif score>=0.6 :
                print('D')
            else:
                print('F')
        except Exception_2 as e:
             print("introduce a number between 0 and 1!")
             print(e) 
             quit()
except Exception_1 as e:
    print("introduce a floating number!")
    print(e)
    quit()








