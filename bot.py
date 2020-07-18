import telebot
import config
import utils
import views
import models
import re

from telebot import types
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')  

n=1
score = 0
init = 0
name = ''

@bot.message_handler(commands=['game'])
def game(message):
    global init
    init = 1
    bot.send_message(message.chat.id, 'Введите ваше имя: ')  
    
    
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global n
    global score
    global name
    bot.answer_callback_query(callback_query_id=call.id, text='...')
    answer=''
    r_ans = str(views.select_point(models.db,n,'right_answer'))
    r_ans = re.sub(r"[(,)]","", r_ans)
    r_ans = r_ans[2 : -2]
    #print(r_ans)
    if call.data == r_ans:
        answer = 'верный'
        #print(str(views.select_point(models.db,n,'score'))[2 : -3])
        score = score + int(str(views.select_point(models.db,n,'score'))[2 : -3])
    else:
        answer = 'неверный'
    bot.send_message(call.message.chat.id, 'Ответ '+call.data+' '+answer+'. Текущий счет: '+str(score))
    n=n+1    
    
    if n<6:
        row = views.select_point(models.db,n,'question')
        row_r = views.select_point(models.db,n,'right_answer')
        row_w = views.select_point(models.db,n,'wrong_answers')
        markup = utils.generate_markup(row_r,row_w)
        bot.send_message(call.message.chat.id, row, reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, 'Игра окончена. Итоговый счет: '+str(score))
        views.add_user(models.db,name,score)
        
@bot.message_handler(content_types=["text"])
def username(message):
    global init
    global name
    if init == 1:
        name = message.text
        init = 0
        #views.add_user(models.db,name)
        global n
        n=1
        #views.init(models.db)
        row = views.select_point(models.db,n,'question')
        row_r = views.select_point(models.db,n,'right_answer')
        row_w = views.select_point(models.db,n,'wrong_answers')
        markup = utils.generate_markup(row_r,row_w)
        bot.send_message(message.chat.id, row, reply_markup=markup)
        #views.close(models.db)


if __name__ == '__main__':
    bot.infinity_polling()
