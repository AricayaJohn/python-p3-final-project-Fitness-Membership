# lib/helpers.py

from models.__init__ import CURSOR, CONN
from models.member import Member
from models.workout_class import Workout


def list_members():
    members = Member.get_all()
    for i, member in enumerate(members, start = 1):
        print(f"{i}, {member.name}")

def create_member():
    name = input("Enter new member's name: ")
    email = input("Enter new member's email: ")
    workout_id = input("Enter member's choice of workout by id: ")
    try:
        member = Member.create(name, email, workout_id)
        print('Sign-up for new member successful')
    except Exception as exc:
        print("Error creating new member: ", exc)

def update_member():
    name = input("Enter the member's name: ")
    members = Member.find_by_name(name)

    if members:
        member = members[0]
        print(f"\n Member found: {member.name}")

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
                new_workout_id = int(input("Enter the new workout ID: "))
                if Workout.find_by_id(new_workout_id):
                    member.workout_id = new_workout_id
                else: print("invalid workout id")
                return
            else:
                print("Invalid choice")
                return

            member.update()
            print(f"Successfully updated {member.name} information")
        except Exception as exc:
            print("Error updating", exc)
    else:
        print("Member not found.")

def delete_member(): 
    name = input("Enter the member's name to delete: ")
    members = Member.find_by_name(name) 
    
    if members: 
        if len(members) > 1: 
            print(f"Multiple members found with name {name}") 
            for i, member in enumerate(members, start=1): 
                print(f"{i} {member.name}") 
            choice = int(input("Enter the number of the member to delete: ")) -1 
            member_to_delete = members[choice]
        else:
            member_to_delete = members[0] 
        member_to_delete.delete() 
        print(f"Successfully deleted member: {member_to_delete.name}")
    
        Member.all = {member.id: member for member in Member.get_all()}
    else: 
        print("Member not found.")

def list_member_workouts():
    name = input("Enter the member's name: ")
    members = Member.find_by_name(name)

    if members:
        if len(members) > 1:
            print(f"Multiple members found with name '{name}' :")
            for i, member in enumerate(members, start=1):
                print(f"{i}. {member.name}")

            choice = int(input("Enter the number of the member to view workouts: "))       
            member = members[choice]
        else: 
            member = members[0]

        workout = Workout.find_by_id(member.workout_id)
        if workout:
            print(f"Member {member.name} is entrolled in: {workout.name}")
        else:
            print("No workout found")
    else:
        print("Member not found")

def create_workout():
    name = input("Enter workout name: ")
    trainer = input("Enter the trainer's name:")
    try:
        workout = Workout(name, trainer)
        workout.save()
        print(f"Successfully created new workout: {workout.name}")
    except Exception as exc:
        print("Error in creating new workout: ", exc)

def list_workouts():
    workouts = Workout.get_all()
    for workout in workouts:
        print(workout)

def check_trainers():
    check_trainers = input("\nDo you want to check the trainers for each class (y/n): ").lower()
    if check_trainers == "y":
        workouts = Workout.get_all()
        print("""
        Workout Classes and Trainers: 
        """)
        for workout in workouts:
            print(f"{workout.name}: {workout.trainer}")
    else:
        print("\nReturning to workout menu")

def update_workouts():
    id = input("Enter the workout's ID: ")
    if workout := Workout.find_by_id(id):
        print("Select which workout to update")
        print("1. Name")
        print("2. Trainer")
        choice = input("> ")
        try:
            if choice == "1":
                new_name = input("Enter new workout name: ")
                workout.name = new_name
            elif choice == "2":
                new_trainer = input("Enter new trainer name: ")
                workout.trainer = new_trainer
            else:
                print("Invalid Choice")
                return

            workout.update()
            print(f"Successfully updated workout: {workout.name}")
        except Exception as exc:
            print("Error updating workout: ", exc)
    else:
        print("Workout not found.")

def delete_workout():
    id = input("Input the workout id to be deleted: ")
    if workout := Workout.find_by_id(id):
        workout.delete()
        print(f"Successfully deleted workout with id : {id}")
    else:
        print("Workout not found")

def find_member_by_workout():
    workout_id = input("Enter the workout ID: ")
    members = Member.find_member_by_workout(workout_id)
    if members:
        print(f"Members enrolled in Workout ID {workout_id}: ")
        for member in members:
            print(member.name)
    else:
        print("no members found for this workout id")

def list_workouts():
    workouts = Workout.get_all()
    for i, workout in enumerate(workouts, start = 1):
        print(f"{i}, {workout.name}")
        
def exit_program():
    print("You are about to leave, bye-bye!")
    exit()