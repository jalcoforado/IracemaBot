from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
from datetime import datetime
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

Localizacao = {}
def start(bot, update):
    print("Start")
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
    Localizacao[update.message.from_user.first_name] = (datetime.now,args[0:])
    print(Localizacao)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ondeesta(bot, update, args):
    global Localizacao
    response_message = Localizacao[args[0]] 
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
    


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()