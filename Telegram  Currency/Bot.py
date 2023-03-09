from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='TOKEN', use_context=True)


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hello! I'm a bot. How can I help you?")


updater.dispacher.add_handler(CommandHandler('start', start))
updater.start_polling()