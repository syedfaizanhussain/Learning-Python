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

# #4.wap to count the numbers of '0' in following tuples
a=(7,0,8,0,0,9)
print(a.count(0))



#5.Store the names of 6 friends in a list. Display the 3rd and 5th friend's name using indexing.
names=[]
names.extend(input("Enter 6 Names : ").split())
print(names)
print(names[2])
print(names[4])


#6.Create a list with your birth year, current year, and calculate your age by subtracting the two values
bod=[2005,2025]
t=bod[1]-bod[0]
print(t)


#7.Make a list of 4 mobile brands. Replace the second brand with "iPhone" and print the updated list.
m=[]
m.extend(input("enter 4 mobile brands name: ").split())
print(m)
m[1]="iphone"
print(m)


#8.Create two tuples: one with your name, one with your age. Concatenate them and print the result.
name=("SYEDFAIZANHUSSAIN",)
age=(20,)
print(name+age)


#9.Create a tuple of 6 numbers. Use slicing to print only the last 3 values
slice=(6,2,8,1,9,4)
print(slice[3:7])


#10.Create a tuple with mixed data types (name, age, float). Print its type using type()
types=("syed",20,5.5)
print(type(types[0]))
print(type(types[1]))
print(type(types[2]))


#11.Make a list of 3 numbers, then multiply the entire list by 2. What happens? Print and understand.
mul=[2,3,4]
print(mul*2)
print(mul)


