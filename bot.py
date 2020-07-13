import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['enter'])
def enter(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add('Да','Пойдем курить?','Куда положить печенье?','Как принимать матпомощь?')
    msg = bot.send_message(message.chat.id, 'У тебя что-то срочное?',reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer)
    
def answer(message):
    keyboard_hider = telebot.types.ReplyKeyboardRemove()
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Что?', reply_markup=keyboard_hider)
    elif message.text == 'Пойдем курить?':
        bot.send_message(message.chat.id, 'Позже', reply_markup=keyboard_hider)
    elif message.text == 'Куда положить печенье?':
        bot.send_message(message.chat.id, 'В тарелку с печеньем', reply_markup=keyboard_hider)
    elif message.text == 'Как принимать матпомощь?':
        bot.send_message(message.chat.id, 'Проверить в заявлении подпись учебной части, подпись студента, копию паспорта студента. Далее надо положить заявление в соответствующий лоток', reply_markup=keyboard_hider)
    

if __name__ == '__main__':
     bot.infinity_polling()

