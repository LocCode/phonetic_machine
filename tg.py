'''
This is the module for connecting with Telegram Bot
'''

from telegram.ext import Updater
import logging
import eng_lang
import ru_lang
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler

tg_token = '882261003:AAEsahXWDo6AOkLrfC1NbfVEUF7v0Ki0CiY'
updater = Updater(token=tg_token, use_context=True)
dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! This bot can make a phonetic analysis of any English word. "
                                                                  "\n Just enter /eng and type the word. \n For example: /eng Apple "
                                                                  "\n\nПривет! Этот бот может сделать фонетический анализ любого русского слова."
                                                                  "\n Всего лишь введите /ru и ваше слово. Например: /ru Яблоко")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


'''
The command /eng receives English word and make phonetic analysis of it
'''


def eng(update, context):

    word = update.message.text.replace("/eng", "").strip()

    if word != "":
        result = eng_lang.get_english_word(word)
        context.bot.send_message(chat_id=update.message.chat_id, text=result)

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="No word has been sent.\nExample: /eng Apple.")


eng_handler = CommandHandler('eng', eng)
dispatcher.add_handler(eng_handler)


'''
The command /ru receives Russian word and make phonetic analysis of it
'''


def ru(update, context):

    word = update.message.text.replace("/ru", "").strip()

    if word != "":
        result = ru_lang.get_russian_word(word)
        context.bot.send_message(chat_id=update.message.chat_id, text=result)

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Вы не послали никакого слова.\nПример: /eng Apple.")


ru_handler = CommandHandler('ru', ru)
dispatcher.add_handler(ru_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.\nИзвините, но я не знаю такой команды.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

#updater.stop()