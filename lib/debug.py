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

#_________________Added new instance Workout_id Check________


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

#_____________Checking get_all_____________________
# ipdb> member13 = Member("cena", "cena123@gmail.com")
# ipdb> member13.save()
# ipdb> Member.get_all()

#____________Find by id test_____________________
# ipdb> Member.find_by_id(2)
# Member name=bro email=bro123@gmail.com id=2

#____________Find by name test____________________
#ipdb> Member.find_by_name("John")
# [Member name=John email=john123@gmail.com id=1]
# ipdb> Member.find_by_name("al")
# [Member name=al email=al123@gmail.com id=3, Member name=al email=al123@gmail.com id=4, Member name=al email=al123@gmail.com id=5]

#__________Creating Workout table and instance_____
# ipdb> Workout.drop_table()
# ipdb> Workout.create_table()
# ipdb> w1 = Workout("Boxing", "tyson")
# ipdb> w1.name
# 'Boxing'
# ipdb> w1.save()

#_______Testing save instance_________
# ipdb> w1 = Workout("Boxing", "tyson")
# ipdb> w1.name
# 'Boxing'
# ipdb> w1.save()

#_______ Testing create classmethod______
#ipdb> w2 = Workout.create("yoga", "sydney")
#ipdb> w2
# Workout Classes name=yoga id=2 trainer =sydney


#_____Testing update instance________
# ipdb> w6 = Workout.create("climbing", "nadal")
# ipdb> w6
# Workout Classes name=climbing id=6 trainer =nadal
# ipdb> w6.name = "surfing"
# ipdb> w6.update()
# ipdb> w6
# Workout Classes name=surfing id=6 trainer =nadal