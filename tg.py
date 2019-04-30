from telegram.ext import Updater
import logging
import languages
import database
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler


lang = languages.Language()


class Telegram:
    def __init__(self, token='882261003:AAEsahXWDo6AOkLrfC1NbfVEUF7v0Ki0CiY'):  # <-- Telegram token is here
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def send_msg(self, context, chat_id, text):
        context.bot.send_message(chat_id=chat_id,
                                 text=text)

    @staticmethod
    def start(update, context):
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="Hello! This bot can make a phonetic analysis of any English word or sentence. "
                                      "\n Just enter /eng and type the word. \n For example: /eng Apple"
                                      "\n But you may also try to enter the word or sentence without command and the bot will try to detect the language it self."
                                      "\n\nПривет! Этот бот может сделать фонетический анализ любого русского слова или предложения."
                                      "\n Просто введите /ru и ваше слово или предложение."
                                      "\n Но также, вы можете попробовать ввести слово или предложение без команды и бот попытается самостоятельно определить язык.")

    def echo(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=lang.autodetect_lang(update.message))
#TODO: Нужно переписать функцию SET_LANG, так как сейчас в нее передаются все данные о сообщение, но перед фильтром необходимо передать только сообщение
    def ru(self, update, context):
        print(update.message.replace("/ru", ""))
        context.bot.send_message(chat_id=update.message.chat_id, text=lang.set_lang(update.message.replace("/ru", ""), 'ru'))

    def uz(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=lang.set_lang(update.message.replace("/uz", ""), 'uz'))

    def en(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=lang.set_lang(update.message.replace("/en", ""), 'en'))

    def fr(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=lang.set_lang(update.message.replace("/fr", ""), 'fr'))

    def de(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=lang.set_lang(update.message.replace("/de", ""), 'de'))


    def start_pooling(self):
        self.updater.start_polling()


telegram_bot = Telegram()  # Init the class of Telegram


# Registration of different handlers of the bot
start_handler = CommandHandler('start', telegram_bot.start)
telegram_bot.dispatcher.add_handler(start_handler)

# Get any word/sentence and auto-detect the lang of it
echo_handler = MessageHandler(Filters.text, telegram_bot.echo)
telegram_bot.dispatcher.add_handler(echo_handler)

# Telegram handler for Russian
ru_handler = CommandHandler('ru', telegram_bot.ru)
telegram_bot.dispatcher.add_handler(ru_handler)

# Telegram handler for English
en_handler = CommandHandler('en', telegram_bot.en)
telegram_bot.dispatcher.add_handler(en_handler)

# Telegram handler for Uzbek
uz_handler = CommandHandler('uz', telegram_bot.uz)
telegram_bot.dispatcher.add_handler(uz_handler)

# Telegram handler for French
fr_handler = CommandHandler('fr', telegram_bot.fr)
telegram_bot.dispatcher.add_handler(fr_handler)

# Telegram handler for German
de_handler = CommandHandler('de', telegram_bot.de)
telegram_bot.dispatcher.add_handler(de_handler)

telegram_bot.start_pooling()  # Starting pooling the requests, it starts the bot

