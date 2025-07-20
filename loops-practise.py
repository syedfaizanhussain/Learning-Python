# 1.wap to print multiplication table of given no.
T=input("Enter A Number to Get Its Multiplication Table: ")
for numbers in range(1,11):
    print(f"{T} x {numbers} = {T*numbers}")


# 2. wap to greet all the person names stored in a list 'l' and which starts with S.
l=["Harry","Soham","Sachin","Rahul"]
for name in l:
    if (name.lower().startswith("s")):
         print(f"{name} GOOD MORNINGSIR!")


# 3.multiplication using whileLOOP()
a=int(input("Enter A Number to Get Its Multiplication Table: "))
i=1
while(i<11):
    print(f"{a} x {i} = {a*i}")
    i=i+1
        

# 4.wap to find whether a number is prime or not.
# prime= number should divisible by it self or by 1 only!
prime=int(input("Enter number : "))
for i in range(2,prime):
    if prime%i==0:
        print("NT PRIME!")
        break
    else:
        print("PRIME!")
        break



# 5.wap to find the sum of first n natural numbers using while.
n=int(input("enter number : "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(f"the sum of n natural numbers is {sum}")

add=0
for i in range(1,n+1):  #using forloop()
    add=add+i
print(f"the sum of n natural numbers is {add}")


# 6.wap to calculate the factorail of given number usingloops
fac=int(input("Enter number : "))
result=1
for i in range(1,fac+1):
    result*=i
print(result)

#using While loop()
i=1
r=1
while i<=fac:
    r*=i
    i+=1
print(r)

#7. STAR printing.
'''
wap to print the following star pattern.
  *
 ***
*****  
Print this star pattern where n=3
'''
n=int(input("Enter no : "))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print(" ")

#8.
'''
wap to print the following star pattern.
***
***
***
'''
w=3
for i in range(1,w+1):
    print("*"*3,end="")
    print(" ")

#9.
'''
wap to print the following star pattern.
*
**
*** m=3
'''
m=int(input("Enter number: "))
for i in range(1,m+1):
    print("*" * i,end="")
    print("")


#10.
'''
wap to print the following star pattern.
***
**
* m=3
'''
m=int(input("Enter number: "))
for i in range(m,0,-1):
    print("*" * i,end="" )
    print("")


##11.
'''
wap to print the following star pattern.
***
* *
***
'''
a=int(input("Enter number : "))
for i in range(1,a+1):
    if(i==1 or i==a):
        print("*" * a)
    else:
        print("*",end="")
        print(" " *(a-2),end="")
        print("*",end="")
        print("")


#12.1.wap to print multiplication table of given no. in reverse! using for loops
rev=int(input("Enter number : "))
for i in range(10,0,-1):
    print(f"{rev} * {i} = {rev * i}")
