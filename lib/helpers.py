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
        print("Error creating new member: " exc)
