from models.__init__ import CURSOR, CONN

class Workout_class:
    all = []

    def __init__(self, name, id=None):
        self._name = name
        self._id = id
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

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if isinstance(new_id, int):
            self._id = new_id
        else:
            raise TypeError("Workout session number")