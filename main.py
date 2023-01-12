import complex
import logger
import rational
import view
import telebot
import config

bot = telebot.TeleBot(config.token)


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
    num4 = bot.send_message(message.chat.id, 'Введите знак:')
    bot.register_next_step_handler(num4, input_rational_sign)


def input_rational_sign(message):
    global sign
    sign = message.text

    rational.init(a, b, c, d)
    result = rational.do_it(sign)

    global data
    data = f'{rational.return_x()} {sign} {rational.return_y()} = {result}'
    logger.log(str(data))
    bot.send_message(message.chat.id, data)








@bot.message_handler(commands=['complex'])
def bot_complex(message):
    bot.send_message(message.chat.id, 'Введите первую часть первого числа:')
    a = int(message.text())
    bot.send_message(message.chat.id, 'Введите вторую часть первого числа:')
    b = int(message.text())
    bot.send_message(message.chat.id, 'Введите первую часть второго числа:')
    c = int(message.text())
    bot.send_message(message.chat.id, 'Введите вторую часть второго числа:')
    d = int(message.text())
    print(message.chat.id, 'Введите знак действия- +, -, *, /.')
    action = message.text()
    complex.init(a, b, c, d)
    result = complex.do_it(action)
    view.view_data(result, 'результат')
    data = f'{complex.return_x()} {action} {complex.return_y()} = {result}'
    bot.send_message(message.chat.id, data)
    logger.log(str(data))


bot.infinity_polling()
