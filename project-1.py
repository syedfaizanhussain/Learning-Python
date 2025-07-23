'''
#PROJECT - 1 
Snake , Gun and Water ! :
            The Snake Water Gun game, a variation of Rock Paper Scissors, is played with three options: Snake, Water, and Gun. 
            Snake beats Water (snake drinks the water), Water beats Gun (water drowns the gun), and Gun beats Snake (gun shoots the snake). 
            Players simultaneously choose one of the three options. The winner is determined by comparing the choices according to these rules.

According to the game rules:

(1)Snake drinks water → Snake wins.
(2)Water drowns gun → Water wins.
(3)Gun shoots snake → Gun wins.



'''

def choice(user="",computer=""):
    if user==computer:
        print(f"THE Match is Draw! Because user :{user} and computer: {computer} choose same !")
    else:
        if user == 1 and computer == 2:   #1-snake , 2-water , 3-gun
            print("USER WIN! (Snake drinks water → Snake wins).")
        elif user ==1 and computer ==3:
            print("COMPUTER WIN! (Gun shoots snake → Gun wins).")
        elif user == 2 and computer == 3:
            print("USER WIN! (Water drowns gun → Water wins).")
        elif user ==2 and computer ==1:
            print("COMPUTER WIN! (Snake drinks water → Snake wins).")
        elif user == 3 and computer == 1:
            print("USER WIN! (Gun shoots snake → Gun wins).")
        elif user ==3 and computer ==2:
            print("COMPUTER WIN! (Water drowns gun → Water wins).")
        else:
            print("Somethings is wrong!")
        
        #     if computer ==2:
        #         print(f"user win the match by choosing {user} ")
        # else:
        #     print(f"computer win the match by choosing {computer} ")


import random                   #random use for taking random 
computer = random.choice([1,2,3])
#user part (player-1)
choices = {1: "snake", 2: "water", 3: "gun"}
user = int(input("Enter 1 for Snake, 2 for Water, 3 for Gun: "))
print(f"user chose : {choices[user]}")
print(f"computer chose : {choices[computer]}")
choice(user,computer)
