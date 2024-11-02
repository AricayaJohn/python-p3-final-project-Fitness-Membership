# lib/cli.py

from helpers import (
    exit_program,
    list_members,
    create_member,
    update_member,
    delete_member,
    list_member_workouts
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
            create_member()
        elif choice == "3":
            update_member()
        elif choice == "4":
            delete_member()
        elif choice == "5":
            list_member_workouts()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List of all members")
    print("2. Create new member")
    print("3. Update member information")
    print("4. Delete member information")
    print("5. Member enrolled workout")


if __name__ == "__main__":
    main()
