'''list1=[1,2,3,4,5,6,7,8,9]
list2=['mad ',1,5,7]
for j in list1:
    if j%2==0:
        list2.append(j)
print(list2)'''
#task2
'''list1=[1,2,3,4,5]
even_sum=0
odd_sum=0
for i in list1:
    if i%2==0:
        even_sum+=i
        
    
        
    else:
        
        odd_sum+=i
print(even_sum)
print(odd_sum)'''
        
list1=[1,2,3,4,5]
esum=0
osum=0
for i in list1:
    if i%2!=0:
     osum+=i
    else:
     esum+=i
print(esum)
print(osum) 
list2=[2038,3057,4567,9807,23678,]
empty_list=[]
for i in list2:
    if i%2==0:
        print(i)
        empty_list.append(i)

empty_list.append('maddineni')
print(empty_list)   
for i in list2:
    if i%2!=0:
        empty_list.append(i)
print(empty_list)
list3=['abcd','efghi','ghifh','dskf','sdddfsdf']

print(set(list3[0]))
set1=list3[0]
print(set1)
a=set1[0]
print(set(list3[1]))
set2=list3[1]
print(set2)
b=set2[0]
print(set(list3[2]))
set3=list3[2]
print(set3)
c=set3[0]
print(set(list3[3]))
set4=list3[3]
print(set4)
d=set4[0]
print(set(list3[4]))
set5=list3[4]
print(set5)
e=set5[0]
print(a+b+c+d+e)
_name='python'
print(_name[6:0:-1])
print(_name[-1:-6:-1])






        
