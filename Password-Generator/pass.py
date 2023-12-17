#!/usr/bin/env  python3
"""Simple Password Generator"""
import sys
import random
import string


def generate_password(length):
    """Generate password"""
    password = ""
    for _ in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of password: "))
        print(f"Your password is: {generate_password(length)}")
    except ValueError:
        print("Invalid input")
        sys.exit(1)