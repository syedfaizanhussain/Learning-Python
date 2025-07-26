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

#2. the game()func.. in a program lets a user play and returns the score as  an integer. you need to read a file 'Hi-Score.txt' which is either blank or contains the  previous Hi-Score. you need to write a program to update the Hi-Score whenever the game() fu.. breaks the Hi-score.
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