#FUNCTIONS --> 
'''A function is a block of code that performs a specific task.
It helps to reuse code and make programs modular and organized.
SYNTAX: 
       def function_name(parameters):
        # block of code
        return result  # (optional)
TYPES OF FUNCTIONS
(1) BUILT IN (print(),len(),range()..etc)
(2) USER DEFINED 
'''

#quick quiz
#function definition
def goodday():
    return "GOOD DAY!"
user=input("Enter Your Name : ")
print(user + goodday())#function call


#functions with arguments(int , string,boolean, float)
#example
def goodday(name,age,gender): #name is parameter (like a variable)
    print("GOODDAY , ")
    print(name)
    print(age)
    print(gender)
name=input("ENTER NAME : ")
age=input("ENTER AGE : ")
gender=input("ENTER GENDER : ")
goodday(name,age,gender)   #function call 
# goodday(age)   #function call 
# goodday(gender)   #function call 










def calculation(a,b):
    sum=a+b
    mul=a*b
    sub=a-b
    return sum,mul,sub

a = int(input("Enter Number : "))
b = int(input("Enter Number : "))
sum,sub,mul=calculation(a,b)   #funcction call
print(f"the sum of {a} and {b} is {sum}")
print(f"the sub of {a} and {b} is {sub}")
print(f"the mul of {a} and {b} is {mul}")



