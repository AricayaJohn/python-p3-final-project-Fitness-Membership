from models.__init__ import CURSOR, CONN

class Workout_class:
    all = []

    def __init__(self, name, id=None)
        self.name = name
        self.id = id
        Workout_class.all.append(self)

    def __repr__(self):
        return f"Workout Classes name={self.name} id={self.id}"
    
    @property
    def name(self):
        return self._name

    
    