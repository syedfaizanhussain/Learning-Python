#FILE I/O 
'''
File I/O stands for File Input and Output.
It is used to read data from or write data to 
files stored on your computer using Python.
SYNTAX : 
        file = open("filename.txt", "mode of opening(read by default)")  #
        content = file.read()
        print(content)
        file.close()

        

Mode	         Meaning
'r'       -->	 Read (default mode)
'w'       -->	 Write (creates a new file or overwrites)
'a'       -->	 Append (adds data to end of file)
'r+'      -->	 Read and write both
'b'       -->	 Binary mode (used with other modes like 'rb', 'wb')
f.readline() --> read one full line at a time
'''

# #read()   #For reading the file
# text=open("text.txt","r")  
# reading=text.read()
# print(reading)
# text.close()
# #readlines() return data from files into Lists 
# file=open("text.txt")
# f1=file.readlines()
# print(f1,type(f1))
# file.close()

#write() Mode (create a new file or override)
# string="hey faizn"
# file=open("myfiles.txt","w")
# writing=file.write("this is nice!\n")
# writing=file.write("As u know my name is fyzan hahahaaa\n")# as u can seee in the file there is no msg which is in the "string" varaible.
# file.close()

#Append (adds data to end of file)
string = "hey faizn"
file=open("myfiles.txt","a")
appending=file.write(string)
appending=file.write("7330907967")

file.close()

