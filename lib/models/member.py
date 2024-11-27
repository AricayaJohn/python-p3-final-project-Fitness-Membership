from models.__init__ import CONN, CURSOR
from models.workout_class import Workout

class Member:
    all = {}

    def __init__(self, name, email, workout_id, id=None):
        self.id = id
        self.name = name
        self.email = email
        self._workout_id = workout_id

    # def __repr__(self):
    #     return (
    #         f"<Member name={self.name} email={self.email} id={self.id} " + 
    #         f"Workout ID: {self.workout_id}>"
    #     )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            if new_name[0].isupper():
                self._name = new_name
            else:
                raise ValueError("""
                Name must start with a capital letter
                """)
        else:
            raise TypeError("Name must have String value")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email): 
        if isinstance(new_email, str) and '@' in new_email: 
            if hasattr(new_email, '__contains__') and '.com' in new_email:
                self._email = new_email 
            else:
                raise ValueError("Email must contain '.com' ")
        else: 
            raise ValueError("Email must be a string containing '@'")

    @property
    def workout_id(self):
        return self._workout_id

    @workout_id.setter
    def workout_id(self, workout_id):
        if type(workout_id) is int and Workout.find_by_id(workout_id):
            self._workout_id = workout_id
        else:
            raise ValueError(
                "Workout_id must reference a workout in the database"
            )

    @classmethod
    def create_table(cls):
        """Create Member table in company.db"""
        sql = """
            CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            workout_id INTEGER)
         """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the existing Member table in company.db"""
        sql = """
            DROP TABLE IF EXISTS members;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO members (name, email, workout_id)
            VALUES(?,?, ?)
        """
        CURSOR.execute(sql, (self.name, self.email, self.workout_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email, workout_id):
        member = Member(name, email, workout_id)
        member.save()

        return member

    def update(self):
        sql = """
            UPDATE members
            SET name = ?,
                email = ?,
                workout_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.email, self.workout_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM members
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        member = cls.all.get(row[0])
        if member:
            member.name = row[1]
            member.email = row[2]
            member.workout_id = row[3]
        else:
            member = cls(row[1], row[2], row[3])
            member.id = row[0]
            cls.all[member.id] = member
        return member

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM members
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM members
            WHERE id = ?
            LIMIT 1 
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM members
            WHERE name = ?
        """
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_member_by_workout(cls, workout_id):
        sql = """
            SELECT * FROM members
            Where workout_id = ?
        """
        rows = CURSOR.execute(sql, (workout_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]