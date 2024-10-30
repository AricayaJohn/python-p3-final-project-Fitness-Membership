from models.__init__ import CURSOR, CONN

class Workout_class:
    all = []

    def __init__(self, class_name, id=None)
        self.class_name = class_name
        self.id = id
        Workout_class.all.append(self)

    def __repr__(self):
        return f"Workout Classes name={self.class_name} id={self.id}"
    
    @property
    def name(self):
        return self._class_name

    @name.setter
    def name(self, new_class_name):
        if isinstance(new_class_name, str):
            if len(new_class_name) == 0:
                raise ValueError("Input name cannot be empty")
                self._name = new_class_name
        else:
            raise TypeError("Name must be a string")