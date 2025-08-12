class Emp:
#     lang= "python"
#     age= 23
#     def getinfo(self):
#         print(f"the language is {self.lang} and Age is {self.age}\n")
#     @staticmethod
#     def greet():
#         print("HELLOOO  !!")
#     @staticmethod
#     def msg():
#         print("It was always Python")   
#     #dunder method
#     def __init__(self):
#         print("IM BAck~")
# faizan = Emp()
# faizan.lang="AI "
# faizan.getinfo()
# faizan.greet()
# faizan.msg()

#constructors

    def __init__(self,name,age,gender):
        self.name = name    
        self.age = age    
        self.gender = gender
        print(f"The Name is {name} and Age is {age} and the gender is {gender} ")    
        
x= Emp("aziz",23,"female")  
print(x.name,x.gender)  
