from aiogram import types, Dispatcher
from create_bot import dp, bot
from handlers.data_base import sqlite_db 
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#декоратор
#@dp.message_handler()
#добавляет асинхронность (событе сообщения)
#async def echo_send(message:types.Message):
    #если текст сообщения равен
    #if message.text == 'Привет':         
        #await message.answer('и тебе привет!') 
    #else:
        #await message.reply("i don't know")        
    #ответить на сообщение        
    #await message.reply(message.text)
    #ответить в лс  
        #await bot.send_message(message.from_user.id, 'заебал')    


#добавляем команды

#добавляем асинхронную функцию, если ты не добавлялся к боту, а пишешь через группу
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Шалом', reply_markup=kb_client)
        await message.delete()
    except: 
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/oladishek_bot')
#Просмотр меню на неделю        
@dp.message_handler(commands=['Меню на неделю'])
async def command_menu_week(message: types.message):
    await bot.send_message(message.from_user.id, 'меню') 
       
#Меню из базы
@dp.message_handler(commands=['Меню'])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)
    
#Просмотр пробок в городе    
#@dp.message_handler(commands='Пробки')
async def command_probki(message: types.message):
    await bot.send_message(message.from_user.id, 'пробки')#, reply_markup=ReplyKeyboardRemove())    
    #reply_markup=ReplyKeyboardRemove - удаляет кастомную клаву

def  register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_menu_week, commands=['Меню на неделю'])
    dp.register_message_handler(command_probki, commands=['Пробки'])
    dp.register_message_handler(menu_command, commands=['Меню'])