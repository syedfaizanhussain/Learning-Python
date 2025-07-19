'''
FORLOOP --> used to iterate through a sequence like lists,tuples, or strings. It repeats a block of code for each item in the sequence.

Syntax:
for variable in range(start,stop):
            #statement

range() --> range() is a built-in Python function used to generate a sequence of numbers.
range(stop)              for i in range(5):        # 0 to 4

range(start,stop)        for i in range(2, 6):     # 2 to 5

range(start,stop,step)   for i in range(1, 10, 2): # 1, 3, 5, 7, 9

'''
 

l=[1,2,4]
for items in l:
    print(items)  #if i print items(varaible) it will print values of list in sequence. 



l=[1,2,4]
for items in l:
    print(l)      #if i print l(list) it will print all list len(list) times.

tup=("fyxan",18,12,34,56,76,23,45,2)  #loops using with tuples.
for i in range(0,9,2):
    print(tup[i])


string = "FYZAN_i6"
for name in range(0,8,2):    #loops using with string (range(start,stop,step))!
    print(string[name])




for i in range(0,51 ,5):   
    print(i)
'''How It Works:
This loop starts from 0, then adds 5 each time, and stops before 51.
It does not count 5 times from each number, it just adds 5 to the previous number.
'''

Dm="hey! call me back"
for msg in range(0,11):    #for loops can also use else like while loop!
    print(Dm)        #Prints the full message each time
    # print(Dm[msg])   #print Dm like Charcters.
else:
    print("Dm send!")


