import random
wordList=["camel","hangman","baboon"]
chosenWord=random.choice(wordList)
guess=input("Guess a letter:").lower()
emptyWord=[]
while("_" in emptyWord):
    for i in range(len(chosenWord)):
        emptyWord.append("_")

        for i in range(len(chosenWord)):
            if(guess==chosenWord[i]):
                emptyWord[i]=chosenWord[i]
        print(emptyWord)        



