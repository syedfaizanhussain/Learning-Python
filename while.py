#WHILE LOOp
'''
The condition is checked first.if its evaluates to true the body of loop is executed otherwise not.
If the loop is entered , the process of [condition check or execution] is continued until the condition becomes false.
If the condition never become false, then loop keep executed.
'''

'''
syntax : 
while(condition):
        statement
        increment
'''
#wap to print 1-50 using while loop.
'''How It Works:
(1)It starts by setting i = 1.

(2)Then it enters a while loop that runs as long as i is less than 51.

(3)Inside the loop:

(4)It prints the current value of i.

(5)Then increases i by 1 using i += 1.

(6)Once i becomes 51, the loop condition i < 51 becomes false, so the loop stops.
'''
# i=1                    
# while(i<51):
#     print(i)
#     i+=1

#wap to print content of a list using while loop
a=["syed","faizan","hussain",20,"male","IT-Student"]
i=0

while(i<len(a)):
    print(a[i])
    i+=1
    # if i==3:                #break method just ignore it! this lesson will come in future !
    #     break
else:                       #else also can be used in while loop!
    print("loops is finished!")

