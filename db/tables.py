from .db import DB


class Tables(DB):
    def init_all_tables(self, force=False):
        self.users(force)
        self.departments(force)
        self.groups(force)
        self.years(force)
        self.timetable(force)

    def users(self, force: bool = False):
        conn = self.get_connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS users')

        c.execute('''CREATE TABLE IF NOT EXISTS users (
                id              SERIAL,
                user_id         INTEGER,
                UNIQUE(user_id)
            )
        ''')
        conn.commit()

    def departments(self, force: bool = False):
        conn = self.get_connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS departments')

        c.execute('''CREATE TABLE IF NOT EXISTS departments (
                id              SERIAL,
                name            VARCHAR,
                UNIQUE(name)
            )
        ''')
        conn.commit()

    def years(self, force: bool = False):
        conn = self.get_connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS years')

        c.execute('''CREATE TABLE IF NOT EXISTS years (
                id              SERIAL,
                year            INT,
                department_id   INT
            )
        ''')
        conn.commit()

    def groups(self, force: bool = False):
        conn = self.get_connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS groups')

        c.execute('''CREATE TABLE IF NOT EXISTS groups (
                id              SERIAL,
                name            VARCHAR,
                year            INT,
                department_id   INT,
                UNIQUE(name)
            )
        ''')
        conn.commit()

    def timetable(self, force: bool = False):
        conn = self.get_connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS timetable')

        c.execute('''CREATE TABLE IF NOT EXISTS timetable (
                id              SERIAL,
                day             VARCHAR,
                group_id        INT,
                file_id         VARCHAR,
                UNIQUE(group_id, day)
            )
        ''')
        conn.commit()