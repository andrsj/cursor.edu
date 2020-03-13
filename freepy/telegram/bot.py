import os
import time
import telebot
from config import TOKEN,KEY


commands = {
    'start'     : '\t Початок використання боту',
    'help'      : '\t Відобразити цей список команд',
    'long'      : '\t Відобразити подію бота (typing...)',
    'sticker'   : '\t Відправити стікер',
    'document'  : '\t Відправити документ',
    'voice'     : '\t Відправити голосове повідомлення',
    'video'     : '\t Відправити відео',
    'videonote' : '\t Відправити відео повідомлення',
    'buttons'   : '\t Відправити кнопки',
    'test'      : '\t Пройти тестування',
    'weather'   : '\t Погода',
    'url'       : '\t URL кнопочка'
}


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)
bot_name = bot.get_me()

info = '''Погодка :) 
Привіт {0.first_name}, 
Я бот <b>{1}</b>
'''

@bot.message_handler(commands = ['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, info.format(m.from_user, bot.get_me().first_name), parse_mode = 'html')
    command_help(m)

@bot.message_handler(commands = ['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Команди: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)

@bot.message_handler(commands = ['long'])
def command_long_text(m):
    cid = m.chat.id
    bot.send_message(cid, "Я пишу...")
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    bot.send_message(cid, "...")

@bot.message_handler(commands = ['sticker'])
def command_sticker(m):
    cid = m.chat.id
    sti = open(os.path.dirname(__file__) + '/static/sticker.webp', 'rb')
    bot.send_sticker(cid, sti)

@bot.message_handler(commands = ['document'])
def command_document(m):
    cid = m.chat.id
    doc = open(os.path.dirname(__file__) + '/static/hi.txt', 'rb')
    bot.send_document(cid, doc)

@bot.message_handler(commands = ['voice'])
def command_voice(m):
    cid = m.chat.id
    voice = open(os.path.dirname(__file__) + '/static/voice.ogg', 'rb')
    bot.send_voice(cid, voice)

@bot.message_handler(commands = ['video'])
def command_video(m):
    cid = m.chat.id
    video = open(os.path.dirname(__file__) + '/static/videonote.mp4', 'rb')
    bot.send_video(cid, video)

@bot.message_handler(commands = ['videonote'])
def command_videonote(m):
    cid = m.chat.id
    videonote = open(os.path.dirname(__file__) + '/static/videonote.mp4', 'rb')
    bot.send_video_note(cid, videonote)

@bot.message_handler(func = lambda message: message.text == "hi")
def command_text_hi(m):
    cid = m.chat.id
    bot.send_message(cid, "Що 'Ні'? Пиши команду або назву міста")

@bot.message_handler(commands = ['buttons'])
def command_buttons(m):
    cid = m.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True)
    itembtna = telebot.types.KeyboardButton('One')
    itembtnb = telebot.types.KeyboardButton('Two')
    itembtnc = telebot.types.KeyboardButton('Three')
    itembtnd = telebot.types.KeyboardButton('Four')
    itembtne = telebot.types.KeyboardButton('Five')
    markup.row(itembtna, itembtnb, itembtnc)
    markup.row(itembtnd, itembtne)
    bot.send_message(cid, "Choose one letter:", reply_markup = markup)

    # custom_keyboard = [ ['top-left', 'top-right'], 
    #                     ['bottom-left', 'bottom-right']]
    # reply_markup = telebot.types.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard = True)
    # bot.send_message(chat_id = cid, text="Custom Keyboard Test", reply_markup = reply_markup)

@bot.message_handler(commands = ['test'])
def command_test(m):
    msg = bot.reply_to(m, "Тест, напиши якусь відповідь:")
    bot.register_next_step_handler(msg, first_step)

def first_step(m):
    try:
        message = m.text
        msg = bot.reply_to(m, "Ти написав '{0}'\nНапиши другу відповідь:".format(message))
        bot.register_next_step_handler(msg, second_step)
    except:
        bot.reply_to(m, 'Oooops')

def second_step(m):
    try:
        message = m.text
        bot.reply_to(m, 'Nice, ти відправив "{0}"'.format(message))
    except:
        bot.reply_to(message, 'Oooops')

@bot.message_handler(commands = ['weather'])
def command_weather(m):
    msg = bot.reply_to(m, "Напиши своє місто:")
    bot.register_next_step_handler(msg, weather_step)

def weather_step(m):
    try:
        message = m.text
        bot.reply_to(m, 'Погода в "{0}"'.format(message))
        bot.send_chat_action(m.chat.id, 'typing')
        time.sleep(2)
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units={2}&lang={3}'.format(message,KEY,'metric','ua-uk')
            import requests
            res = requests.get(url)
            data = res.json()
            urlicon = data['weather'][0]['icon']
            ico = open(os.path.dirname(__file__) + '/png/' + urlicon + '.png', 'rb')
            try:
                weather = f"<b>Опис</b>: {data['weather'][0]['description'].capitalize()}\n"
                weather += f"<u>Температура:</u> {data['main']['temp']}С*\n"
                weather += f"Вітер: <u>Швидкість</u> -> {data['wind']['speed']} м/с | "
                weather += f"<u>Кут</u> (0-359) -> {data['wind']['deg']}*\n"
                weather += f"<u>Вологість</u> -> {data['main']['humidity']}%\n\n"
                url = 'http://api.openweathermap.org'
                author = 'tg://user?id=378636870'
                weather += "<u><a href = '{0}'>API</a></u> що було використане by <a href='{1}'>Andrew</a>".format(url,author)
                bot.send_message(m.chat.id, weather, parse_mode = 'html')
            except:
                bot.send_message(m.chat.id, 'Основну інформацію не знайдено')
            bot.send_photo(m.chat.id, ico)
        except:
            bot.send_message(m.chat.id, "Місто не знайдено :(")
    except:
        bot.send_message(m.chat.id, "Ooooops")


@bot.message_handler(commands = ['url'])
def url(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn_my_site= telebot.types.InlineKeyboardButton(text='Автор', url='tg://user?id=378636870')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку і перейди на сторінку автора.", reply_markup = markup)


@bot.message_handler(content_types = ["text"])
def text_write_message(m):
    if "Test" in m.text:
        bot.reply_to(m, "Найдено 'Test'")

@bot.edited_message_handler(content_types = ['text'])
def text_edit_message(m):
    if "Test" in m.text:
        bot.reply_to(m, "Текст змінено на 'Test'")


bot.enable_save_next_step_handlers(delay = 2)
bot.load_next_step_handlers()
bot.polling()