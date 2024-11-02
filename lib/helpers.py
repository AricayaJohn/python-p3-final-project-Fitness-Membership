# lib/helpers.py

from models.__init__ import CURSOR, CONN
from models.member import Member
from models.workout_class import Workout

def exit_program():
    print("Goodbye!")
    exit()

def list_members():
    members = Member.get_all()
    for member in members:
        print(member)

def create_member():
    name = input("Enter new member's name: ")
    email = input("Enter new member's email: ")
    workout_id = input("Enter member's choice of workout by id: ")
    try:
        member = Member.create(name, email, workout_id)
        print(f'Sign-up for new member: {member} successful')
    except Exception as exc:
        print("Error creating new member: ", exc)

def update_member():
    id_ = input("Enter the member's ID: ")
    if member := Member.find_by_id(id_):
        print("Select which to update: ")
        print("1. Name")
        print("2. Email")
        print("3. Workout ID")
        choice = input("> ")
        try:
            if choice == "1":
                new_name = input("Enter the new name: ")
                member.name = new_name
            elif choice == "2":
                new_email = input("Enter the new email: ")
                member.email = new_email
            elif choice == "3":
                new_workout_id = input("Enter the new workout ID: ")
                member.workout_id = new_workout_id
            else:
                print("Invalid choice")
                return

            member.update()
            print(f"Successfully updated {member} information")
        except Exception as exc:
            print("Error updating", exc)
    else:
        print("Member not found.")

def delete_member():
    id_ = input("Enter the member's ID to delete: ")
    if member := Member.find_by_id(id_):
        member.delete()
        print(f"Successfully deleted member with ID: {id_}")
    else:
        print("Member not found.")

def list_member_workouts():
    id_ = input("Enter the member's Id: ")
    if member := Member.find_by_id(id_):
        workout = Workout.find_by_id(member.workout_id)
        if workout:
            print(f"Member {member.name} is entrolled in: {workout.name}")
        else:
            print("No workout found")
    else:
        print("Member not found")

