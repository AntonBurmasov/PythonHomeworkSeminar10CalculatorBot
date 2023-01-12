# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования


import complex
import rational
import telebot
import config
import datetime





bot = telebot.TeleBot(config.token)

dtn = datetime.datetime.now()



@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id,
                     '<b>Вас приветствует бот-калькулятор комплексных и рациональных чисел, для списка комманд введите /help.</b>',
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Для работы с рациональными числами введите /rational, для работы с комплексными числами введите /complex')


@bot.message_handler(commands=['rational'])
def bot_rational1(message):
    num = bot.send_message(message.chat.id, 'Введите первую цифру первого числа:')
    bot.register_next_step_handler(num, input_rational1_1)


def input_rational1_1(message):
    global a
    a = message.text
    num1 = bot.send_message(message.chat.id, 'Введите вторую цифру первого числа:')
    bot.register_next_step_handler(num1, input_rational1_2)


def input_rational1_2(message):
    global b
    b = message.text
    num2 = bot.send_message(message.chat.id, 'Введите первую цифру второго числа:')
    bot.register_next_step_handler(num2, input_rational2_1)


def input_rational2_1(message):
    global c
    c = message.text
    num3 = bot.send_message(message.chat.id, 'Введите вторую цифру второго числа:')
    bot.register_next_step_handler(num3, input_rational2_2)


def input_rational2_2(message):
    global d
    d = message.text
    num4 = bot.send_message(message.chat.id, 'Введите знак(+, -, *, /): ')
    bot.register_next_step_handler(num4, input_rational_sign)


def input_rational_sign(message):
    global sign
    sign = message.text

    rational.init(a, b, c, d)
    result = rational.do_it(sign)

    global data
    data = f'{rational.return_x()} {sign} {rational.return_y()} = {result}'
    with open('logdata.txt', 'a') as file:
        file.write(str(dtn.strftime("%d-%m-%Y %H:%M")) + ' ' + message.from_user.username + ' id' + str(message.from_user.id) + ' ' + data + '\n')
    bot.send_message(message.chat.id, data)








@bot.message_handler(commands=['complex'])
def bot_complex1(message):
    num = bot.send_message(message.chat.id, 'Введите первую цифру первого числа:')
    bot.register_next_step_handler(num, input_complex1_1)

def input_complex1_1(message):
    global a
    a = int(message.text)
    num1 = bot.send_message(message.chat.id, 'Введите вторую цифру первого числа:')
    bot.register_next_step_handler(num1, input_complex1_2)

def input_complex1_2(message):
    global b
    b = int(message.text)
    num2 = bot.send_message(message.chat.id, 'Введите первую цифру второго числа:')
    bot.register_next_step_handler(num2, input_complex2_1)

def input_complex2_1(message):
    global c
    c = int(message.text)
    num3 = bot.send_message(message.chat.id, 'Введите вторую цифру второго числа:')
    bot.register_next_step_handler(num3, input_complex2_2)

def input_complex2_2(message):
    global d
    d = int(message.text)
    num4 = bot.send_message(message.chat.id, 'Введите знак(+, -, *, /): ')
    bot.register_next_step_handler(num4, input_complex_sign)

def input_complex_sign(message):
    global sign
    sign = message.text

    complex.init(a, b, c, d)
    result = complex.do_it(sign)

    global data
    data = f'{complex.return_x()} {sign} {complex.return_y()} = {result}'
    with open('logdata.txt', 'a') as file:
        file.write(str(dtn.strftime("%d-%m-%Y %H:%M")) + ' ' + message.from_user.username + ' id' + str(message.from_user.id) + ' ' + data + '\n')

    bot.send_message(message.chat.id, data)





bot.infinity_polling()
