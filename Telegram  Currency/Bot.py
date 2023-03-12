from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='6257996334:AAGA4O_RAT1OOM8EUNZ6ckazByrl-zjbH9A',
                  use_context=True)


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hello! I'm a bot. How can I help you?")


updater.dispacher.add_handler(CommandHandler('start', start))
updater.start_polling()