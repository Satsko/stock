import telebot
import config
import time
import utils
import views
from telebot import types
bot = telebot.TeleBot(config.token)
bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
n=1
score = 0
@bot.message_handler(commands=['game'])
def game(message):
    db_worker = views(config.database2_name)
    row = db_worker.select_single2(n)
    n=n+1
    markup = utils.generate_markup(row[3], row[4])
    bot.send_message(message.chat.id, row[2], inline_markup=markup)
    #utils.set_user_game(message.chat.id, row[2])
    db_worker.close2()
    

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    db_worker = views(config.database2_name)
    row = db_worker.select_single2(n)
    answer = row[3]
    if message.text == answer:
        bot.send_message(message.chat.id, 'Верно!')
        score=score+row[1]
    else:
       bot.send_message(message.chat.id, 'Неверно', reply_markup=keyboard_hider)
    if n<6:
        n=n+1
        row = db_worker.select_single2(n)
        markup = utils.generate_markup(row[3], row[4])
        bot.send_message(message.chat.id, row[2], inline_markup=markup)
    db_worker.close2()
    # utils.finish_user_game(message.chat.id)   
    bot.send_message(message.chat.id, 'Score: '+str(score))   

if __name__ == '__main__':
    bot.infinity_polling()
