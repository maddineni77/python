#for loop and while loop
'''for y in range(0,21):

    if y % 2==0:
        print(y)
    print(y*y)    
    
for y in range (0,21,2): # in the range it gives only multiples of 3
    print(y)
for y in range(1000,2000,84):
    print(y)
for y in range(1000,2000,84):
    if y%84==0:
        print(y)'''
#nested loop
# while loop 
y=0
while y <26:
    if y%2==0:
        print(y,'even')
        
    else:
        print(y,'odd')

    y+=5
'''num1=1
while num1<11:
    if num1!=5 and num1!=6:
        for num2 in range(0,31):
            print(num1,num2)
   
    num1+=1'''
num3=7
num3//=2
print(num3)
#break and continue these are jump statements ,these two are used loops
'''for i in range(0,10):
    if i!=5:
        print(i)
for i in range (0,10):
    if i==5:
      continue
    print(i)
for i  in range(0,10):
    if i==5 or i==6:
        continue
    print(i)'''
'''for cls1 in range (1,20):
    for roll in range (1,31):
        if cls1==5:
            continue
        print(cls1,roll)'''

'''num1=5
num2=10
if num2%10==0:
    num1=10
else:
    num1=8'''

'''time=12
str1='good' if time>10 else 'bad'
print('str1')'''
'''user_number=int(input('enter some number'))
if user_number%2!=0:
    print('odd')
else:
    print('even')
number1=int(input('enter some number'))
if number1%3==0 and number1%5==0:
    print(number1)
else :
    print('not a multiple of 3 and 5')'''
#largest number
num1=int(input('enter the first number'))
num2=int(input('enter second number'))
num3=int(input('enter thridnumber'))
if num1<num2:
    if num2<num3:
        pass
    else:
        print(num3)



