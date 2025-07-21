'''
RECURSION() -->
  Recursion is when a function calls itself to solve a smaller part of the same problem.

-->Imagine you're opening a box, and inside that box is another smaller box, and inside that… another one… until the final box has nothing inside.

  To solve this:

  You open the first box.

  Then open the next.

  Keep going until you find the empty box (base case).

  Then start closing them one by one — last-in, first-out (LIFO).

  That’s how recursion works — it keeps calling itself until a stopping condition is met, then unwinds.


EXAMPLE factorail of 5 
fac(1)= 1
fac(2)= 2 x 1
fac(3)= 3 x 2 x 1
fac(4)= 4 x 3 x 2 x 1
fac(5)=5 x 4 x 3 x 2 x 1
fac(n)=n x (n-1) x .. . ..X 3 x 2 x 1    #fac(n-1)= (n-1) x ......x3x2x1

fac(n) = n x fac(n-1)


  '''
#factorail of a number !
'''
fac(0)=1
fac(1)=1
fac(2)=2
.
.
'''
def fac(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * fac(n-1)
num = int(input("Enter A Number To Get its factorai : "))
result=fac()
print(f"The Factorail of {num} is {result}")


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

num = int(input("Enter number of terms: "))
for i in range(num):
    print(fib(i), end=" ")

