#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.member import Member
from models.workout_class import Workout

def seed_database():
    Member.drop_table()
    Workout.drop_table()
    Workout.create_table()
    Member.create_table()

    #create starter data
    #member starter data
    m1 = Member.create("John", 1)
    m2 = Member.create("Peter", 2)

    #class program starter data 
    class_name = Workout.create("HIIT boxing", 1, 1)


seed_database()