# lib/cli.py

from helpers import (
    exit_program,
    list_members,
    create_member,
    update_member,
    delete_member,
    list_member_workouts,
    create_workout,
    list_workouts,
    update_workouts,
    delete_workout,
    find_member_by_workout
)

def member_menu():
    print("\nMember Management:")
    print("1. List all members")
    print("2. Create new member")
    print("3. Update member information")
    print("4. Delete Member information")
    print("5. Member enrolled Workout")
    print("b. Back to main menu")
    choice = input("> ")
    return choice

def workout_menu():
    print("\nWorkout Management:")
    print("1. Read all workouts")
    print("2. Create new workout class")
    print("3. Update workout information")
    print("4. Delete workout")
    print("5. Find member by workout")
    print("b. Back to main menu")
    choice = input("> ")
    return choice

def prompt_for_employee_name():
    name = input("Enter employee's name: ")
    return name

def confirm_action(message):
    confirmation = input(f"{message} (y/n): ").lower()
    return confirmation == 'y'

def main(employee_name):
    while True:
        print(f"\nWelcome, {employee_name}! Gym Management System")
        print("1. Member Management")
        print("2. Workout Management")
        print("e. Exit the program")
        choice = input("> ")

        if choice == "1":
            while True:
                member_choice = member_menu()
                if member_choice == "1":
                    list_members()
                elif member_choice == "2":
                    create_member()
                elif member_choice == "3":
                    update_member()
                elif member_choice == "4":
                    delete_member()
                elif member_choice == "5":
                    list_member_workouts()
                elif member_choice == "b":
                    break
                else:
                    print("Invalid choice")
        elif choice == "2":
            while True:
                workout_choice = workout_menu()
                if workout_choice == "1":
                    list_workouts()
                elif workout_choice == "2":
                    create_workout()
                elif workout_choice == "3":
                    update_workouts()
                elif workout_choice == "4":
                    delete_workout()
                elif workout_choice == "5":
                    find_member_by_workout()
                elif workout_choice == "b":
                    break
                else:
                    print("Invalid choice")
        elif choice == "e":
            exit_program()
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    employee_name = prompt_for_employee_name()
    if confirm_action("Do you want to proceed to the main menu?"):
        main(employee_name)
    else:
        print("Goodbye!")


