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