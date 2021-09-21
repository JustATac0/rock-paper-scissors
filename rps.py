# Created by Josh C

import random
from time import sleep


# Function name is 'tutorial'
def tutorial():

    # Explain rules of the game, prompt user to begin the game or terminate the program
    tut = input("\nWelcome to the Rock, Paper, Scissors tutorial! The rules of the game are pretty simple.\n"
                "There are 3 choices for the player to pick from: rock, paper, or scissors. Each one of\n"
                "the options have 3 possible outcomes: a win, a loss, or a tie. Rock beats out scissors,\n"
                "scissors beat out paper, and paper beats out rock. It goes full circle ensuring that both\n"
                "players have a fair chance against one another. Now that you got the basics down, are you\n"
                "prepared to begin the game? (Y/N)\n")

    # If user chooses to begin game, start game
    if tut == "Y" or tut == "y":
        play()
        return

    # If user chooses to not begin game, terminate program
    if tut == "N" or tut == "n":
        print("Okay!")
        return

    # If user enters a character other that 'Y' or 'N', restart the game
    else:
        print("Sorry, I didn't get that. Let's try again!")
        rock_paper_scissors()
        return


# Function name is 'play'
def play():

    # Prompt user for choice
    selection = input("Do you choose Rock (R), Paper (P), or Scissors (S)?\n")
    # Define possible choices
    options = ["Rock", "Paper", "Scissors"]
    # Define computer choice
    comp_choice = random.choice(options)

    # Compare player choice to computer choice to determine a winner

    if selection == "R" or selection == "r" and comp_choice == "Rock":
        print("It's a tie!")
        replay()
        return

    if selection == "P" or selection == "p" and comp_choice == "Paper":
        print("It's a tie!")
        replay()
        return

    if selection == "S" or selection == "s" and comp_choice == "Scissors":
        print("It's a tie!")
        replay()
        return

    if selection == "R" or selection == "r" and comp_choice == "Scissors":
        print(f"You won! The computer chose {comp_choice}.")
        replay()
        return

    if selection == "P" or selection == "p" and comp_choice == "Rock":
        print(f"You won! The computer chose {comp_choice}.")
        replay()
        return

    if selection == "S" or selection == "s" and comp_choice == "Paper":
        print(f"You won! The computer chose {comp_choice}.")
        replay()
        return

    if selection == "R" or selection == "r" and comp_choice == "Paper":
        print(f"You lost! The computer chose {comp_choice}.")
        replay()
        return

    if selection == "P" or selection == "p" and comp_choice == "Rock":
        print(f"You lost! The computer chose {comp_choice}.")
        replay()
        return

    if selection == "S" or selection == "s" and comp_choice == "Rock":
        print(f"You lost! The computer chose {comp_choice}.")
        replay()
        return

    # If user enters a character other that 'R', 'P', or 'S', prompt user again
    else:
        print("Sorry, I didn't get that. Let's try again!")
        play()
        return


# Function name is 'replay'
def replay():
    # Wait 1 second
    sleep(1)
    # Ask user if they would like to play again
    new_game = input("\nWould you like to play again? (Y/N)\n")

    # If user chooses to not play again, terminate the program
    if new_game == "N" or new_game == "n" or new_game == "No" or new_game == "no":
        print("Okay!")
        return

    # If user chooses to play again, replay the game
    if new_game == "Y" or new_game == "y" or new_game == "Yes" or new_game == "yes":
        play()
        return

    # If user enters a character other that 'Y' or 'N', prompt user again
    else:
        print("Sorry I didn't get that, let's try again!")
        replay()
        return


# Function name is 'rock_paper-scissors'
def rock_paper_scissors():
    # Intro to the game, prompt user to begin game or enter tutorial
    start = input("\nWelcome to Rock, Paper, Scissors! Are you ready to start the game? Type Y for yes or N for no.\n\n"
                  "To access the tutorial, please type T.\n")

    # If user chooses not to begin game, terminate program
    if start == "N" or start == "n" or start == "No" or start == "no":
        print("Okay!")
        return

    # If user chooses to begin game, start game
    if start == "Y" or start == "y" or start == "Yes" or start == "yes":
        play()
        return

    # If user chooses to read the tutorial, open the tutorial
    if start == "T" or start == "t":
        tutorial()
        return

    # If user enters a character other that 'Y', 'N', or 'T', restart the game
    else:
        print("Sorry, I don't understand. Let's try again!")
        rock_paper_scissors()
        return


# Start game on run
rock_paper_scissors()
