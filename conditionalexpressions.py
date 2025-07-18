# CONDITINAL EXPRESSION: 
# It’s used when you want to choose one value based on a condition.
# syntax: 
# if : Executes a block of code only if the condition is True.
# elif : Checks another condition if the first if is False
# else:Executes if all above conditions are False.
age=int(input("Enter age : "))
if(age>=60):
    print("Your are Requested to Not to Drive ")
elif(age>18):
    print("Your are eligible for Driving")
else:
    print("Your are not eligible for Driving")




#wap to print yes when user the age entered by user is greater than or equa to 18
a=int(input("Enterr age : "))
if(a>=18):
    print("YES")


#RELATIONAL OPERATORS.(comparision operators)
#  used to evaluate conditions inside the if statements.
# == --> equals.
# >= --> greater than or equal to.
# <= --> lesser than or equal to


#LOGICAL OPERATORS.
# and --> true if both operands are True
# or --> true if atleast one operands is True
# not --> converts true to false and false to true.