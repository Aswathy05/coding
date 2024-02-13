rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
def image(player):
    if(player==0):
        print(rock)
    elif(player==1):
        print(paper)
    elif(player==2):
        print(scissors) 

rounds=int(input("How many rounds do you want to play?\n"))
c,p=0,0
print("What do you choose?\n0 for rock\n1 for paper\n2 for scissors")
for i in range(rounds):
    player=int(input("Your choice: "))
    while(True):
        if(player>2):
            print("Please enter a valid number")
            player=int(input("Your choice: "))
        if(player<=2):    
            image(player)
            comp=random.randint(0,2)
            print("Computer chose:")
            image(comp)  
        if(player==comp):
            break
        elif((player==0 and comp==1) or (player==1 and comp==2) or (player==2 and comp==0)):
            c+=1
            break
        elif(comp==0 and player==1) or (comp==1 and player==2) or (comp==2 and player==0):
            p+=1      
            break
    print("Computer: " + str(c) +"\tPlayer: "+str(p))    
if(p==c):
    print("Its a draw")
elif(p>c):
    print("You win!")
else:
    print("You lose")        