a=(1,23,14,"hussain",2,6,3,4,"fyzan",1,2,14) # tuple can store elements of different data type

b=("syed","aiengineer",13,1)

c=(2,1,2)
d=(2,) #to make tuple we have to give comus after one value ! if not it will be considered as integer
print(type(d)) #tuple are immutable.

print(type(a)) #tuple are immutable.

print(a)

print(a[0])  #indexing

print(a[0:3]) #slicing 


#tuples methods.
print(a.count(1))  #-->COUNT() use to count the element

print(a+b)  #-->CONCATENATED() use to add two tuples in one tuple

print(c*3) #--> REPETITION() use to multiple 

print(2 in a)  #-->MEMBERSHIP() use to check the element is there in tuple using IN

print("aiengineer" in b) #-->MEMBERSHIP() use to check the element is there in tuple using IN key

print(a.index(2)) #-->INDEX() it will tell the index values of element

print(b.index("aiengineer")) #-->INDEX() it will tell the index values of element

print(len(a))  #LEN() use just check the lenght of tuple or lists or strings its starts from 1 ot from 0
print(len(b))
print(len(c))
print(len(d))

x,y,z=c #--> UNPACKING() it just reassign the values not change the tuples
print(x)