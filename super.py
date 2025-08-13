class country:
    coun = "india"
    def __init__(self):
        print("This is from country !")

class area(country):
    area = "masab"
    def __init__(self):
        super().__init__()
        print("This is from area !")

class home(area):
    home ="house"
    def __init__(self):
        super().__init__()
        print("This is from home  !")
    

# a=country()
# print(a.coun) 

# a=area()
# print(a.coun, a.area )

a=home()

print(a.coun, a.area ,a.home)






# examplee :   

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
    def getinfo(self,addres,salary):
        super().emp()       #using super!
        super().detai(addres,salary)
        print("the details of employees are : ")
    
        
        

d=empinfo()
d.getinfo("hyd",123)  