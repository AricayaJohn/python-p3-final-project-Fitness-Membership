#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.member import Member
from models.workout_class import Workout
# from seed import seed_database

import ipdb


ipdb.set_trace()


#_________________ TRIAL DEBUG_____________________
# seed_database()
# Member.create_table()
# m1 = Member("John", "john123@gmail.com")
# m1.save()


#___________________DEBUG RECORD___________________

#updating member information
# ipdb> m9 =  Member("drooski", "drooski123@gmail.com")
# ipdb> m9
# Member name=drooski email=drooski123@gmail.com id=None
# ipdb> m9.save()
# ipdb> m9
# Member name=drooski email=drooski123@gmail.com id=9
# ipdb> self
# *** NameError: name 'self' is not defined
# ipdb> m9.name
# 'drooski'
# ipdb> m9.name = "dru"
# ipdb> m9.update()
# ipdb> m9
# Member name=dru email=drooski123@gmail.com id=9


#deleting row 
# ipdb> m13 = Member("drooski", "drooski123@gmail.com")
# ipdb> m13
# Member name=drooski email=drooski123@gmail.com id=None
# ipdb> m13.save()
# ipdb> m13
# Member name=drooski email=drooski123@gmail.com id=13
# ipdb> m13.delete()
# ipdb> m13 = Member("drooski", "drooski123@gmail.com")
# ipdb> m13.save()
# ipdb> m13.delete()

