from .db import DB


class User(DB):
    def new_user(self, user_id):
        self.execute_sql(f'INSERT INTO users (user_id) VALUES ({user_id}) '
                         f'ON CONFLICT DO NOTHING')
