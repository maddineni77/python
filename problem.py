'''def positive (num):
    if num>0:
      print('positive')
    elif num<0:
       print('negative')
    else:
       print('zero')

positive(12)
def even(num):
   if num%2==0:
      print('even')
   else:
      print('odd')
even(3)
def greatest(num1,num2):
   if num1>num2:
      print(num1)
   else:
      print(num2)
greatest(2,4)
def pass_fail(marks):
   if marks>40:
      print('pass')
   else:
      print('fail')
pass_fail(56)
#checking a character whether it is vowel or consonent
char=input('enter a single character').lower()
if len(char)!=1:
   print('entered invalid character')
else:
   if char in ['a','e','i','o','u','s']:
      print('vowels')
   elif char.isalpha():
      print('consonets')
   else:
      print('special characters')  '''
# implenting caluculator
user=input('enter the operation to perform').lower()
num1=10
num2=20
if user=='add' or user=='+':
   print(num1+num2)
elif user=='mul'or user=='*':
   print(num1*num2)
elif user=='div'or user=='/':
   if num2==0:
      print('division is not possible')
   else:
      print(num1/num2)
elif user=='sub'or user=='-':
    print(num1-num2)
else:
   print('you fool enter the correct operation')
#to check which month 
user=int(input('enter some number to check which month' ))
if user==1:
   print('january')
elif user==2:
   print('feb')
elif user==3:
   print('march')
elif user==4:
   print('april')
elif user==5:
   print('may')
elif user==4:
   print('june')
elif user==4:
   print('july')
elif user==4:
   print('aug')
elif user==4:
   print('sept')  
elif user==4:
   print('oct')
elif user==4:
   print('november')   
elif user==4:
   print('december')    
else:
   print('evadra nuvvu ')   
      
#leap year
user=int(input('enter some number ra abbai'))
arr=[user]
if len(arr)<3:
   if user%4==0:
      print('leap year ra abbai')
   else:
      print('not a leap year ')
elif len(arr)>=3:
   if user%400==0:
      print('leap year ra nayyana')
   else:
      print('leap kadhu ani chepana')


  
