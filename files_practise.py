#1. wap to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'
#writing mode
poem=open("poems.txt","w")
p1=poem.write("""Twinkle, twinkle, little star,
    How I wonder what you are!
    Up above the world so high,
    Like a diamond in the sky.""")
poem.close() 
#now reading 
reading=open("poems.txt","r")
r1=reading.read()
if "twinkle" in r1:
    print("The word is exists in the poem file!")
else:
    print("Not exists!")
reading.close()
#use with 

# #2. the game()func.. in a program lets a user play and returns the score as  an integer. you need to read a file 'Hi-Score.txt' which is either blank or contains the  previous Hi-Score. you need to write a program to update the Hi-Score whenever the game() fu.. breaks the Hi-score.
import random

def game():
    print("You Are Playing The game!")
    score = random.randint(1,100)
    # print(f"Highest Score {score}")
    # return score
    with open("highscore.txt","r") as f1:
        highscore = f1.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your Score : {score}")
    if(score > highscore):
        with open("highscore.txt","w") as f1:
            f1.write(str(score))
    return score

game()



#3. tables multiplication of 2 -20 and it should be in each file 
def generatetable(n):
    table=""
    for i in range(1,11):
        table+= f"{n} x {i} = {n * i}\n"

    with open(f"Tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generatetable(i)
# it automate the task.


#4. a file contain a word "DONKEY" multiple times . you need to wap which replace this word with ##### by updating same file.
word = "Donkey"
with open("file.txt","r") as f:
    content=f.read()

updated_content=content.replace(word,"#####")
with open("file.txt","w") as f:
    f.write(updated_content)



#5.do 4problem with some more words which is in lists 
words=["donkey","bad","stupid","animal"]
with open("file.txt","r") as f:
    content= f.read()
for word in words:
    content=content.replace(word,"#"* len(word))
with open("file.txt","w") as f:
    f.write(content)

#6. wap to mine a log file and find out whether it contains "python"
with open("log.txt","r") as f:
    content = f.read()

if ("python" in content):
    print("Python Word exists !")
else:
    print("Python Word  not exists !")
#7. wap to find out the line number where python is present from ques 6..
with open("log.txt","r") as f1:
    lines=f1.readlines()
lineno=1
for line in lines:
    if("python" in line):
        print(f"Python Word Exists! line no : {lineno}")
        break
    lineno +=1
else:
    print("No python Word Exists!")


#8.wap to make a copy of a text file"this.txt
with open("this.txt") as cop:
    content=cop.read()

with open("this_copy.txt","w") as cop:
    cop.write(content)


#9.wap to find out whether a file is identical & matches the content of another file!

with open("this.txt") as f3:
    content = f3.read()

with open("log.txt") as f3:
    content2= f3.read()

if(content == content2):
    print("Same!")
else:
    print("not same Content !")


#10. wap to wipeout the content of a file using python


with open("wiped.txt","w") as w:
    w.write("")



#11. wap to rename a file to "renamed_by_python.txt"
with open("renamefile.txt","r") as f5:
    content = f5.read()

with open("rename_by_python.txt","w") as f5:
    f5.write(content)  #we need to install os module to do this but as now we just created another file by 'rename_by_python.txt' name and copies the content from 'renamefile.txt' 
'''
import os

# Rename a file from old name to new name
os.rename("old_file.txt", "new_file.txt")

'''