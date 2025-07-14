#1. wap to display a user entered name followed by good afternoon using input()fun
a=input("Enter Your Name : ")
print(f"GOOD AFTERNOON  {a}") #f-string method
print("GOOD AFTERNOON ", a) #normal method(multiple args)
print("GOOD AFTERNOON "+ a) #another normal method(Concatenation)


#2.wap to detect double spaces in a string 
name="SYED  FAIZAN  HUSSAIN"
print(name.count("  "))   #by using count()--> tells how much double spaces are there in string.
print(name.find("  "))   #by using find()-->he show index if he finds one double space from starting only for one but cant for multiple double spaces.


#3. replace double spaces with single spaces of problem 2.
print(name.replace("  "," "))   #strings are immutable



#4. wap to format the following letters using escape sequence.

letter = "Dear Fyzan, this python course is nice. Thanks!"
print("Dear Fyzan,\n\tThis python course is nice.\n\tThanks!")  #\t--> extra space and \n --> new line


#5.Print the first and last character of any string
string="SyedHussain"
print(string[0])
print(string[-1])


#6.Replace all spaces in a sentence with dashes.
string="syed faizan huss ain"
print(string.replace(" ","-"))




