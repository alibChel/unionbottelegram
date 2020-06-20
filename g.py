import apiai,json
from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Filters


button_start='Оставить отзыв'
button_help='Улучшение Union'
buton_caption='Титры'
game=False

def button_help_handler(update:Update,context:CallbackContext,game):
    update.message.reply_text(
        text='Что бы вы хотели улучшить в Union?',
        reply_markup=ReplyKeyboardRemove(),
    )
def message(message):
    global  response
    request=apiai.ApiAI('44875a454dbd4b0fbbe1613e9240b34d').text_request()
    request.lang='ru'
    request.session_id='session_1'
    request.query=message
    response=json.loads(request.getresponse().read().decode('utf-8'))
    print( response['result']['action'])
    if response['result']['action']=='input.unknown':
        return 'Я на это, не буду отвечать!'
    else:
        return response['result']['fulfillment']['speech']



def help (update:Update,context:CallbackContext):
    update.message.reply_text(
        text='помощи не будет))))))'
    )

def button_start_handler(update:Update,context:CallbackContext):
    update.message.reply_text(
        text=('ну давайте, я готов!'),
        reply_markup=ReplyKeyboardRemove()

    )
def button_caption_handler(update:Update,context:CallbackContext):
    name = 'caption.txt'
    file = open(name, 'r')
    new = file.read()
    update.message.reply_text(
        text=(new),
        reply_markup=ReplyKeyboardRemove()
    )
def start(update:Update,context:CallbackContext):
    update.message.reply_text(
        text='Здраствуйте! Добро пожаловать! Я бот консультант чата Union 😎 вы можете оставить отзыв, или предложить ваше решение по улучшению Union😏 да или просто пообщаться со мной🙂'
    )


def message_handler(update:Update, context:CallbackContext):
    global game
    text=update.message.text
    if text==buton_caption:
        return button_caption_handler(update=update,context=context)
    if text == '/help':
        game=4
        return help(update=update,context=context)
    if text==button_help:
        game=1
        return button_help_handler(update=update,context=context,game=True)
    if text==button_start:
        game=2
        return button_start_handler(update=update,context=context)
    if text=='/start':
        return help(update=update, context=context)


    reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_start),

            ],
            [
            KeyboardButton(text=buton_caption)],

        ],
        resize_keyboard=True
    )
    if game==1:
        update.message.reply_text(
            text='Спасибо!я обязательно попробую внедрить, ваше предложение🧐\nСпасибо, что выбрали Union!\nХотите вернуться в  главное меню? просто напишите мне и я все сделаю🙃',

            )
        game=3
    elif game==2:
        update.message.reply_text(
            text='Спасибо за ваш отзыв! Я обязательно над этим подумаю🤔\n и  постараюсь сделать чат лучше🙃\nСпасибо, что выбрали Union!\nХотите вернуться в главное меню? просто скажите мне и я все сделаю🤓',
            )
        game=3

    else:
        update.message.reply_text(
            text=message(text),
            reply_markup=reply_markup)





def main():
    print('Start')
    updater=Updater(
        token='1164909696:AAE9Do5JqnH-W_3mks1PTpsNwO5IyCQXmRU',
        use_context=True
    )
    print('ko')
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
