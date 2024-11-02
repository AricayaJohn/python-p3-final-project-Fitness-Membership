# lib/cli.py

from helpers import (
    exit_program,
    list_members,
    create_member
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_members()
        elif choice == "2":
            create_member
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List of all members")


if __name__ == "__main__":
    main()
