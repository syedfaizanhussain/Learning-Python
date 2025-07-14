list=["syed","faizan","hussain",19,"Boy"]  #lists are mutable (we can change elements)
print(list[3])   
list[3]=20
print(list[3])
#list can be indexing like 
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[1:4])  
print(list[-1])  
print(list[::-1]) #reversing with indexing


#lists methods (which not create a new list but chamge/update the old list)
list.append("Student")  #-->APPEND() use to add a element at end of list.
print(list)

list.reverse()  #-->REVERSE() use to reverse the list.
print(list)

list.remove(20)  #-->REMOVE() use to remove any element from list.
print(list)

list.pop(1)  #-->POP() use to delete element from list at index pop(index_number).
print(list)  

list.sort() #-->SORT() use to arrange list in ascending to desending.
print(list)

list.insert(4,"Male")  #-->INSERT() use to add an element in list  at a specific in index (Insert(inder_number,what to add)).
print(list)

list.extend(["Biker","coder","AI enginner"])  #-->EXTEND() most usefu to add multiple elements in list its same like append but add more at a time.
print(list)

b=list.copy() #-->COPY() use to copy the list.
print(b)

list.clear() #-->CLEAR() use to clear all list it make empty list
print(list)










