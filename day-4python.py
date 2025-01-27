Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(list(range(0,100)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> list=[1,2,3,4,5,6,7,8,9,10]
>>> print(list(range()))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(list(range()))
TypeError: range expected at least 1 argument, got 0
>>> print(range(list))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(range(list))
TypeError: 'list' object cannot be interpreted as an integer
>>> print(range(0,100))
range(0, 100)
>>> print(list(range(0,1000)))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(list(range(0,1000)))
TypeError: 'list' object is not callable
>>> print(list(range(0,100)))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(list(range(0,100)))
TypeError: 'list' object is not callable
