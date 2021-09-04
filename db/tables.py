from .db import DB


class Tables(DB):
    def init_all_tables(self, force=False):
        self.init_user(force)

    def init_user(self, force: bool = False):
        conn = self.get_connection()
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS users')

        c.execute('''CREATE TABLE IF NOT EXISTS users (
                id              SERIAL,
                user_id         INTEGER,
                lang            TEXT DEFAULT 'eng',
                wax             TEXT[25],
                email           TEXT,
                balance         FLOAT DEFAULT 15,
                UNIQUE(user_id, wax)
            )
        ''')
        conn.commit()
