from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from db.db_manager import admin_manager


def cancel():
    kb = ReplyKeyboardMarkup(True)
    kb.row('Відміна')

    return kb


def menu():
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton('Налаштування', callback_data=f'admin| settings'))
    kb.add(InlineKeyboardButton('Розсилка', callback_data=f'admin| mailing'))

    return kb


def settings(position):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton('Відділення', callback_data=f'admin| department'))
    kb.add(InlineKeyboardButton('Розклади', callback_data=f'admin| timetable'))
    kb.add(InlineKeyboardButton('Тексти повідомлень', callback_data=f'admin| message_text'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'admin| {position}'))
    return kb


def department(position):
    kb = InlineKeyboardMarkup()
    departments = admin_manager.get_departments()

    if departments:
        if type(departments) == list:
            for dep_id, dep_name in departments:
                kb.add(InlineKeyboardButton(f'{dep_name}', callback_data=f'admin| department {dep_id} edit'))
        else:
            kb.add(InlineKeyboardButton(f'{departments[0]}', callback_data=f'admin| department {departments[1]} edit'))

    kb.add(InlineKeyboardButton('Додати', callback_data=f'admin| department add_dep'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'admin| {position}'))
    return kb


def years(position, dep_id):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(f'Курс 1', callback_data=f'admin| department {dep_id} 1 year'),
           InlineKeyboardButton(f'Курс 2', callback_data=f'admin| department {dep_id} 2 year'))
    kb.add(InlineKeyboardButton(f'Курс 3', callback_data=f'admin| department {dep_id} 3 year'),
           InlineKeyboardButton(f'Курс 4', callback_data=f'admin| department {dep_id} 4 year'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'admin| {position}'))

    return kb


def groups(position, dep_id: int, year: int):
    kb = InlineKeyboardMarkup()

    groups_list = admin_manager.get_groups(dep_id, year)

    if groups_list:
        if type(groups_list) == list:
            for group_id, group_name in groups_list:
                kb.add(InlineKeyboardButton(f'{group_name}', callback_data=f'admin| department {group_id} group'))
        else:
            kb.add(InlineKeyboardButton(f'{groups_list[1]}', callback_data=f'admin| department {groups_list[0]} group'))

    kb.add(InlineKeyboardButton('Додати', callback_data=f'admin| department {dep_id} {year} add_group'),
           InlineKeyboardButton('Назад', callback_data=f'admin| department {dep_id} edit'))
    return kb


def days(position, group_id: int):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton('ПН', callback_data=f'admin| set_timetable {group_id} mon'),
           InlineKeyboardButton('ВТ', callback_data=f'admin| set_timetable {group_id} tue'))
    kb.add(InlineKeyboardButton('СР', callback_data=f'admin| set_timetable {group_id} wed'),
           InlineKeyboardButton('ЧТ', callback_data=f'admin| set_timetable {group_id} thu'))
    kb.add(InlineKeyboardButton('ПТ', callback_data=f'admin| set_timetable {group_id} fri'))

    kb.add(InlineKeyboardButton('Назад', callback_data=f'admin| {position}'))
    return kb











