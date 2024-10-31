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
            self._member_id = new_id
        else:
            raise TypeError("Workout session number")
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        if isinstance(new_id, int):
            self._id = new_id
        else:
            raise TypeError("Id must be a number")

    @classmethod
    def create_table(cls):
        """Create Workout table in company.db"""
        sql = """
            CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            member_id INTEGER,
            FOREIGN KEY (member_id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """Delete existing workout table in company.db"""
        sql = """
            DROP TABLEif EXISTS workouts;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
