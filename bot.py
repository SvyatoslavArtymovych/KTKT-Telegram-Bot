import telebot

import db
import keyboards
import timetable


db.get_connection()
db.init_db()

#bot = telebot.TeleBot('*') # test
bot = telebot.TeleBot('*') # main


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю, {0.first_name} ! \nЯ створений, щоб допомагати тобі орієнтуватися по навчальному процесі.'.format(message.from_user, bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id, "Якщо ти знайшов помилку напиши моєму творцю:  @P0wer_bla4er", reply_markup=keyboards.main_keyboard)
    db.new_user(user_id=message.chat.id)
    db.search_teacher_mode(message.chat.id, 'off')


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == '📋розклад пар':
        bot.send_message(message.chat.id, 'Виберіть відділення', reply_markup=keyboards.faculty_keyboard)

    elif message.text.lower() == '⏳розклад дзвінків':
        bot.send_message(message.chat.id, str(timetable.lesson_time + timetable.break_time), parse_mode="HTML")

    elif message.text.lower() == '📆розклад парних/непарних тижнів':
        bot.send_message(message.chat.id, timetable.month)

    elif message.text.lower() == '🎓корисні посилання':
        bot.send_message(message.chat.id, 'Виберіть потрібне посилання⬇️', reply_markup=keyboards.links_keyboard)

    elif message.text.lower() == '👨🏻‍🏫👩🏻‍🏫 викладачі':
        bot.send_message(message.chat.id, 'Я допоможу тобі дізнатись як звати викладача. Напиши мені його прізвище', reply_markup=keyboards.back_keyboard)
        db.search_teacher_mode(message.chat.id, 'on')

    elif message.text.lower() == '📔методички до лабораторних/практичних робіт':
        bot.send_message(message.chat.id, 'Виберіть відділення', reply_markup=keyboards.faculty_techniques)

# Методички вибыр відділення:
    elif message.text.lower() == 'ok':
        bot.send_message(message.chat.id, 'Виберіть відділення', reply_markup=keyboards.discipline_ok)

    elif message.text.lower() == 'зi':
        bot.send_message(message.chat.id, 'Виберіть відділення', reply_markup=keyboards.discipline_zi)

    elif message.text.lower() == 'тo':
        bot.send_message(message.chat.id, 'Виберіть відділення', reply_markup=keyboards.discipline_to)

    elif message.text in keyboards.ok_files_id:
        bot.send_document(message.chat.id, keyboards.ok_files_id[message.text])
#------------------
    elif message.text.lower() == 'на початок':
        bot.send_message(message.chat.id, "Повертаю на початок", reply_markup=keyboards.main_keyboard)
        db.search_teacher_mode(message.chat.id, 'off')

    elif message.text.lower() == 'список відділень':
        bot.send_message(message.chat.id, "Повертаю до списку відділень", reply_markup=keyboards.faculty_keyboard)

    elif message.text.lower() == 'ок':
        bot.send_message(message.chat.id, 'Виберіть групу', reply_markup=keyboards.ok_groups_keyboard)

    elif message.text.lower() == 'зі':
        bot.send_message(message.chat.id, 'Виберіть групу', reply_markup=keyboards.zi_groups_keyboard)

    elif message.text.lower() == 'то':
        bot.send_message(message.chat.id, 'Виберіть групу', reply_markup=keyboards.to_groups_keyboard)

    elif message.text.lower() == 'статистика':
        bot.send_message(message.chat.id, 'Кількість студентів які запускали бота = %s' % db.check_statisctic())


# OK Groups
    elif message.text.lower() == 'ок-11':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_11', message.chat.id)

    elif message.text.lower() == 'ок-12':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_12', message.chat.id)

    elif message.text.lower() == 'ок-21':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_21', message.chat.id)

    elif message.text.lower() == 'ок-22':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_22', message.chat.id)

    elif message.text.lower() == 'ок-31':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_31', message.chat.id)

    elif message.text.lower() == 'ок-32':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_32', message.chat.id)

    elif message.text.lower() == 'ок-41':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_41', message.chat.id)

    elif message.text.lower() == 'ок-42':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('ok_42', message.chat.id)

# zi groups
    elif message.text.lower() == 'зі-11':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_11', message.chat.id)

    elif message.text.lower() == 'зі-12':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_12', message.chat.id)

    elif message.text.lower() == 'зі-13':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_13', message.chat.id)

    elif message.text.lower() == 'зі-21':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_21', message.chat.id)

    elif message.text.lower() == 'зі-22':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_22', message.chat.id)

    elif message.text.lower() == 'зі-31':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_31', message.chat.id)

    elif message.text.lower() == 'зі-32':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_32', message.chat.id)

    elif message.text.lower() == 'зі-41':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_41', message.chat.id)

    elif message.text.lower() == 'зі-42':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('zi_42', message.chat.id)

# to groups
    elif message.text.lower() == 'то-11':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_11', message.chat.id)

    elif message.text.lower() == 'то-12':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_12', message.chat.id)

    elif message.text.lower() == 'то-21':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_21', message.chat.id)

    elif message.text.lower() == 'то-31':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_31', message.chat.id)

    elif message.text.lower() == 'то-32':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_32', message.chat.id)

    elif message.text.lower() == 'то-41':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_41', message.chat.id)

    elif message.text.lower() == 'то-42':
        bot.send_message(message.chat.id, 'Виберіть день', reply_markup=keyboards.days_keyboard)
        db.set_group('to_42', message.chat.id)

    else:
        if(str(db.check_mode(message.chat.id)) == 'on' and str(db.search_teacher(surname=message.text.lower())) != 'None' ):
            bot.send_message(message.chat.id, str(db.search_teacher(surname=message.text.lower())))
        else:
            bot.send_message(message.chat.id, 'Я такого не знаю🥺')

# Інлайн клавіатура
@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    try:
        if c.data == 'mon':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=str(timetable.check(c.message.chat.id, 'mon')), reply_markup=keyboards.days_keyboard)

        if c.data == 'tue':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=str(timetable.check(c.message.chat.id, 'tue')), reply_markup=keyboards.days_keyboard)

        if c.data == 'wed':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=str(timetable.check(c.message.chat.id, 'wed')), reply_markup=keyboards.days_keyboard)

        if c.data == 'thu':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=str(timetable.check(c.message.chat.id, 'thu')), reply_markup=keyboards.days_keyboard)

        if c.data == 'fri':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=str(timetable.check(c.message.chat.id, 'fri')), reply_markup=keyboards.days_keyboard)

    except:
        print('Inline keyboard error, user: %i' % c.message.chat.id)


bot.polling()

