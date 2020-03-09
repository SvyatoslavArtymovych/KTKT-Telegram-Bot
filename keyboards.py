import telebot




main_keyboard = telebot.types.ReplyKeyboardMarkup(True)
main_keyboard.row('📋Розклад пар')
main_keyboard.row('⏳Розклад дзвінків', '📆Розклад парних/непарних тижнів')
main_keyboard.row('📔Методички до лабораторних/практичних робіт')
main_keyboard.row('🎓Корисні посилання')
main_keyboard.row('👨🏻‍🏫👩🏻‍🏫 Викладачі')

back_keyboard = telebot.types.ReplyKeyboardMarkup(True)
back_keyboard.row('На початок')

faculty_keyboard = telebot.types.ReplyKeyboardMarkup(True)
faculty_keyboard.row('ОК', 'ЗІ', 'ТО')
faculty_keyboard.row('На початок')

# Groups
ok_groups_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
ok_groups_keyboard.row('ОК-11', 'ОК-12')
ok_groups_keyboard.row('ОК-21', 'ОК-22')
ok_groups_keyboard.row('ОК-31', 'ОК-32')
ok_groups_keyboard.row('ОК-41', 'ОК-42')
ok_groups_keyboard.row('Список відділень', 'На початок')

zi_groups_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
zi_groups_keyboard.row('ЗІ-11', 'ЗІ-12', 'ЗІ-13')
zi_groups_keyboard.row('ЗІ-21', 'ЗІ-22')
zi_groups_keyboard.row('ЗІ-31', 'ЗІ-32')
zi_groups_keyboard.row('ЗІ-41', 'ЗІ-42')
zi_groups_keyboard.row('Список відділень', 'На початок')

to_groups_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
to_groups_keyboard.row('ТО-11', 'ТО-12')
to_groups_keyboard.row('ТО-21')
to_groups_keyboard.row('ТО-31', 'ТО-32')
to_groups_keyboard.row('ТО-41', 'ТО-42')
to_groups_keyboard.row('Список відділень', 'На початок')


# Клавіатура з днями тижня
days_keyboard = telebot.types.InlineKeyboardMarkup()
monday = telebot.types.InlineKeyboardButton(text="Пн", callback_data='mon')
tuesday = telebot.types.InlineKeyboardButton(text="Вт", callback_data='tue')
wednesday = telebot.types.InlineKeyboardButton(text="Ср", callback_data='wed')
thursday = telebot.types.InlineKeyboardButton(text="Чт", callback_data='thu')
friday = telebot.types.InlineKeyboardButton(text="Пт", callback_data='fri')
days_keyboard.add(monday, tuesday, wednesday, thursday, friday)


links_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
our_site = telebot.types.InlineKeyboardButton(text='🌐 Наш сайт', url='https://www.ktkt.com.ua/')
news = telebot.types.InlineKeyboardButton(text='📰 Новини', url='https://www.ktkt.com.ua/?page_id=1219')
scholarship = telebot.types.InlineKeyboardButton(text='💸 Стипендія', url='https://www.ktkt.com.ua/?page_id=2717')
photos = telebot.types.InlineKeyboardButton(text='📸 Фото', url='https://www.ktkt.com.ua/?page_id=430')
youtube = telebot.types.InlineKeyboardButton(text='📺 YouTube', url='https://www.youtube.com/channel/UCOd1kVIz5AoAhgv-7fnb1Gg')
instagram_main = telebot.types.InlineKeyboardButton(text='📱 Instagram', url='https://www.instagram.com/ktktnulp/')
instagram_topktkt = telebot.types.InlineKeyboardButton(text='🔝 Топ КТКТ (Instagram)', url='https://www.instagram.com/top_ktkt/')
links_keyboard.add(our_site, news, scholarship, photos, youtube, instagram_topktkt, instagram_main)


# Для методичок:
faculty_techniques = telebot.types.ReplyKeyboardMarkup(True)
faculty_techniques.row('OK', 'ЗI', 'ТO')
faculty_techniques.row('На початок')

discipline_ok = telebot.types.ReplyKeyboardMarkup(True)
discipline_ok.row('Алгоритми та МО', 'Дискретна математика')
discipline_ok.row('Електрорадіовимірювання', 'Інформатика')
discipline_ok.row('Комп\'ютерні системи та мережі')
discipline_ok.row('Операційні системи', 'Н, Д та Е КС та М')
discipline_ok.row('Організація баз даних', 'Основи Інформатики')
discipline_ok.row('Периферійні пристрої', 'Системне програмування')
discipline_ok.row('Програмування в Internet', 'Програмування')
discipline_ok.row('На початок')

