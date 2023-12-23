#!/usr/bin/python3

"""Command-line rock paper scissors game"""
import random

while True:
    print("Welcome To My Rock Paper Scissors Game 🌟🖤")
    print("1 For Rock 🪨\n2 For Paper📄\n3 For Scissors ✂️ \nLet's Hope You're Lucky!🤣")

    rock_art = """

     ---'   ____)
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

    tie_art = """
      _   _
     | | (_)
     | |_ _  ___
     | __| |/ _ \
     | |_| |  __/
      \__|_|\___|

        """

    u_choice = int(input("Enter your choice: "))
    computers_choice = random.randint(1, 3)
    """Tie Instances"""
    if u_choice == 1 and computers_choice == 1:
        print("You choose rock")
        print(rock_art)
        print("Computer chose rock")
        print(rock_art)
        print("Its a tie!!!")
        print(tie_art)
    elif u_choice == 2 and computers_choice == 2:
        print("You choose paper")
        print("Computer chose paper")
        print("Its a tie!!!")
        print(tie_art)
    elif u_choice == 3 and computers_choice == 3:
        print("You chose scissors")
        print("Computer chose scissors")
        print("Its a tie!!!")
        print(tie_art)

    """Win Instances For User"""
    if u_choice == 1 and computers_choice == 3:
        print("You chose rock")
        print(rock_art)
        print("Computer chose scissors")
        print(scissors_art)
        print("You Win!!!")
    elif u_choice == 2 and computers_choice == 1:
        print("You chose paper")
        print(paper_art)
        print("Computer chose rock")
        print(rock_art)
        print("You Win!!!")
    elif u_choice == 3 and computers_choice == 2:
        print("You chose scissors")
        print(scissors_art)
        print("Computer chose paper")
        print(paper_art)
        print("You Win!!!")

    """Win Instances For Computer"""
    if u_choice == 1 and computers_choice == 2:
        print("You chose rock")
        print(rock_art)
        print("Computer chose paper")
        print(paper_art)
        print("You Lose!!!")
    elif u_choice == 2 and computers_choice == 3:
        print("You chose paper")
        print(paper_art)
        print("Computer chose scissors")
        print(scissors_art)
        print("You Lose!!!")
    elif u_choice == 3 and computers_choice == 1:
        print("You chose scissors")
        print(scissors_art)
        print("Computer chose rock")
        print(rock_art)
        print("You Lose!!!")

    another_round = input("Do you want to play another round? (yes/no): ")
    if another_round.lower() != "yes":
        break
