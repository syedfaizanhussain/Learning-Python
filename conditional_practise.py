#1.wap to find greatest of 4numbers entered by user.
a=int(input("enter number : "))
b=int(input("enter number : "))
c=int(input("enter number : "))
d=int(input("enter number : "))
if(a>=b and a>=c and a>=d):
    print("a is greatest among 4numbers")
elif(b>=c and b>=d and b>=a):
    print("b is greatest among 4numbers")
elif(c>=d and c>=a and c>=b):
    print("c is greatest among 4numbers")
else:
    print("d is greatest among 4numbers")


#2.wap to find out whether a student has passed or failed if it requires a total of 40% and atleat 33% in each subject to pass.assume 3subjects and take marks as an input from the user.
math=int(input("Enter marks : "))
python=int(input("Enter marks : "))
com=int(input("Enter marks : "))
total = ((math+python+com)/300)*100
if(math>=33 and python>=33 and com>=33 and total>=40):
    print("STUDENT HAS PASSED!")
else:
    print("STUDENT HAS FAILED!")


#3.A Spam comment is defined as a ttext containing following keywords 
# "Make a Lot of money","buy now","subscribe this","click this".wap to detect these spams
spam=input("enter comment : ")
if("make a lot of money" in spam.lower() or "buy now" in spam.lower() or "subscribe this"in spam.lower()):
    print("This is SPAM")
else:
    print("NOT SPAM ")


#4.wap to find whether a given username contains less than 10 characters or not .
user=input("Enter Username : ")
print(len(user))
if(len(user)<10):
    print("Your username length is less than 10")


#5.wap which finds out whether a given name is present in alist or not
s_names=[]
s_names.extend(input("Enter names : ").split())  # yo can also make a list and enter names in it manually!
lis=input("Enter Name : ")
if(lis in s_names):
    print("Name Found")
else:
    print("No Such Name!")


#6.wap to calculate the grade of a student from his marks from the following 
#90-100-> EX
# 80-90->A
# 70-80->B
# 60-70->C
# 50-60->D
#<50  ->F
marks=int(input("Enter marks : "))
if(marks>=90 and marks<=100):
    print("EX")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks>=50 and marks<60):
    print("D")
else:
    print("F")


#7.wap to find out whethera given post is talking about "faizan" or not .
post=input("Enter a post : ").lower()
if("faizan" in post):
    print("about faizan")
else:
    print("Not About faizan")