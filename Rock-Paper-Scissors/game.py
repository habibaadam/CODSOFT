#!/usr/bin/python3

"""Command-line rock paper scissors game"""
import random
import os

#Tracking number of wins # avoid global variables when working on a project.
#instead define a function and call them inside it.
# user_wins = 0
# computer_wins = 0

def game():
    user_wins = 0
    computer_wins = 0
    another_round = 0
    try:

        while True:
            print("Welcome To My Rock Paper Scissors Game 🌟🖤")
            print("1 For Rock 🪨\n2 For Paper📄\n3 For Scissors ✂️ \nLet's Hope You're Lucky!🤣")

            rock_art = """

             ---'    ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)

              """

            paper_art = """

                  _______
              ---'   ____)____
                        ______)
                        _______)
                       _______)
              ---.__________)

                """

            scissors_art = """
                 _______
              ---'   ____)____
                        ______)
                     __________)
                    (____)
              ---.__(___)

                """
            user_Input = input("Enter your choice: ")
            os.system('clear')
            computers_randomNumber = random.randint(0,2) #changed the variable to computer random
            #create a list to contain the choices, and choices of the art,
            #that way you dont need to manually know what the user or computer picked, it will be done
            # automatically by the program
            choice = ["Rock", "Paper","scissors"] 
            choice_art = [rock_art, paper_art, scissors_art]

            # handle exception when the user input a non interger and terminate your program
            #so basically what i did here was that while its not a valid interger just prompt back
            #the enter your choice instead of quiting the program and saying invalid input.
            while not isinstance(user_Input, int):
                 try:
                    user_Input = int(user_Input)
                 except ValueError:
                     user_Input = input("Enter your choice: ")
            if not user_Input > 2:
                #create a list to figure out what computer / user chose.
                users_choice = choice[user_Input]
                computers_choice = choice[computers_randomNumber]
                computer_art_choice = choice_art[computers_randomNumber]
                users_art_choice = choice_art[user_Input]
                #game logic to determine winner/
                """Win Instances For User"""
                if (user_Input == 0 and computers_randomNumber == 2) or (user_Input == 1 and computers_randomNumber ==  0) or (user_Input == 2 and computers_randomNumber == 1):
                    print(f"You chose {users_choice}")
                    print(users_art_choice)
                    print(f"computer chose {computers_choice}")
                    print(computer_art_choice)
                    print("You Win!!!")
                    user_wins += 1
                    
                elif user_Input == computers_randomNumber:
                    print(f"You chose {users_choice}")
                    print(users_art_choice)
                    print(f"computer chose {computers_choice}")
                    print(computer_art_choice)
                    print("\nIT'S A TIE!!!")
                    
                else:
                    print(f"you chose {users_choice}")
                    print(users_art_choice)
                    print(f"computer chose {computers_choice}")
                    print(computer_art_choice)
                    print("You Lose!!!")
                    computer_wins += 1     
            else: 
                user_Input = input("Enter your choice: ")
            another_round += 1
            if another_round > 3:
                another_round = 0
                user_Input = input("Do you want to play another round? (y, continue, or (ctrl + d) or (ctrl + c ) to quit): ")
                if not user_Input.lower() == "y":
                    if user_wins > computer_wins:
                        print(f"Your total score is : {user_wins}")
                        print(f"Computer's total score is : {computer_wins}")
                        print("Congratulations you are the ultimate winner 🏆")
                    elif user_wins == computer_wins:
                        print("Its a draw Game! 🤝")
                    else:
                        print(f"Your total score is : {user_wins}")
                        print(f"Computer's total score is : {computer_wins}")
                        print("computer won: Better luck next time 👾")
                    exit(0)

        # when someone should press (ctrl + d, or ctrl + c) quit the program 
        #else it will crash you program
    except (EOFError, KeyboardInterrupt):       
        os.system('clear')
        print(f"\nYour total score is : {user_wins}")
        print(f"Computer's total score is : {computer_wins}")
        print("Thank you for playing Rock, Paper, Scissors Game!")
        if user_wins > computer_wins:
            print("Congratulations you are the ultimate winner 🏆")
        elif user_wins == computer_wins:
            print("Its a draw Game! 🤝")
        else:
            print("computer won: Better luck next time 👾")
        exit(0) #exit the program automatically.

#call your function as a file not a script like when someone
#import your program so it will not run the code automatially
if __name__ == "__main__":
    game()

#########################################################################################################
        # this could save you from repeating some certain logic over and over again.
        # if u_choice == 1 and computers_choice == 1:
        #     print("You choose rock")
        #     print(rock_art)
        #     print("Computer chose rock")
        #     print(rock_art)
           
        # elif u_choice == 2 and computers_choice == 2:
        #     print("You choose paper")
        #     print("Computer chose paper")
        #     print("\nIT'S A TIE!!!")
        # elif u_choice == 3 and computers_choice == 3:
        #     print("You chose scissors")
        #     print("Computer chose scissors")
        #     print("\nIT'S A TIE!!!")
        #     print("You Lose!!!")
        #     computer_wins += 1

        # if u_choice == 1 and computers_choice == 3:
        #     print("You chose rock")
        #     print(rock_art)
        #     print("Computer chose scissors")
        #     print(scissors_art)
           
        #     user_wins += 1
        # elif u_choice == 2 and computers_choice == 1:
        #     print("You chose paper")
        #     print(paper_art)
        #     print("Computer chose rock")
        #     print(rock_art)
        #     print("You Win!!!")
        #     user_wins += 1
        # elif u_choice == 3 and computers_choice == 2:
        #     print("You chose scissors")
        #     print(scissors_art)
        #     print("Computer chose paper")
        #     print(paper_art)
        #     print("You Win!!!")
        #     user_wins += 1
        # """Win Instances For Computer"""
        # if u_choice == 1 and computers_choice == 2:
        #     print("You chose rock")
        #     print(rock_art)
        #     print("Computer chose paper")
        #     print(paper_art)
        #     print("You Lose!!!")
        #     computer_wins += 1
        # elif u_choice == 2 and computers_choice == 3:
        #     print("You chose paper")
        #     print(paper_art)
        #     print("Computer chose scissors")
        #     print(scissors_art)
            
        # elif u_choice == 3 and computers_choice == 1:
        #     print("You chose scissors")
        #     print(scissors_art)
        #     print("Computer chose rock")
        #     print(rock_art)
        #     print("You Lose!!!")
        #     computer_wins += 1

   