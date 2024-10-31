#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.member import Member
from models.workout_class import Workout

def seed_data():
    Member.drop_table()
    Workout.drop_table()
    Workout.create_table()
    Member.create_table()

    