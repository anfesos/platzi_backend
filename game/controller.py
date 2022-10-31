import user_interface
import random
import model
import re
import sys

def orquestation():
    
    while model.game_status:
        select_menu_option()
    

def select_menu_option():
    
    player_choice = user_interface.menu_choice()

    if player_choice == '1':
        show_rules()
    elif player_choice == '2':
        change_configurations()
    elif player_choice == '3':
        round_number = 0
        user_interface.players_points
        while round_number < model.max_number_of_rounds:
            play_game()
            round_number+=1
        user_interface.screen_result(winner())
        user_interface.do_you_want_play_again()
    elif player_choice == '4':
        print("\n Game Finished !!! :( \n")
        model.game_status = False
        #TODO: Make a question if the user wants to save a historic of the results
    else:
        raise Exception("The user don't sent a correct information in the menu")


def play_game():

    player_choice_select = user_interface.player_choice()
    player_choice_select = player_choice_select.lower()

    machine_choice = random_machine_choice()
    
    print(f"\n{model.player_name} : {player_choice_select} <Fight> Machine : {machine_choice} \n")

    if player_choice_select != machine_choice:
        if player_choice_select == "stone" and machine_choice == "scissor":
            print(f"Win {model.player_name} !\n")
            model.player_points+=1
        elif player_choice_select == "stone" and machine_choice == "paper":
            print(f"Win the Machine !\n")
            model.machine_points+=1
        elif player_choice_select == "paper" and machine_choice == "scissor":
            print(f"Win the Machine !\n")
            model.machine_points+=1
        elif player_choice_select == "paper" and machine_choice == "stone":
            print(f"Win {model.player_name} !\n")
            model.player_points+=1
        elif player_choice_select == "scissor" and machine_choice == "stone":
            print(f"Win the Machine !\n")
            model.machine_points+=1
        elif player_choice_select == "scissor" and machine_choice == "paper":
            print(f"Win {model.player_name} !\n")
            model.player_points+=1
    else:
        print("It was draw !!\n")
    
    user_interface.players_points()


def random_machine_choice():
    choices = ("stone","paper","scissor")

    return random.choice(choices)


def winner():
    if model.player_points > model.machine_points:
        model.last_winner = model.player_name
        return model.player_name
    elif model.player_points < model.machine_points:
        model.last_winner = "machine"
        return "machine"
    else:
        model.last_winner = "draw"
        return "draw"


def change_configurations():

    change_the_name_by_defect()
    
    change_the_numbers_of_rounds()


def change_the_name_by_defect():
    answer = input("Do you want to change the name of the player by defect? (y/n): ")

    while len(answer) > 1 or not re.match("^[yn]",answer.lower()):
        answer = input("You should insert the character (y/n): ")
    
    if answer == "y":
        answer = input("Insert the new name: ")
        new_name = answer
        while len(answer) > 1 or not re.match("^[y]",answer.lower()):
            answer = input(f"Do you want this name ({new_name}) really? (y/n) : ")

            while len(answer) > 1 or not re.match("^[yn]",answer.lower()):
                answer = input(" you should insert the character (y/n): ")
            
            if answer == "n":
                answer = input("What is the correct name? : ")
                new_name = answer
            else:
                model.player_name = new_name
                print("Player name changed successfully.!!!")
    else:
        print("You don´t change the name by defect.")


def change_the_numbers_of_rounds():
    
    list_of_rounds = [1,2,3,4,5]

    answer = input("Do you want to change the number of rounds to play? (y/n) : ")

    while len(answer) > 1 or not re.match("^[yn]",answer.lower()):
        answer = input("You should insert the character (y/n): ")

    if answer == "y":

        answer = input("Insert one integer number between 1 to 5: ")

        while len(answer)>1 or not re.match("^[1-5]",answer):
            answer = input("You should insert one integer number between 1 to 5: ")

        model.max_number_of_rounds = int(answer)

        print("Number of rounds changed successfully.!!!")
    else:
        print("You don't change the number of rounds by defect.")


def show_rules():

    with open(sys.path[0] + '/Rules.md','r') as file:
        for line in file:
            print(line)

