from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# створюємо функцію-відповідь на команду /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привіт, я бот для конвертації валют! "
                                  "Введіть /help щоб дізнатися більше.")


# створюємо функцію-відповідь на команду /help
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я можу конвертувати валюту за офіційним "
                                  "курсом НБУ. Введіть /list, щоб подивитися "
                                  "доступні валюти для конвертації.")


# створюємо функцію-відповідь на команду /list
def list_currencies(update, context):
    text = "Доступні валюти для конвертації: USD, EUR, GBP"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


# створюємо функцію-відповідь на повідомлення з текстом
def convert_currency(update, context):
    text = update.message.text.upper()
    if text in ["USD", "EUR", "GBP"]:
        # TODO: зробити конвертацію валют тут
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Ви хочете конвертувати {text}!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Недоступна валюта для конвертації. "
                                      "Введіть /list, щоб подивитися "
                                      "доступні валюти.")


# створюємо функцію-відповідь на невідому команду
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Хм, я не розумію що ви маєте на увазі. "
                                  "Введіть /help, щоб побачити список "
                                  "доступних команд.")


# створюємо екземпляр клієнта
updater = Updater(bot_token='6257996334:AAGA4O_RAT1OOM8EUNZ6ckazByrl-zjbH9A',
                  use_context=True)

# створюємо диспетчер для обробки команд
dispatcher = updater.dispatcher

# додаємо обробник для команд
