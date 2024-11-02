from models.__init__ import CURSOR, CONN

class Workout:
    all = {}

    def __init__(self, name, trainer, id=None):
        self._name = name
        self._id = id
        self._trainer = trainer

    def __repr__(self):
        return f"Workout Classes name={self.name} id={self.id} trainer ={self.trainer}"
    
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
    def trainer(self):
        return self._trainer

    @trainer.setter
    def trainer(self, new_trainer):
        if isinstance(new_trainer, str) and len(new_trainer) > 0:
            self._new_trainer = new_trainer
        else:
            raise TypeError("Trainer must have string value")

    @classmethod
    def create_table(cls):
        """Create Workout table in company.db"""
        sql = """
            CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            trainer TEXT)
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

    def save(self):
        """Create row instance for workout table"""
        sql = """
            INSERT INTO workouts (name, trainer)
            VALUES(?, ?)
        """