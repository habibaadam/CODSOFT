#!/usr/bin/python3

"""Command-line rock paper scissors game"""
import random

#Tracking number of wins
user_wins = 0
computer_wins = 0


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

    for _ in range(3):
        u_choice = int(input("Enter your choice: "))
        try:
            u_choice_err = int(u_choice)
        except ValueError:
            print("Please enter a number between 1 and 3")
            continue

        computers_choice = random.randint(1, 3)
        """Tie Instances"""
        if u_choice == 1 and computers_choice == 1:
            print("You choose rock")
            print(rock_art)
            print("Computer chose rock")
            print(rock_art)
            print("\nIT'S A TIE!!!")
        elif u_choice == 2 and computers_choice == 2:
            print("You choose paper")
            print("Computer chose paper")
            print("\nIT'S A TIE!!!")
        elif u_choice == 3 and computers_choice == 3:
            print("You chose scissors")
            print("Computer chose scissors")
            print("\nIT'S A TIE!!!")

        """Win Instances For User"""
        if u_choice == 1 and computers_choice == 3:
            print("You chose rock")
            print(rock_art)
            print("Computer chose scissors")
            print(scissors_art)
            print("You Win!!!")
            user_wins += 1
        elif u_choice == 2 and computers_choice == 1:
            print("You chose paper")
            print(paper_art)
            print("Computer chose rock")
            print(rock_art)
            print("You Win!!!")
            user_wins += 1
        elif u_choice == 3 and computers_choice == 2:
            print("You chose scissors")
            print(scissors_art)
            print("Computer chose paper")
            print(paper_art)
            print("You Win!!!")
            user_wins += 1



        """Win Instances For Computer"""
        if u_choice == 1 and computers_choice == 2:
            print("You chose rock")
            print(rock_art)
            print("Computer chose paper")
            print(paper_art)
            print("You Lose!!!")
            computer_wins += 1
        elif u_choice == 2 and computers_choice == 3:
            print("You chose paper")
            print(paper_art)
            print("Computer chose scissors")
            print(scissors_art)
            print("You Lose!!!")
            computer_wins += 1
        elif u_choice == 3 and computers_choice == 1:
            print("You chose scissors")
            print(scissors_art)
            print("Computer chose rock")
            print(rock_art)
            print("You Lose!!!")
            computer_wins += 1

    print(f"Your total score is : {user_wins}")
    print(f"Computer's total score is : {computer_wins}")

    another_round = input("Do you want to play another round? (yes/no): ")
    if another_round.lower() != "yes":
        print("Thanks for playing!")
        break