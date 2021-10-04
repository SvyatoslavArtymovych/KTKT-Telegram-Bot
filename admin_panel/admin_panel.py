from config import *
from . import keyboards
from . import next_step_handlers


def open_admin_panel(message):
    if message.chat.id in admins:
        bot.send_message(message.chat.id, 'Адмін панель', reply_markup=keyboards.menu())
    else:
        bot.send_message(message.chat.id, 'Заборонено')


def inline(c):
    if 'admin' not in c.data:
        return
    c.data = c.data[c.data.index('|')+1:].strip()
    callback_data = c.data.split()

    print(callback_data)

    if 'settings' in callback_data or 'admin_menu' in callback_data:
        bot.edit_message_text(chat_id=c.from_user.id,
                              message_id=c.message.message_id,
                              text='Виберіть пункт:',
                              reply_markup=keyboards.settings('settings'))

    elif 'department' in callback_data:
        if callback_data[-1] == 'department':
            bot.edit_message_text(chat_id=c.from_user.id,
                                  message_id=c.message.message_id,
                                  text='Виберіть пункт:',
                                  reply_markup=keyboards.department('admin_menu'))

        elif callback_data[-1] == 'add_dep':
            bot.send_message(c.from_user.id, 'Введіть назву нового відділення', reply_markup=keyboards.cancel())
            bot.delete_message(c.from_user.id, c.message.message_id)

            bot.register_next_step_handler(c.message, next_step_handlers.new_department)

        elif callback_data[-1] == 'edit':
            bot.edit_message_text(chat_id=c.from_user.id,
                                  message_id=c.message.message_id,
                                  text='Список курсів цього відділення\n\nВиберіть пункт:',
                                  reply_markup=keyboards.years('department', callback_data[-2]))

        elif callback_data[-1] == 'year':
            bot.edit_message_text(chat_id=c.from_user.id,
                                  message_id=c.message.message_id,
                                  text=f'Список груп цього відділення, {callback_data[-2]} курсу\n\n'
                                       f'Виберіть пункт:',
                                  reply_markup=keyboards.groups('department edit',
                                                                callback_data[-3],
                                                                callback_data[-2]))

        elif callback_data[-1] == 'add_group':
            bot.send_message(c.from_user.id, 'Введіть назву нової групи', reply_markup=keyboards.cancel())
            bot.delete_message(c.from_user.id, c.message.message_id)

            bot.register_next_step_handler(c.message,
                                           next_step_handlers.new_group,
                                           callback_data[-3],
                                           callback_data[-2])

        elif callback_data[-1] == 'group':
            bot.edit_message_text(chat_id=c.from_user.id,
                                  message_id=c.message.message_id,
                                  text='Виберіть день, щоб показати розклад',
                                  reply_markup=keyboards.days(f'{callback_data[-2]} edit', callback_data[-2]))

    elif 'set_timetable' in callback_data:
        if callback_data[0] == 'set_timetable':
            bot.send_message(c.from_user.id, 'А тепер відправ розклад ЦІЄЇ групи в ЦЕЙ день',
                             reply_markup=keyboards.cancel())
            bot.delete_message(c.from_user.id, c.message.message_id)

            bot.register_next_step_handler(c.message,
                                           next_step_handlers.add_timetable,
                                           callback_data[-2],
                                           callback_data[-1])











