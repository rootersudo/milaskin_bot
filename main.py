import telebot
from telebot import types
import random
bot = telebot.TeleBot('6053910162:AAELq9mxkumdJb0Om-G0o13h1UBDIECTf5U')

def read_score(user_id):
    file = open('res' + str(user_id), 'r')
    score = file.readline()
    file.close()
    return int(score)
def write_score(user_id,score):
    file = open('res' + str(user_id), 'w')
    file.write(str(score))
    file.close()
def promo_write(score):
    file = open('promo', 'w')
    file.write(str(score))
    file.close()

def read_promo():
    file = open('promo', 'r')
    score = file.readline(2)
    file.close()
    return int(score)


score=0
@bot.message_handler(commands=['help'])

def help(message):
    bot.send_message(message.from_user.id,'Введите /start , чтобы запустить бота \nСправа внизу появиться меню управления ботом \nЕсли вы - новый пользователь, то, пожалуйста, зарегестрируйтесь - введите команду /registration,\nДля возвращения в главное меню введите /back')

@bot.message_handler(commands=['registration'])
def reg(message):

    user_id = message.from_user.id
    score=0
    with open('users','r') as f:
        f.seek(0)
        a = f.readlines()
        f.close()

    if str(user_id)+'\n' not in a:
        with open('users','a') as f:
            f.writelines(str(user_id)+'\n')
            f.close()
        write_score(user_id,score)

    else :
        bot.send_message(message.from_user.id,' Вы уже зарегестрированы! ')

@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    global score

    file = open('res' + str(user_id),'r')
    score = file.readline()
    file.close()

    bot.send_message(message.chat.id,'HI!',parse_mode='html')#html-tag and oth..
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    play = types.KeyboardButton('/Играть')
    get_m = types.KeyboardButton('/Получить_деньги')
    deposit = types.KeyboardButton('/Пополнить_баланс')
    money = types.KeyboardButton('/Проверить_счет')
    markup.add(play, get_m, deposit, money)
    bot.send_message(message.from_user.id, "Твой id: " + str(user_id), reply_markup=markup)

@bot.message_handler(commands=['back'])
def start(message):

    user_id = message.from_user.id

    global score

    file = open('res' + str(user_id),'r')
    score = file.readline()
    file.close()


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    play = types.KeyboardButton('/Играть')
    get_m = types.KeyboardButton('/Получить_деньги')
    deposit = types.KeyboardButton('/Пополнить_баланс')
    money = types.KeyboardButton('/Проверить_счет')

    markup.add(play, get_m, deposit, money)
    bot.send_message(message.from_user.id, "Твой счет -> " + str(score), reply_markup=markup)

@bot.message_handler(commands=(['Играть']))
def get_text_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    one_sev=types.KeyboardButton('/1-7')
    eigh_fiv=types.KeyboardButton('/8-14')
    sex_twthr=types.KeyboardButton('/15-21')
    back = types.KeyboardButton('/back')
    markup.add(one_sev,eigh_fiv,sex_twthr,back)
    bot.send_message(message.from_user.id, 'Удачи!', reply_markup=markup)

@bot.message_handler(commands=(['Пополнить_баланс']))
def get_text_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back = types.KeyboardButton('/back')
    markup.add(back)
    bot.send_message(message.from_user.id, 'в разработке')
    bot.send_message(message.from_user.id, '')
    bot.send_message(message.from_user.ID,'',reply_markup=markup)

@bot.message_handler(commands=['Проверить_счет'])
def mess(message):

    user_id = message.from_user.id
    score = read_score(user_id)
    bot.send_message(message.from_user.id,"Ваш счет -> "+str(score))

@bot.message_handler(commands=(['Получить_деньги']))
def get_money(message):
    user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back = types.KeyboardButton('/back')
    markup.add(back)
    bot.send_message(message.from_user.id,"Введите промокод",reply_markup=markup)


    @bot.message_handler(commands=(['Daily_Bonus']))
    def bonus(message1):
        global score
        flag = read_promo()
        if flag<5:
            score=read_score(user_id)
            score+=random.Random().randint(1,25)
            write_score(user_id,score)
            flag+=1
            promo_write(flag)
            bot.send_message(message1.from_user.id,"Ваш счет -> "+str(score))
        else:
            flag += 1
            promo_write(flag)
            bot.send_message(message1.from_user.id,"Лимит на промокод исчерпан\nПромокод пользователи суммарно вводили "+str(flag)+" раз (")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)
        bot.send_message(message1.from_user.id,"/back для возврата в меню)",reply_markup=markup)



@bot.message_handler(commands=['1-7'])
def ch(message):
    user_id = message.from_user.id

    score = read_score(user_id)
    score = int(score)

    if score < 100:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)

        bot.send_message(message.from_user.id, "Недостаточно средств, пополните баланс",reply_markup=markup)
    else:
        res = random.Random().randint(1, 21)

        if res < 8 :
            bot.send_message(message.from_user.id, 'Поздравляем с выигрышем) ')
            score += 221

        else:
            bot.send_message(message.from_user.id, 'Прости, ты проиграл( ')
            score -= 100
        write_score(user_id,score)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)

        bot.send_message(message.from_user.id,"Выпало число -> "+str(res)+"\nВаш счет -> "+str(score),reply_markup=markup)

@bot.message_handler(commands=['8-14'])
def ch(message):
    user_id = message.from_user.id

    score = read_score(user_id)
    score = int(score)

    if score<100:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)
        bot.send_message(message.from_user.id, "Недостаточно средств, пополните баланс",reply_markup=markup)
    else:
        res = random.Random().randint(1, 21)

        if res < 15 and res>7 :
            bot.send_message(message.from_user.id, 'Поздравляем с выигрышем) ')
            score += 221

        else:
            bot.send_message(message.from_user.id, 'Прости, ты проиграл( ')
            score -= 100
        write_score(user_id,score)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)
        bot.send_message(message.from_user.id,"Выпало число -> "+str(res)+"\nВаш счет -> "+str(score),reply_markup=markup)

@bot.message_handler(commands=['15-21'])
def ch(message):
    user_id = message.from_user.id

    score = read_score(user_id)

    score = int(score)
    if score<100:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)
        bot.send_message(message.from_user.id, "Недостаточно средств, пополните баланс",reply_markup=markup)
    else:
        res = random.Random().randint(1, 21)

        if res < 22 and res>14 :
            bot.send_message(message.from_user.id, 'Поздравляем с выигрышем) ')
            score += 221

        else:
            bot.send_message(message.from_user.id, 'Прости, ты проиграл( ')
            score -= 100
        write_score(user_id,score)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('/back')
        markup.add(back)
        bot.send_message(message.from_user.id,"Выпало число -> "+str(res)+"\nВаш счет -> "+str(score),reply_markup=markup)



bot.polling(none_stop=True)
