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
    m2 = Member.create("Peter", "perter123@gmail.com", 2)

# _______#Workout starter data
    Workout.create("Boxing", "Tyson")
    Workout.create("Swimming", "Micheal")
    Workout.create("Yoga", "Sydney")
    Workout.create("Cardio", "Kobe")

seed_database()
