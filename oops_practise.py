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
class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        print(f"Train '{self.name}' initialized with {self.seats} seats at ₹{self.fare} per ticket.")
    
    def book_ticket(self, tickets):
        if tickets <= 0:
            print("Please enter a valid number of tickets to book.")
        elif tickets > self.seats:
            print(f"Only {self.seats} seat(s) available. Cannot book {tickets} ticket(s).")
        else:
            self.seats -= tickets
            total_cost = tickets * self.fare
            print(f"{tickets} ticket(s) booked successfully! Total cost: ₹{total_cost}")
    
    def get_status(self):
        print(f"Seats available: {self.seats}")
    
    def get_fare_info(self):
        print(f"Fare per ticket: ₹{self.fare}")


# Example Usage
train1 = Train("Rajdhani Express", 50, 1500)
train1.get_status()
train1.get_fare_info()
train1.book_ticket(3)
train1.get_status()
train1.book_ticket(48)
train1.get_status()
train1.book_ticket(1)  # This should now fail (no seats left)
