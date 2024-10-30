from models.__init__ import CURSOR, CONN

class Workout_class:
    all = []

    def __init__(self, name, id=None):
        self.name = name
        self.id = id
        Workout_class.all.append(self)

    def __repr__(self):
        return f"Workout Classes name={self.name} id={self.id}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) == 0:
                raise ValueError("Input name cannot be empty")
            self._name = new_name
        else:
            raise TypeError("Name must be a string")