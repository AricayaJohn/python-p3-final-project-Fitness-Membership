from models.__init__ import CURSOR, CONN

class Workout:
    all = {}

    def __init__(self, name, trainer, id=None):
        self._name = name
        self._id = id
        self._trainer = trainer

    def __repr__(self):
        return f"Workout Classes name={self.name} id={self.id} trainer={self.trainer}"
    
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
            self._trainer = new_trainer
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
        CURSOR.execute(sql, (self.name, self.trainer))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, trainer):
        member = cls(name, trainer)
        member.save()
        return member

    def update(self):
        """UPDATE the table row"""
        sql = """
            UPDATE workouts
            SET name = ?,
                trainer = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.trainer, self.id))
        CONN.commit()

    def delete(self):
        """Delete row base on id"""
        sql = """
            DELETE FROM workouts
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        """ Returns the row objects in the Workout table"""

        workout = cls.all.get(row[0])
        if workout:
            workout.name = row[1]
            workout.trainer = row[2]
        else:
            workout = cls(row[1], row[2])
            workout.id = row[0]
            cls.all[workout.id] = workout
        return workout

    @classmethod
    def get_all(cls):
        """Return an object/list containing Workout data"""
        sql = """
            SELECT * 
            FROM workouts
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Coresponding Workout row by id"""
        sql = """
            SELECT *
            FROM workouts
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return coresponding workout row by name"""
        sql = """
            SELECT *
            FROM workouts
            WHERE name = ?
        """
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]