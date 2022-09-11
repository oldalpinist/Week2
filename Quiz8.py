import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

today = '11/09/2022'
planet_of_solarsystem_dict = {'Mercury': ephem.Mercury, 'Venus': ephem.Venus(today),
                              'Mars': ephem.Mars(today), 'Saturn': ephem.Saturn(today), 'Jupiter': ephem.Jupiter(today),
                              'Neptune': ephem.Neptune(today), 'Uranus': ephem.Uranus(today)}

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Вызван /Start')
    update.message.reply_text('Ну здравствуй, пользователь - назови планету или нажми для повтора //Start')


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def which_constellation(bot, update):
    planet_name = update.message.text.split()[1]
    ephem_body = planet_of_solarsystem_dict.get(planet_name, None)
    ephem_body = planet_of_solarsystem_dict.get.get(planet_name, None)
    if ephem_body != None:
        constellation = ephem.constellation(planet_of_solarsystem_dict[planet_name])
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('Try again this is planet not from solar system!')





if __name__ == "__main__":
    main()
