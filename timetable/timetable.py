from config import bot
from . import keyboards
from . import next_step_handlers


def open_menu(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=keyboards.menu())


def inline(c):
    if 'user' not in c.data:
        return
    c.data = c.data[c.data.index('|')+1:].strip()
    callback_data = c.data.split()
    print(callback_data)

    if callback_data[-1] == 'department_menu':
        bot.edit_message_text(chat_id=c.from_user.id,
                              message_id=c.message.message_id,
                              text='Виберіть пункт:',
                              reply_markup=keyboards.department('timetable_menu'))

    elif callback_data[0] == 'department':
        bot.edit_message_text(chat_id=c.from_user.id,
                              message_id=c.message.message_id,
                              text='Виберіть курс:',
                              reply_markup=keyboards.years('department_menu', callback_data[1]))

    elif callback_data[0] == 'year':
        bot.edit_message_text(chat_id=c.from_user.id,
                              message_id=c.message.message_id,
                              text='Виберіть групу:',
                              reply_markup=keyboards.groups('timetable_menu', callback_data[1], callback_data[-1]))

    elif callback_data[0] == 'group':
        bot.edit_message_text(chat_id=c.from_user.id,
                              message_id=c.message.message_id,
                              text='Виберіть день:',
                              reply_markup=keyboards.days('department_menu', callback_data[1]))





