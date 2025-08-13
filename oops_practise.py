# #1. create a class programmer for storing information of few programmers working at microsoft
class programmer:
    company = "microsoft"
    def __init__(self,name,age,gender,salary,address):
        self.name = name 
        self.age= age
        self.gender = gender
        self.salary =salary
        self.address=address
        print(f'''                    #we can write like this also ad like below aslo !
              The Name is {name}.
              The Age is {age}.
              The Gender is {gender}.
              The Salary is {salary}.
              The Address is {address}.
              ''')
        
d=programmer("Hussain",23,"Male",120000,"VNC")
print(d.name,d.address,d.age,d.company,d.gender)
        
        


#2 write a class calculator capable of finding square,cube,square root of a number!
from math import sqrt
class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"The square is {self.n ** 2}")
        
    def cube(self):
        print(f"The Cube is {self.n ** 3}")
    
    def squareroot(self):
        print(f"The square Root is {sqrt(self.n)}")


a=calculator(int(input("Enter number : ")))
a.square()
a.cube()
a.squareroot()


#3. create a class attribute a , create an object from it and set a directly using object.a = o does this chnage the class attribute !

class attribute:
    a="yaba"
    b="yafai"
    
change=attribute()
change.a="o"
change.b=23

print(change.a)
print(change.b)
print(attribute.a)   
# class attribute is not changed but an instance attribute is added    
    
#4. add a static method in problem 2, to greet the user with hello !
from math import sqrt
class calculator:
        
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"The square is {self.n ** 2}")
        
    def cube(self):
        print(f"The Cube is {self.n ** 3}")
    
    def squareroot(self):
        print(f"The square Root is {sqrt(self.n)}")

    @staticmethod
    def greet():
        print("HELLO CODER!!")

a=calculator(int(input("Enter number : ")))
a.greet()
a.square()
a.cube()
a.squareroot()



#5. write a class train which has methods to book a ticket.get status (no of seats) and get fare information of train running under indian railways
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        self.fro = None   # Initialize start station attribute
        self.to = None    # Initialize destination station attribute
        self.seats = 10   # Example total seats available

    def bookticket(self, fro, to):
        if self.seats > 0:
            self.fro = fro
            self.to = to
            self.seats -= 1
            print(f"Ticket booked in train no: {self.trainNo} from {fro} to {to}.")
            print(f"Seats remaining: {self.seats}")
        else:
            print("Sorry, no seats available.")

    def status(self):
        if self.fro and self.to:
            print(f"Train no: {self.trainNo} is booked from {self.fro} to {self.to}.")
            print(f"Seats available: {self.seats}")
        else:
            print(f"No tickets booked yet on train no: {self.trainNo}.")

    def fare(self, fro, to):
        # Random fare between 34 and 2344 for demonstration
        fare_amount = randint(34, 2344)
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is ₹{fare_amount}.")

# Testing the class
a = Train(123)
a.bookticket("Mumbai", "Goa")
a.status()
a.fare("Mumbai", "Goa")
