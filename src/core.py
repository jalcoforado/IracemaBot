from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL

Localizacao = []
def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_CATS_URL + args[0]
    )


def avisar(bot, update, args):
    response_message = "Ok "+update.message.from_user.first_name+u", até ja!"
    global Localizacao
    Localizacao[update.message.from_user.first_name] = args[0:]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ondeesta(bot, update, args):
    global Localizacao
    response_message = Localizacao[update.message.from_user.first_name] 
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
 


def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    try:
        updater = Updater(token=TELEGRAM_TOKEN)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(
            CommandHandler('start', start)
        )
        dispatcher.add_handler(
            CommandHandler('avisar', avisar, pass_args=True)
        )
        dispatcher.add_handler(
            CommandHandler('ondeesta', ondeesta, pass_args=True)
        )
        dispatcher.add_handler(
            CommandHandler('http', http_cats, pass_args=True)
        )
        dispatcher.add_handler(
            MessageHandler(Filters.command, unknown)
        )

        updater.start_polling()

        updater.idle()
    except expression as identifier:
        print (expression.message)
    


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()