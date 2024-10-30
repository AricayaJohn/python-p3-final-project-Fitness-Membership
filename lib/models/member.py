from models.__init__ import CONN, CURSOR

class Member:

    all = []

    def __init__(self, name, id=None, class_id):
        self.name = name
        self.id = id
        self.class_id  = class_id
        Member.all.append(self)

    def __repr__(self):
        return f"Member name={self.name} id={self.id} class_id = {self.class_id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) == 0:
                raise ValueError("Input name canot be empty")
            self._name = new_name
        else:
            raise TypeError("Name must be a s String")
            
    @property
    def member_id(self):
        return self._id

    @member_id.setter
    def member_id(self, new_id):
        if isinstance(new_id, int):
            self._id = new_id
        else:
            raise TypeError("Member id must be an integer")

    @property
    def class_id(self):
        return self._class_id

    