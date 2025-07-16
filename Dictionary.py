marks={
    "Syed": 87,
    "faizan":39,      #IT IS DICTIONARY IS A COLLECTION OF KEY-VALUES PAIRS 
    "hussain":40,     #The keys cant be duplicated if then it will override that (hussain =40 --> hussain =49)
    "sai":89,        #it is mutable  #it is unordered
    "hussain":49
}
print(marks)
print(marks["faizan"])   #to access the value we need to use it key! we cant directly index.




#dictionary methods
student={
    "badsha":34,
    "rehmath":89,
    "ayan":66,
    "yaba":45,
    0:"harry"
}
student[0]="munna"  #update 

print(student)
print(student.items())  #ITEM() --> it will return dictionary as lists 

print(student.keys())  #KEYS() --> it will display all the keys.

print(student.values()) #VALUES() --> it will display all values.

print(student.update({"yaba":50,0:"zayn","badsha":100,"rehmath":99,"jawad":67}))  #UPDATE() --> used to update the  multiple values of keys in dictionary.
print(student)

student["yaba"]=51  #used to update single values.
print(student)

print(student.get("hafsa")) #GET() --> it returns the value of key if it is not exists in dictionary it will not raise an error (NONE).
# print(student["hafsa"])    #it also returns the value of key if it is not exists in dictionary it will raise an error.

print(student.pop("yaba"))  #POP()--> it will Removes and returns the value of the given key.
print(student)
 
print(student.popitem())  #POPITEM()--> it will Removes the last inserted key-value pair.

b=student.copy() #COPY()--> use to copy the dictionary in another variable.
print(student)
print(b)