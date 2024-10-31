from models.__init__ import CURSOR, CONN
from models.member import Member

class Workout:
    all = {}

    def __init__(self, name, member_id, id=None):
        self._name = name
        self._id = id
        self.member_id = member_id

    def __repr__(self):
        return f"Workout Classes name={self.name} id={self.id} member id={self.member_id}"
    
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
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, new_id):
        if isinstance(new_id, int):
            self.member_id = new_id
        else:
            raise TypeError("Workout session number")