from models.__init__ import CONN, CURSOR

class Member:
    all = {}

    def __init__(self, name, email, id=None):
        self.id = id
        self._name = name
        self._email = email

    def __repr__(self):
        return f"Member name={self.name} email={self.email} id={self.id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise TypeError("Name must have String value")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if isinstance(new_email, str):
            self._email = new_email
        else:
            raise ValueError("Email must be a string")

    @classmethod
    def create_table(cls):
        """Create Member table in company.db"""
        sql = """
            CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT)
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
            INSERT INTO members (name, email)
            VALUES(?,?)
        """
        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        member = Member(name, email)
        member.save()

        return member

    def update(self):
        sql = """
            UPDATE members
            SET name = ?,
                email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.email, self.id))
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

        else:
            member = cls(row[1], row[2])
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