import random
from hangman_lgo import logo

#printing hanggman logo
print(logo)
print("Welcome to Hangman!")

lives = 6

game_start = True
while game_start:
    #inputing user choice
    choice = int(input("What do you choose? choose 0 for rock, 1 for paper, or 2 for scissors"))

    #computer choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {computer_choice}")

    #comparing user and computer choice
    if computer_choice > choice:
        lives -= 1
        print("You lose")
        print(f"You have {lives} trials left")
    elif computer_choice == 0 and choice == 2:
        lives -= 1
        print("You lose")
        print(f"You have {lives} trials left")
    elif computer_choice < choice:
        print("You win")
    else:
        print("Draw Game! Choose again please")

    if lives == 0:
        game_start = False



