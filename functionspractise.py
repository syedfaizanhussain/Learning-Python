#1.wap using functions to find greatest number of three number .
def big_num(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b 
    else:
        return c
    
a=int(input("Enter a: "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
print(f"The Greatest Number among Three Numbers is {big_num(a,b,c)}")

#2. wap using fun() to convert fehrenheit  to celsuis.
#formula --> c=5(f-32)/9
def Fah_cel(f):
    return 5*(f-32)/9

f=int(input("Enter temperature : "))   #Round the number to 2 decimal places(round(number, digits)
print(f"fahrehheit {f} to celsius {round(Fah_cel(f),2)}")

#3. how do you prevent a python print() function to print a new line at the end.
print("Hello ",end="")
print("Faizan")

#4.write a recursive fun() to calcuate the sum of first n natural numbers.
'''
for recursive you always have to do like thiss. 
sum(1)=1
sum(2)=1 + 2 
sum(3)=1 + 2 + 3
sum(4)=1 + 2 + 3 + 4 
sum(5)=1 + 2 + 3 + 4 + 5
sum(n)=1 + 2 + 3 + 4 + 5.....(n-1) + n
sum(n) = sum(n-1) + n

'''
def sum(a):
    if a==1 : 
        return 1
    else:
       return sum(a-1) + a    # this will be execuitng only we have to add bade case also. so it willbe stop at a specific number ( as we have to stop it on 1 because sum(1) is 1 only)

a=int(input("Enter Number : "))
print(f"The sum of {a} is {sum(a)}")



