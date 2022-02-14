import telebot
from decouple import config
from telebot import types
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)


@bot.message_handler(commands=["start", "hi", "Hi"])
def answer_start(message):
    text = f"Добро пожаловать в Автосервис Rent cars Bishkek!" \
           f"Выберите кузов желаемой машины:"
    keyboard_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Внедорожник', callback_data='Внедорожник')
    btn_2 = types.InlineKeyboardButton(text='Седан', callback_data='Седан')
    keyboard_in.add(btn_1, btn_2)
    bot.send_photo(message.chat.id,
                   photo="https://static.tildacdn.com/tild3863-3363-4136-b564-633036643763/Image00008.jpg")
    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.callback_query_handler(func=lambda call: True)
def send_cource(call):
    if call.data == 'Внедорожник':
        keyboard = InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton('Land Cruiser', callback_data='LandCruiser')
        btn_2 = types.InlineKeyboardButton('Land Cruiser Prado', callback_data='LandCruiserPrado')
        btn_3 = types.InlineKeyboardButton('Harrier', callback_data='Harrier')
        keyboard.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали  {call.data}! Теперь выберите модель машины:'
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
    if call.data == 'Седан':
        keyboard = InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton('Windom', callback_data='Windom')
        btn_2 = types.InlineKeyboardButton('Camry', callback_data='Camry')
        btn_3 = types.InlineKeyboardButton('Prius', callback_data='Prius')
        keyboard.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали  {call.data}! Теперь выберите модель машины:'
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == 'LandCruiser':
        bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}'
                                               ' Ознакомтесь подробнее с характиристиками машины:')

        bot.send_photo(call.message.chat.id,
                       photo="https://s0.rbk.ru/v6_top_pics/resized/1440xH/media/img/4/51/756250743360514.jpg")
        f = open('LandCruiser.txt')
        for line in f:
            bot.send_message(call.message.chat.id, line)
        f.close()
        dostavka(call.message.chat.id)
    if call.data == 'LandCruiserPrado':
        bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}'
                                               ', ознакомтесь подробнее с характиристиками машины:')
        bot.send_photo(call.message.chat.id,
                       photo="http://cdn.motorpage.ru/Photos/800/01a88.jpg")
        f = open('LandCruiserPrado.txt')
        for line in f:
            bot.send_message(call.message.chat.id, line)
        f.close()
        dostavka(call.message.chat.id)

    if call.data == 'Harrier':
        bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}'
                                               ', ознакомтесь подробнее с характиристиками машины:')
        bot.send_photo(call.message.chat.id,
                       photo="https://a.d-cd.net/7b4ad2es-960.jpg")
        f = open('Harrier.txt')
        for line in f:
            bot.send_message(call.message.chat.id, line)
        f.close()
        dostavka(call.message.chat.id)

    if call.data == 'Windom':
        bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}'
                                               ', ознакомтесь подробнее с характиристиками машины:')
        bot.send_photo(call.message.chat.id,
                       photo="https://mezamo.ru/images/toyota-windom-2004-2006-%D1%81%D0%B5%D0%B4%D0%B0%D0%BD/toyota-windom-2004-2006-sedan.jpg")
        f = open('Windom.txt')
        for line in f:
            bot.send_message(call.message.chat.id, line)
        f.close()
        dostavka(call.message.chat.id)
    if call.data == 'Camry':
        bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}'
                                               ', ознакомтесь подробнее с характиристиками машины:')
        bot.send_photo(call.message.chat.id,
                       photo="https://carsdo.ru/job/CarsDo/photo-gallery/toyota/camry-1-1.jpg")
        f = open('Camry.txt')
        for line in f:
            bot.send_message(call.message.chat.id, line)
        f.close()
        dostavka(call.message.chat.id)
    if call.data == 'Prius':
        bot.send_message(call.message.chat.id, f'Вы выбрали {call.data}'
                                               ', ознакомтесь подробнее с характиристиками машины:')
        bot.send_photo(call.message.chat.id,
                       photo="https://carsdo.ru/job/CarsDo/photo-gallery/toyota/prius-1-1.jpg")
        f = open('Prius.txt')
        for line in f:
            bot.send_message(call.message.chat.id, line)
        f.close()
        dostavka(call.message.chat.id)

    if call.data == 'salon':
        bot.send_message(call.message.chat.id, "Вы можете забрать машину по адресу:\n"
                                               "г. Бишкек, ул. Суюмбаева, 123, контактные данные: +996555500000")
    if call.data == 'home':
        bot.send_message(call.message.chat.id, "Введите Ваш адрес и контактные данные:")


@bot.message_handler(content_types=['text'])
def send_good_message(message):
    bot.send_message(message.chat.id, "Ожидайте, как только машина приедет, с Вами свяжутся!")


def dostavka(id):   # функция которая вызывается после выбора машины, для выбора пользователем вид доставки
    keyboard = InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Забрать с салона', callback_data='salon')
    btn_2 = types.InlineKeyboardButton('Доставка на дом', callback_data='home')
    keyboard.add(btn_1, btn_2)
    text = 'Как Вы хотите получить машину:'
    bot.send_message(id, text, reply_markup=keyboard)


bot.polling()
