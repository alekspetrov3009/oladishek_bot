from aiogram import Bot
from aiogram.dispatcher import Dispatcher, storage
import os
#импорт из библы класса сохранения в оперативной памяти
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
#MemoryStorage - сохранение в оперативке

storage=MemoryStorage()

bot = Bot(token = os.getenv('TOKEN'))  #Получить токен
dp = Dispatcher(bot, storage=storage)

