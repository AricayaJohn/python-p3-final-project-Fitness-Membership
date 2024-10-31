#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.member import Member
from models.workout_class import Workout_class

m1 = Member("John", 1)
class_name = Workout_class("HIIT boxing", 1)

import ipdb

ipdb.set_trace()
