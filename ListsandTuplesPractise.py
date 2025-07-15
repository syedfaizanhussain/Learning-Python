#1. wap to store seven fruits in a list entered by user.
fruits_7=[]

f1=fruits_7.append(input("Enter fruit Name : "))
f2=fruits_7.append(input("Enter fruit Name : "))
f3=fruits_7.append(input("Enter fruit Name : "))
f4=fruits_7.append(input("Enter fruit Name : "))
f5=fruits_7.append(input("Enter fruit Name : "))
f6=fruits_7.append(input("Enter fruit Name : "))
f7=fruits_7.append(input("Enter fruit Name : "))
print(fruits_7)


#2. wap to accept marks of 6students and display them in a sorted manner.

#in this we using SPLIT() -->The split() method breaks a string into parts and puts them in a list.
marks=[]

m1=marks.append(input("Enter s1 marks : "))  #this is method 1 and easiest using APPEND()
m2=marks.append(input("Enter s2 marks : "))
m3=marks.append(input("Enter s3 marks : "))
m4=marks.append(input("Enter s4 marks : "))
m5=marks.append(input("Enter s5 marks : "))
m6=marks.append(input("Enter s6 marks : "))
marks.sort()
print(marks)


marks.extend(input("Enter 6Students Marks : ")).split()  #this is method2 and hard using EXTEND().
marks.sort()
print(marks) 


#3.wap to sum a list with 4numbers.
list=[12,34,2,8]
s=sum(list)   #used SUM() to sum.
total=list[0]+list[1]+list[2]+list[3]  # manual method using INDEX.
print(f"The sum of 4values from list is  {s}")
print(f"The sum of 4values from list is  {total}")

m=(1,3,4)  #using SUM() with tuples!.
t=sum(m)
print(t)

#4.wap to count the numbers of '0' in following tuples
a=(7,0,8,0,0,9)
print(a.count(0))