# CLI+ORM Project for Gym Workout and Member Management

## Learning Goals

- We want to Focus on building functionality that follow the CRUD operations(CREATE, READ, UPDATE, Delete) 
- We want to use SQLite and Python to store and manage data in the Company.db database

---

## Introduction

Take a look at the directory structure:

.lib
    ├── models
    │   ├── __init__.py
                //Initialize SQLite3 to allow our python code to use SQL commands
                //Connect our database to our other files
                //Includes Cursor object that lets you run sql commands
    │   └── member.py 
                //Defines member class its functions and operations
                //Includes the CRUD operations to handle database interaction
    │   └──workout_class.py
                //Defines the Workout class function and operations
                //Include CRUD methods for managing workouts
    ├── cli.py
                //Contains the main function that runs the CLI(command-line interface)
    ├── debug.py
                //Creates ipdb debugger to check if our functions and methods are working properly
    └── helpers.py
                //Functions as a bridge between CLI and the data class models

---

## Generating Your Environment then using CLI

1. To run this application you first need to fork and clone this repository:
https://github.com/AricayaJohn/python-p3-final-project-Fitness-Membership

2. Install dependencies:
$pipenv install

3. Enter virtual environment
$pipenv shell

4. To use the CLI:
$python lib/cli.py

##Editing

1. Set up a classmethod function, or an instance in either member.py or workout_class.py

2. Create a cli option in cli.py for your new method or instance

3. Create a helper method that can interact with your class model file if needed

##CLI main menu:

Please select an option:
0. Exit the program
1. List of all members
2. Create new member
3. Update member information
4. Delete member information
5. Member enrolled workout
6. Create new workout class
7. Read all workouts
8. Update workout information
9. Delete workout
10. Find member by workout
---

## Conclusion

This CLI application is for a fitness company that has a need to manage their members and their workout data to make better business decisions. It is designed to allow the program to create, review, update, and delete a member or workout in the fitness company's database

Happy coding!