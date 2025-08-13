'''INHERITANCE : Inheritance is a feature in object-oriented programming where a new class (called a child or subclass) inherits properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This helps to reuse code and create a hierarchy of related classes.


TYPES : 
(1)- single
(2)- multiple
(3)- multilevel



-->Single Inheritance
A subclass inherits from one parent class.
Example: Class B inherits from Class A.

-->Multiple Inheritance
A subclass inherits from more than one parent class.
Example: Class C inherits from Class A and Class B.

-->Multilevel Inheritance
A subclass inherits from a class which is itself a subclass of another class.
Example: Class C inherits from Class B, which inherits from Class A.
'''
# #single - A subclass inherits from one parent class.
class emp():
    lang = "java"
    def d(self):
        print(f"the name : {self.name} and age : {self.age}")
    
class programmer(emp):
    lang = "py"
    def salary(self):
        print(f"salary is {self.salary}")
        
a=emp()
a.name ="titu"
a.age =23 
b=programmer()
a.lang = "c++"
print(a.lang,b.lang)
b.salary = 23445555
print(a.name ,b.salary)


# multiple - A subclass inherits from more than one parent class.
class empl():
    age = 23
    name = "default"
    def emp(self):
        print(f"the name is {self.name} and age is {self.age}")
        
    
class detail():
    def detai(self,addres,salary):
        self.addres= addres
        self.salary = salary
        print(f"the adres is {self.addres} and salary is {self.salary}")
        
        
class empinfo(empl,detail):
    def getinfo(self):
        print("the details of employees are : ")
        
    def runall(self):
        self.emp()
        self.detai("hyd",123)
        
        

d=empinfo()

d.runall()
# we calling all methods from one class



#multilevel - A subclass inherits from a class which is itself a subclass of another class.
class country:
    coun = "india"

class area(country):
    area = "masab"

class home(area):
    home ="house"
    

a=country()
# print(a.coun, a.area )   #it will throw an error !
print(a.coun) #it will only give its class attribute! if we writinf or access like (a.home() then we can access a.area name also because the last class is inherists from class which is inherit from another class! )
a=area()
print(a.coun, a.area )
a=home()
print(a.coun, a.area ,a.home)



