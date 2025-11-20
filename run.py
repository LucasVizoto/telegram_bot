from src.integrations.telegram_comunicator import bot

import src.main.routes.__commands_imports 

if __name__ == '__main__':
    print('The bot is runnig now!!')
    bot.polling()