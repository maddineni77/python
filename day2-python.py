Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str='shear khan okkadini kadhu'
print(str[0:])
shear khan okkadini kadhu
print(str[0:100])
shear khan okkadini kadhu
print(len(str))
25
print(str[0:25])
shear khan okkadini kadhu
print(str[25])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(str[25])
IndexError: string index out of range
print(str[24])
u
print(str[0:24:-1])

print(str[24:0:-1])
uhdak inidakko nahk raeh
print(str[-1:-25])

print(str[-25:-1])
shear khan okkadini kadh
print(str[-25:-1:-1])

>>> print(str[-1:-25:-1)
...       
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(str[-1:-25:-1])
...       
uhdak inidakko nahk raeh
>>> #immutability-> we cannot change the characters in the string by indexing
...       
>>> str[10]='n'
...       
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str[10]='n'
TypeError: 'str' object does not support item assignment
>>> # strings in python are immutable
...       
>>> str1='string'
...       
>>> str2='string2'
...       
>>> str3='string3'
...       
>>> str1='string'
...       
>>> str2='string'
...       
>>> str3='string'
...       
>>> print(id(str1))
...       
140730808041616
>>> print(id (str2))
...       
140730808041616
>>> print(id(str3))
...       
140730808041616
>>> # id -> function gives the address of the memory block
...       
