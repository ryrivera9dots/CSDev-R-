import random

def RockPaperScissors():
    player = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
    computer = random.choice(["Rock", "Paper", "Scissors"])

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print(f"It's a tie! Both chose {player}.")
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        print(f"You win! {player} beats {computer}.")
    else:
        print(f"You lose! {computer} beats {player}.")

def play_game():
    print("Welcome to Rock, Paper, Scissors 9Dots coders")
    while True:
        RockPaperScissors()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Call the play_game function to start the game
play_game()
