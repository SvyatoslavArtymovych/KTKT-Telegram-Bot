from config import bot
from funks import build_handler_dict
from admin_panel import admin_panel
from timetable import timetable
from db import db_manager

db_manager.table_manager.init_all_tables()

from db.db_manager import admin_manager

bot.add_message_handler(build_handler_dict(handler=admin_panel.open_admin_panel, commands=['admin']))
bot.add_message_handler(build_handler_dict(handler=timetable.open_menu, commands=['user']))
bot.register_callback_query_handler(
    callback=admin_panel.inline,
    func=lambda callback: "admin" in callback.data
    )
bot.register_callback_query_handler(
    callback=timetable.inline,
    func=lambda callback: "user" in callback.data
    )


@bot.message_handler(commands=['test'])
def clear(message):
    # from admin_panel import next_step_handlers
    # bot.register_next_step_handler(message, next_step_handlers.new_department)
    bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAIBgmE6RfF3pC_KvD2PbSowloc1idxTAALztDEb3rDZSfR59f6CkrlGAQADAgADcwADIAQ')


@bot.message_handler(content_types=['photo'])
def clear(message):
    print(message.json['photo'][0]['file_id'])


bot.polling(non_stop=True)
