import logging
import ephem
import datetime
import settings
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def greet_user(update, context):
    print('Вызван /start')
    print(update['message']['text'])
    update.message.reply_text('Здравствуй, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f"Ты сказал *{user_text}*.\nи получил ответ _{user_text} _но все же назови планету!",
                              parse_mode='MARKDOWN')


def planet_place(update, context):
    user_text = update.message.text
    text_data = user_text.split()
    if not len(text_data) > 1:
        return update.message.reply_text("Надо назвать планету")

    planet_name = text_data[1].strip()
    if not hasattr(ephem, planet_name):
        return update.message.reply_text("Назови другую планету!")

    planet_data = getattr(ephem, planet_name)
    current_date = date.today()
    planet_data = planet_data(current_date)
    constellation = ephem.constellation(planet_data)
    update.message.reply_text(f'Планета *{planet_name}* сейчас в *{constellation}*.', parse_mode='MARKDOWN')

def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",  greet_user))
    dp.add_handler(CommandHandler("planet",  planet_place))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

    main()