discipline_zi = telebot.types.ReplyKeyboardMarkup(True)
discipline_zi.row('АЗІ та їх Експлуатація', 'Глобальні мережі зв\'язку')
discipline_zi.row('Інженерна та комп\'ютерна графіка')
discipline_zi.row('Пeриферійні пристрої', 'Прoграмування в Internet')
discipline_zi.row('Сиcтемне програмування')
discipline_zi.row('Програмно-апаратні засоби локальних комп\'ютерних мереж')
discipline_zi.row('Оcнови Інформатики', 'Основи схемотехніки')
discipline_zi.row('Oб\'єктно Орієнтоване Програмування', 'OБД')
discipline_zi.row('Інформаційні ресурси Internet', 'Мережні операційні системи')
discipline_zi.row('Інформатика 2018-2019', 'Iнформатика_м.с')
discipline_zi.row('На початок')

discipline_to = telebot.types.ReplyKeyboardMarkup(True)
discipline_to.row('Засоби ОТ та їх ТО')
discipline_to.row('Об\'єктно Орієнтоване Програмування', 'Cистемне програмування')
discipline_to.row('Цифрові СК та їх ТО', 'Компї\'ютерні мережі')
discipline_to.row('Oснови Інформатики', 'ОБД')
discipline_to.row('Обладнання інформаційних мереж та їх ТО')
discipline_to.row('Інформатика_м.с', 'Iнформатика 2018-2019')
discipline_to.row('На початок')

