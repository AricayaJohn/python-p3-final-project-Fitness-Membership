from models.__init__ import CURSOR, CONN

class Workout:
    all = {}

    def __init__(self, name, id=None):
        self._name = name
        self._id = id

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

    @classmethod
    def create_table(cls):
        """Create Workout table in company.db"""
        sql = """
            CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            member_id INTEGER,
            FOREIGN KEY (member_id) REFERENCES members(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """Delete existing workout table in company.db"""
        sql = """
            DROP TABLE IF EXISTS workouts;
        """
        CURSOR.execute(sql)
        CONN.commit()

