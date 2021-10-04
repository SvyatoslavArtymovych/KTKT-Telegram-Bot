from .db import DB


class TimeTable(DB):
    def get_departments(self):
        return self.execute_sql(f'SELECT id, name FROM departments '
                                f'ORDER BY name asc')

    def get_groups(self, department_id: int, year: int):
        return self.execute_sql(f'SELECT id, name FROM groups '
                                f'WHERE department_id = {department_id} and year = {year} '
                                f'ORDER BY name asc')

    def get_years(self, department_id: int):
        return self.execute_sql(f'SELECT id, year FROM years '
                                f'WHERE department_id = {department_id} '
                                f'ORDER BY id asc')

    def add_timetable(self, group_id: int, day: str, file_id: str):
        self.execute_sql(f"INSERT INTO timetable (day, group_id, file_id) "
                         f"VALUES ('{day}', '{group_id}', '{file_id}') "
                         f"ON CONFLICT (group_id, day) "
                         f"DO UPDATE set file_id = '{file_id}'")













