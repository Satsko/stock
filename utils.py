from telebot import types
from random import shuffle
import views
from config import database2_name


#def set_user_game(chat_id, estimated_answer):

#def finish_user_game(chat_id):

def get_answer_for_user(chat_id):



def generate_markup(right_answer, wrong_answers):
    markup = types.InlineKeyboardMarkup()
    all_answers = '{},{}'.format(right_answer, wrong_answers)
    list_items = []
    for item in all_answers.split(','):
        list_items.append(item)
    shuffle(list_items)
    for item in list_items:
        markup.add(item)
    return markup
