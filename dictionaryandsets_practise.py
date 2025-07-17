#1.wap to create a dic of hindi words with values as there English translation.provide user withan aption to look it up.
# translation={
#     "kela":"banana",
#     "aam":"mango",
#     "sep":"apple",
#     "anaar":"pomegranate"
# }

# print(translation[input("Enter hindi word to for english : ")]) #wrong logic cause if the  input key is not exists in dictionary then it will raise an error.
# w=input("Enter hindi to english : ")
# print(translation.get(w))  # it willnot throw the error if the value  is not there in dic.


#2. wap to input eight numbers from the user and display all the unique numbers(once).
# num_8=set()

# (num_8.add(int(input("Enter 1 number: "))))
# (num_8.add(int(input("Enter 2 number: "))))
# (num_8.add(int(input("Enter 3 number: "))))
# (num_8.add(int(input("Enter 4 number: "))))
# (num_8.add(int(input("Enter 5 number: "))))
# (num_8.add(int(input("Enter 6 number: "))))
# (num_8.add(int(input("Enter 7 number: "))))
# (num_8.add(int(input("Enter 8 number: "))))
# print(f"The uniques values are {num_8}")



#3. can we have a set with 18(int) and'18(str) as a value in it ? 
# s={18,'18'} #--> as18 is integer and '18' is act as string so both are totally different.
# print(s)



# #4.what will be len of following set s:
# s=set()
# s.add(20)  #the len will be 2 but the values is 3right! so 20==20.0 it act as same datatype.
# s.add(20.0)
# s.add('20')
# print(len(s))

#5. create an empty dic. allow 4friends to enter their fav language as values and use key as their names.assume that the names are unique.
# fav={}
# key=input("Enter your name :  ")
# value=input("Enter fav lang :  ")
# fav[key]=value

# key=input("Enter your name :  ")
# value=input("Enter fav lang :  ")
# fav[key]=value

# key=input("Enter your name :  ")
# value=input("Enter fav lang :  ")
# fav[key]=value

# key=input("Enter your name :  ")
# value=input("Enter fav lang :  ")
# fav[key]=value
# print(fav)



#6.can you change the values inside a list which is contained in set s? 
change={8,7,12,"fyzan",[1,2]}  #we cant change infact lists cannot be their in sets because there are immutable!


#7.