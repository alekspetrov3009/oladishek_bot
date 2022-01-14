from aiogram.utils import executor
from create_bot import dp
import runpy
from handlers.data_base import sqlite_db



#Действия при запуске
async def on_startup(_):
    #инфа в консоли
    print('Бот вышел в онлайн')
    runpy.run_module(mod_name='to_json')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


#не отвечать на сообщения, пока бот был не онлайн
executor.start_polling(dp, skip_updates=True, on_startup = on_startup)