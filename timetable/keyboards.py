from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from db.db_manager import timetable_manager


def menu():
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton('Відділення', callback_data=f'user| department_menu'))

    return kb


def department(position):
    kb = InlineKeyboardMarkup()
    departments = timetable_manager.get_departments()

    if departments:
        if type(departments) == list:
            for dep_id, dep_name in departments:
                kb.add(InlineKeyboardButton(f'{dep_name}', callback_data=f'user| department {dep_id}'))
        else:
            kb.add(InlineKeyboardButton(f'{departments[0]}', callback_data=f'user| department {departments[1]}'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'user| {position}'))
    return kb


def years(position, dep_id):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(f'Курс 1', callback_data=f'user| year {dep_id} 1'),
           InlineKeyboardButton(f'Курс 2', callback_data=f'user| year {dep_id} 2'))
    kb.add(InlineKeyboardButton(f'Курс 3', callback_data=f'user| year {dep_id} 3'),
           InlineKeyboardButton(f'Курс 4', callback_data=f'user| year {dep_id} 4'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'user| {position}'))

    return kb


def groups(position, dep_id: int, year: int):
    kb = InlineKeyboardMarkup()

    groups_list = timetable_manager.get_groups(dep_id, year)

    if groups_list:
        if type(groups_list) == list:
            for group_id, group_name in groups_list:
                kb.add(InlineKeyboardButton(f'{group_name}', callback_data=f'user| group {group_id}'))
        else:
            kb.add(InlineKeyboardButton(f'{groups_list[1]}', callback_data=f'user| group {groups_list[0]}'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'user| department {dep_id}'))
    return kb


def days(position, group_id: int):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton('ПН', callback_data=f'user| get_timetable {group_id} mon'),
           InlineKeyboardButton('ВТ', callback_data=f'user| get_timetable {group_id} tue'),
           InlineKeyboardButton('СР', callback_data=f'user| get_timetable {group_id} wed'))
    kb.add(InlineKeyboardButton('ЧТ', callback_data=f'user| get_timetable {group_id} thu'),
           InlineKeyboardButton('ПТ', callback_data=f'user| get_timetable {group_id} fri'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'user| {position}'))
    return kb
