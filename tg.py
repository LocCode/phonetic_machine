'''
This is the module for connecting with Telegram Bot
'''


# Import diffrent telegram libs
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

# Импорт модуля английского языка
import eng_lang
# Импорт модуля русского языка
import ru_lang

my_tg_token = '882261003:AAEsahXWDo6AOkLrfC1NbfVEUF7v0Ki0CiY'
# Different stuff from Telegram documentation
bot = telegram.Bot(token=my_tg_token)
updater = Updater(token=my_tg_token, use_context=True)
dispatcher = updater.dispatcher
# Logger from Telegram
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Show the information about the bot
print(bot.get_me())

# Show received messages
updates = bot.get_updates()
print([u.message.text for u in updates])

chat_id = bot.get_updates()[-1].message.chat_id


# Send message to the user
def send_message_to_user(text):
    bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')


# First message from the user
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm Phonetic Machine bot. Firstly choose the language.")


# Adding function "Start" to the dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Analyzing russian word
def ru(update, context):
    word = update.message.text.replace("/ru", "")
    word_result = ru_lang.get_russian_word(word)

    # Выводим результаты фонетического анализа слова
    print("\nРезультат фонетического анализа слова «", word, "»")

    # Вывод количества букв в вводимом слове
    print("\nВсего букв в слове «", word, "»:", word_result[0])

    # Вывод количества гласных и их количества
    print("\nВсего гласных в слове «", word, "»:", len(word_result[1]))
    print("Список гласных в слове: «", word, "»:", word_result[1])

    # Вывод количества согласных и их количества
    print("\nВсего согласных в слове «", word, "»:", len(word_result[2]))
    print("Список согласных в слове: «", word, "»:", word_result[2])

    context.bot.send_message(chat_id=update.message.chat_id, text=word_result)


ru_handler = CommandHandler('ru', ru)
dispatcher.add_handler(ru_handler)


# Analyzing english word
def eng(update, context):
    print(update.message.text)
    word = update.message.text.replace("/eng", "")
    word_result = eng_lang.get_english_word(word)

    # Выводим результаты фонетического анализа слова
    message_result = "\nThe result of phonetic analysis of the word «", word, "» " \
                                                                          "\nTotal letters in the «", word, "»:", word_result[0]
    "\nTotal consonants in the word «", word, "»:", len(word_result[1]), "" \
                                                                         "\nThe list of consonants of the word: «", word, "»:", word_result[1],
    "\nTotal vowels in the word «", word, "»:", len(word_result[2]),\
    "\nThe list of vowels of the word: «", word, "»:", word_result[2]

    context.bot.send_message(chat_id=update.message.chat_id, text=message_result)


eng_handler = CommandHandler('eng', eng)
dispatcher.add_handler(eng_handler)


# Into Caps function with inline mode
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


# Adding function "inline_caps" to the dispatcher
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


# Wait for the messages
updater.start_polling()


# Unknown command was send
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)