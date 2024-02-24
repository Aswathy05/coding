import numberGuessGameArt
import random
print(numberGuessGameArt.logo)
print("\nWelcome to the Number Guessing Game!\n\nI'm thinking of a number from 1 to 100")

def play_again():
    another_game=input("Type 'y' if you want to play another game. Type 'n' if you want to exit\n")
    if(another_game=="y"):
        game()
    else:
        print("Goodbye!\n")

def difficulty():
    difficulty=input("\nChoose the diffculty. Type 'easy' or 'hard': ").lower()
    global attempts
    if(difficulty=="easy"):
        attempts=10
    else:
        attempts=5
    print(f"\nYou will be given {attempts} attempts to guess the number\n")
    return attempts

def game():
    random_number = random.randint(1,100)
    difficulty()
    for _ in range(1,attempts+1):
        guessed_number=int(input("Guess a number: "))
        if(guessed_number==random_number):
            print("That's correct! You guessed it right! You won!\n")
            play_again()
            break
        else:
            if(guessed_number<random_number+5 and guessed_number>random_number):
                print("High but you're near!")
            elif(guessed_number>random_number-5 and guessed_number<random_number):
                print("Low but you're near!")
            elif(guessed_number>random_number):
                print("Too high!")
            elif(guessed_number<random_number):
                print("Too low!")
            print(f"Guess again.\nYou have {attempts-_} attempts left\n")
    else:
        print(f"You've used all your attempts! The number was {random_number}. Better luck next time.\n")
        play_again()
game()  


