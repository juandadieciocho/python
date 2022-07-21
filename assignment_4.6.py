# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:12:29 2021

@author: juanc
"""

#4.6 Write a program to prompt the user for hours 
#and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and 
#time-and-a-half for the hourly rate for all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() 
#and use the function to do the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75). You should use input to read a 
#string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to -
# you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function.

#para mi
#def computepay(h,r):
#    pay=0
#    text="Pay:"
#    res_1=type(h)==str
#    res_2=type(r)==str
#    if res_1==True :
#        hrs = float(input("Enter Hours: \n"))
#        h=hrs
#    if res_2==True :
#        rate= float(input("Enter Rate: \n"))
#        r=rate
#    if h<=40 :
#        pay=h*r
#    else:
#        pay=40*r+(h-40)*(1+(1/2))*r
#    return [text,pay];
    
#a=computepay('45','10.5') 
#print(a) 

#para resultados
#para lista
#para diccionario

#def fun():  
#    d = dict();   
#    d['str'] = "GeeksforGeeks"
#    d['x']   = 20
#    return d  
    
# Driver code to test above method  
#d = fun()   
#print(d)  

#para la clase modelo 1
   
#def computepay(h,r):
#    pay=0
#    res_1=type(h)==str
#    res_2=type(r)==str
#    if res_1==True :
#        hrs = float(input("Enter Hours: \n"))
#        h=hrs
#    if res_2==True :
#        rate= float(input("Enter Rate: \n"))
#        r=rate
#    if h<=40 :
#        pay=h*r
#    else:
#        pay=(40*r)+(h-40)*(1+(1/2))*r
#    return pay; 

#values=computepay(45,10.5) 
#print("Pay ",values)
#####
def computepay(h,r):
    text_hour="enter the hours \n"
    text_rate="enter the rate \n"
    hour_1=input(text_hour)
    rate_1=input(text_rate)
    pay=0
    advise=" "
    def is_number(s):
      try:
        float(s)
        return True
      except ValueError:
        return False;
      
    if  is_number(hour_1)==True and is_number(rate_1)==True:
        hour_1=float(hour_1)
        rate_1=float(rate_1)
        h=hour_1
        r=rate_1
       
        if h<=40 :
            pay=h*r
        else:
            pay=(40*r)+(h-40)*(1+(1/2))*r 
    elif  is_number(hour_1)==False :
            try:
                hour_1 =input("Enter Hours: \n")
                if is_number(hour_1)==True:
                    try:
                      hour_1=float(hour_1)
                      if is_number(rate_1)==True:
                          rate_1=float(rate_1)
                          h=hour_1
                          r=rate_1
                          if h<=40 :
                              pay=h*r
                          else:
                              pay=(40*r)+(h-40)*(1+(1/2))*r
                    except:
                       advise="introduce a valid value for rate"
                       return advise
            except:
                advise="introduce a valid value for hour"
                return advise
                
    elif is_number(rate_1)==False :
            try:
                rate_1 = input("Enter rate: \n")
                if is_number(rate_1)==True:
                    try:
                      rate_1=float(rate_1)
                      r=rate_1
                      if is_number(hour_1)==True:
                          if h<=40 :
                              pay=h*r
                          else:
                              pay=(40*r)+(h-40)*(1+(1/2))*r
                    except:
                        advise="introduce a valid value for hour" 
                        return advise              
            except:
                advise="introduce a valid value for rate"  
                return  advise        
    return pay;       
            
    
    
                            
value=computepay(10,5) 
print("Pay",value)                 
                
#hour_1=float(input("Enter the hours \n"))

a=10.5   
a.isdigit()                 

#text='introduzca su num \n'
#puntaje=input(text)            
#if type(puntaje)==float:
#    print("si") 
#else:
#    print("no")         
            
#text='introduzca su num \n'
#puntaje=input(text)            
#if ==float:
#    print("si") 
#else:
#    print("no")   
    
    
#type(puntaje)        
            
            
             
            
        
        
  
    


