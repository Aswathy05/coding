import random
import hangmanTools
import hangmanWords
print(hangmanTools.logo)
wordList=hangmanWords.words
chosenWord=random.choice(wordList)
emptyWord=[]
for i in range(len(chosenWord)):
        emptyWord.append("_")
print(*emptyWord)
print()
lifeLoss=0
prev=[]
while(True):    
        guess=input("Guess a letter:").lower()
        if(guess in prev):
            print("You already guessed the letter. Guess another letter!\n")
            continue
        else:
            prev.append(guess)     
        crt=0
        for i in range(len(chosenWord)):
            if(guess==chosenWord[i]):
                emptyWord[i]=chosenWord[i]
                crt=1
                
        if(crt==0):
            print("You guessed it wrong. You lose a life :(\n")
            lifeLoss+=1
        print(*emptyWord,"\n")
        if("_" not in emptyWord):
            print("YOU WIN ;)")
            break 
        print(hangmanTools.hangMans[lifeLoss],"\n")  
        if(lifeLoss==(len(hangmanTools.hangMans)-1)):
            print("YOU LOSE :(")
            print(f"The word was {chosenWord}.")
            break
        
        



