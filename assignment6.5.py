# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:45:11 2021

@author: juanc
"""
#6.5 Write code using find() and string slicing 
#(see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
position=text.find('0.8475')
print(float(text[position:]))