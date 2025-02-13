num2=4               #conditional statements if and else
if num2<0:
    print('negative')  # identation is must after if and else condition
else:
       if num2==0:          #  these   are nested conditional statements 
             print('zero')
       else:      
           print('postive')    
print('combination positive and negative are  called integers ')
str1=''
if len(str1)>=9:
     print('9')
else:
       if len(str1)<=0:
         print('empty string')
       else:
            print('lenght between 0-9')
# else if -elif
num1=0
if num1>0:
     print('positive')
elif num1<0:
     print('negative')
else:
     print('enter your name')
# current bill
current_units=int(input('enter no. of units'))
if current_units>=0 and current_units<=100:
     if current_units<0:
          print('invalid')
     else:
        print('no.of units *50rupees')

else:
      if current_units>=101 and current_units<=200:
           print('no. of units * 100rupees')
      else:
           if current_units>=201 and current_units<=300:
                print('no. of units * 150 rupees ')
           else:
                 if current_units==300:
                      print('no. of units * 150 rupees ')
                 
        
     
     