ok_files_id = {
    'Алгоритми та МО': 'BQACAgIAAxkDAAJgr15mmPqjL2rAX-MYutbnxH8XscXRAALOBQACDcwwS4PqX2y_VlzVGAQ',
    'Дискретна математика': 'BQACAgIAAxkDAAJgsl5mmRUObT1rbSoVdRnWaPs9CtEbAALQBQACDcwwS36L0A5NYaJIGAQ',
    'Електрорадіовимірювання': 'BQACAgIAAxkDAAJgtV5mmRhvDhcUU3j3GTNFB6ujcD8zAALRBQACDcwwS0kyS-S81WwjGAQ',
    'Інформатика': 'BQACAgIAAxkDAAJguF5mmRygriaeSsCJNRrswXthbaK4AALSBQACDcwwS3PHGaTlRtbqGAQ',
    'Комп\'ютерні системи та мережі': 'BQACAgIAAxkDAAJgu15mmSfV4ppYh35q7LublPhLayI6AALUBQACDcwwS63fe41fpfEIGAQ',
    'Н, Д та Е КС та М': 'BQACAgIAAxkDAAJgvl5mmS_otCSRRgnMHk5n7rin4I4HAALVBQACDcwwS4gU9J7k_P1hGAQ',
    'Операційні системи': 'BQACAgIAAxkDAAJgwV5mmTdQbTs0E3nQiUUn7zkMvYwnAALWBQACDcwwSxdqJX5YLbN9GAQ',
    'Організація баз даних': 'BQACAgIAAxkDAAJgxF5mmTpzQJyyhTATp6wnYkgRGLzJAALXBQACDcwwS-qBoA83NTVTGAQ',
    'Основи Інформатики': 'BQACAgIAAxkDAAJgx15mmT3l-nRvzWjar9XwmpAek_AiAALeBgACago4S6XXjptsGJFUGAQ',
    'Периферійні пристрої': 'BQACAgIAAxkDAAJgyl5mmUHAZ9s5KAGK-zKzPiVCKWD2AALYBQACDcwwSzPFdrWH6jH4GAQ',
    'Системне програмування': 'BQACAgIAAxkDAAJg015mmU3r_FnnmtzAbO6UnZynLM4lAALgBgACago4S9JijadDMG0JGAQ',
    'Програмування в Internet': 'BQACAgIAAxkDAAJgzV5mmUWmnETJTICqsI2mwOMrZ6vWAALZBQACDcwwS39PdoEZw98mGAQ',
    'Програмування': 'BQACAgIAAxkDAAJg0F5mmUlwupFc0hSwxXyCCJgyjwk6AALfBgACago4SwQumTAdXG_gGAQ',

    'АЗІ та їх Експлуатація': 'BQACAgIAAxkDAAJg515mmzQvCdKtoXyfTSvR4OavST68AALeBQACDcwwS46goGFmFhrLGAQ',
    'Глобальні мережі зв\'язку': 'BQACAgIAAxkDAAJg6l5mmz7A0civzSDpEQ20zwYr4QL_AALfBQACDcwwS3XDGufgKCPvGAQ',
    'Інженерна та комп\'ютерна графіка': 'tjLQKDKwM15_HmvPj6iAALgBQACDcwwSwb1UHrVDrCjGAQ',
    'Пeриферійні пристрої': 'BQACAgIAAxkDAAJhCF5mm3b7234rNSSveehr9wVcro2uAALkBgACago4S-z7NW-IrSFrGAQ',
    'Прoграмування в Internet': 'BQACAgIAAxkDAAJhDl5mm4SQ_0jXh0726OXbShIQ2fY6AALlBgACago4S3MbHCzlzRQAARgE',
    'Сиcтемне програмування': 'BQACAgIAAxkDAAJhFl5mnDB0y-3oSZX_bQIf3ppjgjwPAALnBQACDcwwS2B-RenqM5iNGAQ',
    'Програмно-апаратні засоби локальних комп\'ютерних мереж': 'BQACAgIAAxkDAAJhC15mm318psO6j5BCnorBZL4WA2p0AALmBQACDcwwS7p_xR01tPTWGAQ',
    'Оcнови Інформатики': 'BQACAgIAAxkDAAJhAl5mm2Vh6ks2TaZtJHcCXw371eeFAAIFBQACKw84SyoOZ7T6TVMUGAQ',
    'Основи схемотехніки': 'BQACAgIAAxkDAAJhBV5mm3Pjpht_h-mYanjLvooFdhx9AALlBQACDcwwSynDP-embXOJGAQ',
    'Oб\'єктно Орієнтоване Програмування': 'BQACAgIAAxkDAAJg_F5mm120YU3YOP5qjwR1nAZsuCzgAALkBQACDcwwS0K3vjN-5E-3GAQ',
    'OБД': 'BQACAgIAAxkDAAJg_15mm2A7TTOYS0CnmNwJ7bpCDoFgAALjBgACago4S6fJ6YVkK8m_GAQ',
    'Інформаційні ресурси Internet': 'BQACAgIAAxkDAAJg9l5mm1TQSGPYSGY_0C73o3hvvKY_AALiBQACDcwwS1-KDsjvzPWZGAQ',
    'Мережні операційні системи': 'BQACAgIAAxkDAAJg-V5mm1ksEk0TLHIU1RDvbh0kI2GZAALjBQACDcwwS_FXCzbPVgkDGAQ',
    'Інформатика 2018-2019': 'BQACAgIAAxkDAAJg8F5mm0cLLbbui6v0OE2mLlUgisxEAALiBgACago4S8wmFmgfpKAMGAQ',
    'Iнформатика_м.с': 'BQACAgIAAxkDAAJg815mm0rAzj5v-6kkx-gWT6CyauvKAALhBQACDcwwSwksYgUFWeJIGAQ',

    'Засоби ОТ та їх ТО': 'BQACAgIAAxkDAAJhG15mnwr-FmHf39c2MyTC0gxFgtdTAALoBQACDcwwSz0hdZczuT7WGAQ',
    'Об\'єктно Орієнтоване Програмування': 'BQACAgIAAxkDAAJhKF5mn6XCF5OdtMfkAlRGnOf4fgs8AALoBgACago4S-7e0uS6Myp-GAQ',
    'Cистемне програмування': 'BQACAgIAAxkDAAJhNF5mn7YctW9vstU2tNikiWNjUyVHAALvBQACDcwwS-XWHDk34ix5GAQ',
    'Цифрові СК та їх ТО': 'BQACAgIAAxkDAAJhN15mn76--VjGGaxImY-R0SXXnzdNAALwBQACDcwwS2WmRikwKbTOGAQ',
    'Компї\'ютерні мережі': 'BQACAgIAAxkDAAJhJV5mn6BzPlSi-1dIGfltEdAieLvjAALrBQACDcwwSyNq5HzkwTjJGAQ',
    'Oснови Інформатики': 'BQACAgIAAxkDAAJhMV5mn7NFFc39NXEC4aIcewlS4kJBAALuBQACDcwwS_VanJFHDWidGAQ',
    'ОБД': 'BQACAgIAAxkDAAJhLl5mn6tnCVfouR0g4EA4QkdnL8lGAALtBQACDcwwS6ATWhCq1v4jGAQ',
    'Обладнання інформаційних мереж та їх ТО': 'BQACAgIAAxkDAAJhK15mn6oV1G3lmgQDif3YXCgcs9DqAALsBQACDcwwS0GMEpIeydV_GAQ',
    'Інформатика_м.с': 'BQACAgIAAxkDAAJhIV5mnxHWUIyJ5GzsvLpatGbYJ1NsAALqBQACDcwwS6HNOQoORm3JGAQ',
    'Iнформатика 2018-2019': 'BQACAgIAAxkDAAJhHl5mnw7ro5YwKp1UqB1nLDaIpVAJAALpBQACDcwwS7hv6DgAAVN9mBgE'
}


