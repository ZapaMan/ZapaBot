import telegram
from telegram.ext import Updater, CommandHandler
import logging

bot = telegram.Bot(token='536256966:AAHagBitKv_aLWP3ggpLZaXyoFeX-e9fCDk')

updater = Updater(token='536256966:AAHagBitKv_aLWP3ggpLZaXyoFeX-e9fCDk')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %name(s) - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Soy un bot, dime cosas guarras\n\n"
                                                          "Si tan torpe eres que necesitas que te guíe,"
                                                          "dime /ayuda (so memo)")


def fiesta(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="FIESTA DE LA TOGA\nFIESTA DE LA TOGA")


def ayuda(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Puedes preguntarme por /fiesta o por /negocio.\n\n"
                                                          "¿Qué querías?¿Lecciones de física cuántica, pringadiglio?")


def negocio(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Voy a montar mi propio parque de atracciones\n"
                                                          "Con casinos!! Y furcias!!!\n")
    bot.send_message(chat_id=update.message.chat_id, text="Es más: OLVIDA LOS CASINOS!!")


start_handler = CommandHandler('start', start)
fiesta_handler = CommandHandler('fiesta', fiesta)
negocio_handler = CommandHandler('negocio', negocio)
ayuda_handler = CommandHandler('ayuda', ayuda)

dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(fiesta_handler)
dispatcher.add_handler(negocio_handler)

updater.start_polling()
