from models.__init__ import CONN, CURSOR

class Member:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self._name = name

    def __repr__(self):
        return f"Member name={self.name} id={self.id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) == 0:
                raise ValueError("Input name canot be empty")
            elif hasattr(self, "_name"):
                raise ValueError("member already has a name")
            self._name = new_name
        else:
            raise TypeError("Name must be a s String")
            



    