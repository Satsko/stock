import telebot
from telebot import types
from random import shuffle
import views
import ast
import re


#def set_user_game(chat_id, estimated_answer):

#def finish_user_game(chat_id):

#def get_answer_for_user(chat_id):



def generate_markup(right_answer, wrong_answers):

    markup = types.InlineKeyboardMarkup()
    r_a = re.sub(r'[()]','', str(right_answer))
    w_a = re.sub(r'[()]','', str(wrong_answers))
    r_a = re.sub(r',]',']', r_a)
    w_a = re.sub(r',]',']', w_a)
    r_a = re.sub(r',',"','", r_a)
    w_a = re.sub(r',',"','", w_a)
    list_r = ast.literal_eval(r_a)
    list_w = ast.literal_eval(w_a)
    list_w.extend(list_r)
    shuffle(list_w)
    for item in list_w:
        #markup.add(item)
        markup.add(telebot.types.InlineKeyboardButton(text=item,callback_data=item))
        #print(item)
    return markup

