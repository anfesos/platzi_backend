import re
from statistics import mode
import model


def menu_choice():
    print("\n+-------------------+\n")

    print("¡¡¡ Play Stone, Paper and Sccisor !!! \n")
    print("1. Rules of the game.")
    print("2. Change configurations by defect.")
    print("3. Let's play!!!")
    print("4. Exit Game.\n")

    choice = input("What do you want to do, insert one option: ")

    while len(choice) !=1 or not re.match('[1-4]',choice):
        choice = input("You should insert any number between (1-4) : ")
    
    print("\n+-------------------+\n")
    return choice

def player_choice():
    choice = input("What is your choice: [Stone, Paper, Scissor]: ")

    while not re.match("(stone)|(paper)|(scissor)",choice.lower()):
        choice = input("You should type any the next options: [stone, paper, scissor]: ")

    return choice

def players_points():
    print("\n**** Game Status ****")
    print(f"{model.player_name} points: {model.player_points}")
    print(f"Machine points   : {model.machine_points}")
    print("*********************\n")


def screen_result(winner_player):

    if winner_player == model.player_name:
        print(f"\n {winner_player} You're the best.!!!\n")
    elif winner_player == "machine":
        print(f"\nThe machines rules.!!!\n")
    else:
        print(f"\nThe Game finished draw, good luck next time.\n")
    
    print("---------------------\n")


def do_you_want_play_again():
    play_again = input("Do you want play again?(y/n): ")

    while len(play_again) !=1 or not re.match('^[yn]',play_again.lower()):
        play_again = input("You should insert (y/n) character: ")

    
    if play_again.lower() == 'y':
        print("\n+-------------------+\n")
        print(f"\nWelcome Again {model.player_name} \n")
        
        if model.last_winner == model.player_name:
            print("I see you want to win again. !!!\n")
        elif model.last_winner == "machine":
            print("I see you want the revenge. Let's do it.!!!\n")
        else:
            print("No more draws.!!!\n")
        model.machine_points=0
        model.player_points=0
    else:
        model.game_status = False
        print("Finished Game. :)")
