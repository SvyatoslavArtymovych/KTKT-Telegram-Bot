from config import bot
from . import keyboards
from db.db_manager import admin_manager


def new_department(message):
    if message.text == 'Відміна':
        bot.send_message(message.chat.id, 'Відмінено')
        bot.send_message(message.chat.id, 'Виберіть пункт',
                         reply_markup=keyboards.department('department'))
    else:
        admin_manager.create_department(message.text)
        bot.send_message(message.chat.id, 'Додано')
        bot.send_message(message.chat.id, 'Виберіть пункт',
                         reply_markup=keyboards.department('department'))


def new_group(message, department_id, year):
    if message.text == 'Відміна':
        bot.send_message(message.chat.id, 'Відмінено')
        bot.send_message(message.chat.id, 'Виберіть пункт',
                         reply_markup=keyboards.department('department'))
    else:
        admin_manager.create_group(department_id=department_id,
                                   year=year,
                                   name=message.text.upper())
        bot.send_message(message.chat.id, 'Додано')
        bot.send_message(message.chat.id, 'Виберіть пункт',
                         reply_markup=keyboards.department('department year'))


def add_timetable(message, group_id, day):
    if message.text == 'Відміна':
        bot.send_message(message.chat.id, 'Відмінено')
        bot.send_message(message.chat.id, 'Виберіть пункт',
                         reply_markup=keyboards.department('department'))
    else:
        try:
            file_id = message.json['photo'][0]['file_id']
            admin_manager.add_timetable(group_id, day, file_id)
            bot.send_message(message.chat.id, 'Додано')
            bot.send_message(message.chat.id, 'Виберіть пункт',
                             reply_markup=keyboards.department('department'))
        except:
            bot.send_message(message.chat.id, 'Не додано')
