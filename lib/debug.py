#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.member import Member
from models.workout_class import Workout_class

member = Member("John", 1)
workout = Workout_class("HIIT boxing", 1)

import ipdb

ipdb.set_trace()
