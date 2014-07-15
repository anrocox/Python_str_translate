#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

In python How to define a mapping table of characters for use in a string?

En python ¿Como definir una tabla de mapeo de caracteres para usar en un
string?
'''

#create a str
s = 'in addition to case folding'
print(s)

#generates a dict with translation table. The two arguments must be strings of
#equal length. Each character in first arg will be mapped to the character at
#the same position in the second arg.
d = str.maketrans('abcdef', 'uvwxyz')
print(d)

#generates a copy of 's' where all characters have been mapped through the
#map of the dictionary 'd'
s_new = s.translate(d)
print(s_new)

#the third argument defined the characters that are mapped to None.
d = str.maketrans('abcdef', 'uvwxyz', 'io')
print(d)

#characters mapped to None are deleted.
s_new = s.translate(d)
print(s_new)
