'''#naming convention
#Snake Case:
Words are separated by underscores.
Used for variable names, function names, and module names.
Example: my_variable_name, calculate_average
#Camel Case:
First word is lowercase, subsequent words start with uppercase.
Not commonly used in Python, but sometimes seen in methods within classes.
Example: myVariableName, calculateAverage
#Pascal Case:
First word and subsequent words start with uppercase.
Used for class names.
Example: MyClassName, Person
'''
# there is no constants in pyhton
# conersion from one data type to another
float1=5.0
print(int(float1))
str1='maddineni'

str2=list(str1)
print(str2)
list1=[1,2,3,[1,2,3,'mad'],23]
str1=str(list1)
print(str1)
print(len(str1))
print(str1[30])
print(str1[31:0:-1])