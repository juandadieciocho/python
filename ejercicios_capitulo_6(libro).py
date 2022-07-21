# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:19:48 2021

@author: juanc
"""

palabra_1 ='banana'
def contador_palabras(palabra):
    palabra=str(palabra)    
    contador = 0
    for letra in palabra:
        if letra == 'a':
            contador = contador + 1
        else: 
            contador=contador
    return(contador)

contador_palabras('palabra_1')

#startswith:empieza con 
palabra_1.startswith('a')
#encontrar cadena dentro de cadenas
palabra_1.find('a')
#minusculas
palabra_2=palabra_1.lower()
palabra_2
#mayusculas
palabra_3=palabra_1.upper()
#contar
palabra_1.count('a'[:])



#str.capitalize()
#Return a copy of the string with its first character capitalized and the rest lowercased.

#Changed in version 3.8: The first character is now put into titlecase 
#rather than uppercase. This means that characters like digraphs will 
#only have their first letter capitalized, instead of the full character.

#str.casefold()
#Return a casefolded copy of the string. 
#Casefolded strings may be used for caseless matching.

#Casefolding is similar to lowercasing but more aggressive 
#because it is intended to remove all case distinctions in a string. 
#For example, the German lowercase letter 'ß' is equivalent to "ss". 
#Since it is already lowercase, lower() would do nothing to 'ß'; 
#casefold() converts it to "ss".

#The casefolding algorithm is described in section 3.13 of the Unicode Standard.

#New in version 3.3.

#str.center(width[, fillchar])
#Return centered in a string of length width. 
#Padding is done using the specified fillchar (default is an ASCII space).
#The original string is returned if width is less than or equal to len(s).

#str.count(sub[, start[, end]])
#Return the number of non-overlapping occurrences of substring 
#sub in the range [start, end]. Optional arguments start and end
# are interpreted as in slice notation.

#str.encode(encoding="utf-8", errors="strict")
#Return an encoded version of the string as a bytes object. 
#Default encoding is 'utf-8'. errors may be given to set a different
# error handling scheme. The default for errors is 'strict', meaning
# that encoding errors raise a UnicodeError. Other possible values are
# 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any 
#other name registered via codecs.register_error(), see section Error 
#Handlers. For a list of possible encodings, see section Standard Encodings.

#By default, the errors argument is not checked for best performances,
# but only used at the first encoding error. Enable the Python Development Mode
#, or use a debug build to check errors.

#Changed in version 3.1: Support for keyword arguments added.

#Changed in version 3.9: The errors is now checked in development 
#mode and in debug mode.

#str.endswith(suffix[, start[, end]])
#Return True if the string ends with the specified suffix, 
#otherwise return False. suffix can also be a tuple of suffixes to look 
#for. With optional start, test beginning at that position. With optional end,
# stop comparing at that position.

#str.expandtabs(tabsize=8)
#Return a copy of the string where all tab characters are replaced
#by one or more spaces, depending on the current column and the given tab size.
# Tab positions occur every tabsize characters (default is 8, 
#giving tab positions at columns 0, 8, 16 and so on). To expand the string,
# the current column is set to zero and the string is examined character 
#by character. If the character is a tab (\t), one or more space characters 
#are inserted in the result until the current column is equal to the next 
#tab position. (The tab character itself is not copied.) If the character 
#is a newline (\n) or return (\r), it is copied and the current column 
#is reset to zero. Any other character is copied unchanged and the current
# column is incremented by one regardless of how the character is represented 
#when printed.

#str.find(sub[, start[, end]])
#Return the lowest index in the string where substring 
#sub is found within the slice s[start:end]. Optional 
#arguments start and end are interpreted as in slice notation. 
#Return -1 if sub is not found.

#str.index(sub[, start[, end]])
#Like find(), but raise ValueError when the substring is not found.

#str.isalnum()
#Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().

#str.isalpha()
#Return True if all characters in the string are alphabetic and there is at least one character, False otherwise. Alphabetic characters are those characters defined in the Unicode character database as “Letter”, i.e., those with general category property being one of “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”. Note that this is different from the “Alphabetic” property defined in the Unicode Standard.

#str.isascii()
#Return True if the string is empty or all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F.

#New in version 3.7.

#str.isdecimal()
#Return True if all characters in the string are decimal characters and there is at least one character, False otherwise. Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category “Nd”.

#str.isdigit()
#Return True if all characters in the string are digits and there is at least one character, False otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

#str.isidentifier()
#Return True if the string is a valid identifier according to the language definition, section Identifiers and keywords.
#para mas consultar
#https://docs.python.org/3/library/stdtypes.html#string-methods
