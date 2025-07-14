#strings are immutable
a="FAIZAN"
# print(a)
# print(type(a))
# # as you see this is string 
# # string slicing
# print(len(a)) #knowing length of a stirng 
# print(a[1:5]) #indexing [ind_start : ind_end]
b="hey iam Fyzan"
# print(len(b))
# print(b[1:10:2]) #slicing with skip values[start:end:skipvalues] 
# print(a[-5]) #negative slicing


#string methods
print(a.endswith("AN")) #case sensitive 
print(a.startswith("FAI")) #case sensitive 
print(a.lower()) #case sensitive 

print(b.count("a"))  #count string 
print(a.count("A"))  #count string
print(a.replace("FAI","SAI")) #replace ("old word","new word")
print(a.replace("FAIZAN","FYZAN")) #replace ("old word","new word")
print(b.find("iam")) #find method


#escape sequence
print("HEY MY NAME IS\t\'SYEDFAIZAN\'")
print("HEY MY NAME IS\v\'SYEDFAIZAN\'")

# \t --> give extra space
# \n --> new line
# \"  \" --> for using double quote
# \'  \' --> for using single quote
