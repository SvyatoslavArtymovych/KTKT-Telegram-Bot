from .db import DB


class AdminPanel(DB):
    def create_department(self, name: str):
        self.execute_sql(f"INSERT INTO departments (name) "
                         f"VALUES ('{name}') "
                         f"ON CONFLICT DO NOTHING")

    def get_departments(self):
        return self.execute_sql(f'SELECT id, name FROM departments '
                                f'ORDER BY name asc')

    def delete_department(self, name):
        self.execute_sql(f'DELETE FROM departments '
                         f'WHERE name=\'{name}\'')

    def create_group(self, name: str, department_id: int, year: int):
        self.execute_sql(f"INSERT INTO groups (name, department_id, year) "
                         f"VALUES ('{name}', {department_id}, {year}) "
                         f"ON CONFLICT DO NOTHING")

    def get_groups(self, department_id: int, year: int):
        return self.execute_sql(f'SELECT id, name FROM groups '
                                f'WHERE department_id = {department_id} and year = {year} '
                                f'ORDER BY name asc')

    def delete_group(self, group_id: int):
        self.execute_sql(f'DELETE FROM groups '
                         f'WHERE id = {group_id}')

    def create_year(self, department_id: int, year: int):
        self.execute_sql(f"INSERT INTO years (department_id, year) "
                         f"VALUES ({department_id}, {year}) "
                         f"ON CONFLICT DO NOTHING")

    def get_years(self, department_id: int):
        return self.execute_sql(f'SELECT id, year FROM years '
                                f'WHERE department_id = {department_id} '
                                f'ORDER BY id asc')

    def delete_year(self, year_id: int):
        self.execute_sql(f'DELETE FROM years '
                         f'WHERE id = {year_id}')

    def add_timetable(self, group_id: int, day: str, file_id: str):
        self.execute_sql(f"INSERT INTO timetable (day, group_id, file_id) "
                         f"VALUES ('{day}', '{group_id}', '{file_id}') "
                         f"ON CONFLICT (group_id, day) "
                         f"DO UPDATE set file_id = '{file_id}'")













