#!/usr/bin/env python3
"""A simple calculator CLI app"""
import sys

def add(num1, num2):
    """Addition function"""
    return num1 + num2

def subtract(num1, num2):
    """For subtraction"""
    return num1 - num2

def multiply(num1, num2):
    """For multiplication"""
    return num1 * num2

def divide(num1, num2):
    """For division"""
    return num1 / num2

while True:
    print("Welcome to my calculator app\n")
    print("Select an operation to perform\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

    user_choice = input("Enter your choice🤗\n")
    if user_choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        sys.exit(1)

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    output = None

    if user_choice == "1":
        output = add(num1, num2)
    elif user_choice == "2":
        output = subtract(num1, num2)
    elif user_choice == "3":
        output = multiply(num1, num2)
    elif user_choice == "4":
        output = divide(num1, num2)

    print(f"Result: {output}\n")

    user_choice = input("Do you want to continue with another operation? (y/n): ")
    if user_choice == "n":
        break
