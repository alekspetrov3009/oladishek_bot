from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#фильтр мата
#@dp.message_handler()         
async def echo(message:types.Message):
    #разделяет текст, провряет знаки пунктуации, делает буквы маленькими и производит транскрипцию
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) !=set():
        await message.reply('Маты запрещены')
        await message.delete()
        
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)