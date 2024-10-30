from models.__init__ import CONN, CURSOR

class Member:

    all = []

    def __init__(self, name, member_id=None):
        self.name = name
        self.member_id = member_id
        Member.all.append(self)

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
        return self._member_id

    @member_id.setter
    def member_id(self, new_member_id):
        if isinstance(new_member_id, int):
            self._member_id = new_member_id
        else:
            raise TypeError("Member id must be an integer")

    def __repr__(self):
        return f"Member name={self.name} member_id={self.id}"