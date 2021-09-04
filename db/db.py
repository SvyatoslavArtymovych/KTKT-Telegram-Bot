import psycopg2

import config


class DB:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                database=config.PG_DATABASE,
                user=config.PG_USER,
                password=config.PG_PASSWORD,
                host=config.PG_HOST,
                port=config.PG_PORT
            )
        return self.connection

    def execute_sql(self, query):
        conn = self.get_connection()
        c = conn.cursor()

        c.execute(query)

        try:
            result = c.fetchall()

            if len(result) > 1:
                return result
            elif len(result) == 1:
                return result[0]
        except psycopg2._psycopg.ProgrammingError:
            conn.commit()
