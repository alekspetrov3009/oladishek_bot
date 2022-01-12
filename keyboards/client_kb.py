from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
#KeyboardButton - создание кнопки
#ReplyKeyboardRemove - удаление клавиатуры


b1=KeyboardButton('/start')
b2=KeyboardButton('/Меню')
b3=KeyboardButton('/Пробки')
b4=KeyboardButton('Поделиться номером', request_contact=True)
b5=KeyboardButton('Отправить где я', request_location=True)

kb_client=ReplyKeyboardMarkup(resize_keyboard=True)   #этот класс замещает клавиатуру на созданную
#one_time_keyboard=True - сворачивает клавиатуру после нажатия

kb_client.add(b1).row(b2, b3).row(b4,b5) #добавляем кнопки к созданной клавиатуре
#add(b1) - просто кнопки сверху вниз
#insert(b1) - вставить кнопку справа
#row(b1, b2, b3) - в строку 
