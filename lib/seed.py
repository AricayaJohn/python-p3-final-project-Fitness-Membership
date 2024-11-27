#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.member import Member
from models.workout_class import Workout

def seed_database():
    Member.drop_table()
    Workout.drop_table()
    Workout.create_table()
    Member.create_table()

# _______#create starter data
# _______#member starter data
    m1 = Member.create("John", "john123@gmail.com", 1)
    m2 = Member.create("Peter", "peter123@gmail.com", 2)
    m3 = Member.create("Nik", "Nik123@gmail.com", 3)
    m4 = Member.create("King", "king123@gmail.com", 1)

# _______#Workout starter data
    Workout.create("Boxing", "Tyson")
    Workout.create("Swimming", "Micheal")
    Workout.create("Yoga", "Sydney")
    Workout.create("Cardio", "Kobe")

seed_database()
