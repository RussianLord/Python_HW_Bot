import telebot
import os, random, glob
from time_dys import show_time
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
user = telebot.types.User(id, is_bot='Бот Доктор Врач',first_name='Тестировщик кода')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Привет')
    item2 = telebot.types.KeyboardButton('Сколько время?')
    markup.add(item1,item2)
    bot.reply_to(message, f"""\
    Привет {user.full_name}, я бот {user.is_bot}.
    В данном варианте ты можешь нажимать на кнопочки для получения определённого результата! Попробуй!\
    """)
    bot.send_message(message.chat.id, 'Выбирай кнопку' ,reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Ну, здарова...')    
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Да')
        item2 = telebot.types.KeyboardButton('Нет')
        markup.add(item1,item2)
        bot.send_message(message.chat.id,f'Хочешь послушать музыку?', reply_markup=markup) 
    elif message.text == 'Сколько время?' :
        bot.send_message(message.chat.id, 'Местное время')
        bot.send_message(message.chat.id, show_time())
    elif message.text == 'Да':
        # bot.send_message(message.chat.id, 'Родила тебя пизда!')  
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Rumble')
        item2 = telebot.types.KeyboardButton('Big Apple')
        item3 = telebot.types.KeyboardButton('Случайная из альбома(11)')
        markup.add(item1,item2, item3)
        bot.send_message(message.chat.id,f'Выбирай одну из 3-х или пусть играет случайная.', reply_markup=markup) 
    elif message.text == 'Нет':
        bot.send_message('/start')
    elif message.text == 'Rumble':
        bot.send_message(message.chat.id, 'Загружается...')
        audio = open(r'songs/Tee Lopes - Rumble in the Zoo.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        bot.clear_step_handler_by_chat_id()
    elif message.text == 'Big Apple':
        bot.send_message(message.chat.id, 'Загружается...')
        audio = open(r'songs/Tee Lopes - Big Apple, 3 PM.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        bot.send_message('/start')
    elif message.text == 'Случайная из альбома(11)':
        bot.send_message(message.chat.id, 'Загружается...')
        files = os.listdir('songs/')
        list = []
        for x in files:
                list.append(x)
        random_song = f'songs/{random.choice(list)}'
        audio = open(random_song,'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()

bot.infinity_polling()