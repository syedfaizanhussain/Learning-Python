a={1,2,3,3,4,4,7,5,"faizan"}
c={"harry",3,"faizan",4,5,7,0,9}  #SET is a collection of non-repetitive elements.
s={}   #this is empty dictionary not set
b=set() #this is empty set 
print(type(b))
print(type(a))
print(a)    #it is unordered


# #SET method()
print(a.add(0)) #ADD() --> use to add value in existing set.
# print(a)    #it is unordered

print(c.update(["hussain","syed",29,1,2]))#UPDATE() --> it will uadd multiple values.
# print(c)

print(a.discard(6))#DISCARD() --> use to remove the values if its not exists it will not give an error.
# print(a)
 
#SETS OPERATIONS.
print(a.difference(c))  #-->DIFFERENCE (it will print values which is in a set not in c set)

print(a.union(c))#-->UNIOn (it combine all values from both sets and remove the duplicates.)

print(a.intersection(c))#-->INTERECTION (it give commom values from both sets. and remove duplicate.)

print(a) 
print(c)
print(a.issubset(c)) #-->ISSUBSET (It checks if all elements of one set are present in another)

print(c.issuperset(a)) #-->ISSUBSET (It checks if all elements of one set are present in another)


print(len(a)) #--> LEN use toknow the length of sets.
print(len(b))
print(len(c))








